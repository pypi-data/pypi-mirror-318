import asyncio
import websockets
import webbrowser
import os
import signal
import sys
import json
from pathlib import Path
from .config import config
from chatollama import Event
from .core.agent import Agent
from .builtin import register_builtins

class Interface:
    def __init__(self):
        self.server = None
        self.should_exit = False
        self.agent = Agent()
        
        # Register builtin nodes and sockets
        register_builtins(self.agent)
        
        # Events
        self.on_setting_change = Event()
        self.on_connection_change = Event()
        self.on_websocket_message = Event()
        self._setup_signal_handlers()
        self._setup_agent_handlers()

    def _setup_signal_handlers(self):
        # Handle Ctrl+C gracefully
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

    def _setup_agent_handlers(self):
        """Setup handlers for agent events."""
        self.agent.on_node_added.on(self._handle_node_added)
        self.agent.on_node_removed.on(self._handle_node_removed)
        self.agent.on_connection_made.on(self._handle_connection_made)
        self.agent.on_connection_removed.on(self._handle_connection_removed)
        self.agent.on_node_executed.on(self._handle_node_executed)

    def _signal_handler(self, signum, frame):
        self.should_exit = True
        if self.server:
            self.server.close()
        sys.exit(0)

    async def _handle_websocket(self, websocket):
        try:
            # Trigger connection event
            await asyncio.get_event_loop().run_in_executor(
                None, 
                lambda: self.on_connection_change.trigger(True)
            )
            
            # Send initial node registry
            await self._send_node_registry(websocket)
            
            while not self.should_exit:
                try:
                    message = await websocket.recv()
                    data = json.loads(message)
                    
                    # Trigger raw message event
                    responses = await asyncio.get_event_loop().run_in_executor(
                        None, 
                        lambda: self.on_websocket_message.trigger(data)
                    )
                    
                    await self._handle_message(websocket, data)
                    
                except websockets.exceptions.ConnectionClosed:
                    print("Browser disconnected")
                    self.should_exit = True
                    break
        finally:
            # Ensure we exit when the connection is closed
            self.should_exit = True
            # Trigger disconnection event
            await asyncio.get_event_loop().run_in_executor(
                None, 
                lambda: self.on_connection_change.trigger(False)
            )
            if self.server:
                self.server.close()

    async def _send_node_registry(self, websocket):
        """Send the available nodes to the client."""
        print("Preparing to send node registry")
        print("Registered nodes:", self.agent.registered_nodes)
        
        registry = {
            "type": "node_registry",
            "nodes": [
                {
                    **node_class.get_ui_definition(),
                    "type": node_class.node_type,
                    "title": node_class.node_title
                }
                for node_class in self.agent.registered_nodes.values()
            ]
        }
        print("Sending node registry:", registry)
        await websocket.send(json.dumps(registry))

    async def _handle_message(self, websocket, data):
        """Handle incoming websocket messages."""
        msg_type = data.get('type')
        print(f"Received message: {msg_type}", data)
        
        if msg_type == 'get_setting':
            # Handle settings request
            value = config.get(data['key'])
            response = {
                'type': 'setting',
                'key': data['key'],
                'value': value
            }
            await websocket.send(json.dumps(response))
            
        elif msg_type == 'set_setting':
            # Handle settings update
            success = config.set(data['key'], data['value'])
            await asyncio.get_event_loop().run_in_executor(
                None, 
                lambda: self.on_setting_change.trigger(data['key'], data['value'])
            )
            response = {
                'type': 'setting_response',
                'success': success,
                'key': data['key'],
                'value': data['value']
            }
            await websocket.send(json.dumps(response))
            
        elif msg_type == 'create_node':
            # Handle node creation
            print("Creating node:", data['node_type'])
            node = self.agent.create_node(data['node_type'])
            print("Created node:", node)
            if node:
                # Set the node position from the drop coordinates
                node.position = tuple(data.get('position', (0, 0)))
                print("Set node position:", node.position)
                # Generate a unique node ID
                node_id = f"{data['node_type']}_{len(self.agent.nodes)}"
                print("Generated node ID:", node_id)
                # Add the node to the agent's node registry
                self.agent.nodes[node_id] = node
                print("Added node to registry. Current nodes:", self.agent.nodes)
                # Send response with node data
                response = {
                    'type': 'node_created',
                    'node_id': node_id,
                    'node_data': node.to_dict()
                }
                print("Sending response:", response)
                await websocket.send(json.dumps(response))
            else:
                print("Failed to create node")
                
        elif msg_type == 'connect_nodes':
            # Handle node connection
            success = self.agent.connect_sockets(
                data['from_node'], data['from_socket'],
                data['to_node'], data['to_socket']
            )
            response = {
                'type': 'connection_response',
                'success': success,
                'connection': data
            }
            await websocket.send(json.dumps(response))
            
        elif msg_type == 'execute_node':
            # Handle node execution
            success = self.agent.execute_node(data['node_id'])
            response = {
                'type': 'execution_response',
                'success': success,
                'node_id': data['node_id']
            }
            await websocket.send(json.dumps(response))

        elif msg_type == 'update_node_position':
            # Handle node position update
            node_id = data['node_id']
            if node_id in self.agent.nodes:
                node = self.agent.nodes[node_id]
                node.position = tuple(data['position'])
                response = {
                    'type': 'position_updated',
                    'node_id': node_id,
                    'position': node.position
                }
                await websocket.send(json.dumps(response))

    def _handle_node_added(self, node_id, node):
        """Handle node added event."""
        if self.server and hasattr(self.server, 'websockets') and self.server.websockets:
            asyncio.create_task(self._broadcast({
                'type': 'node_added',
                'node_id': node_id,
                'node_data': node.to_dict()
            }))

    def _handle_node_removed(self, node_id, node):
        """Handle node removed event."""
        if self.server and hasattr(self.server, 'websockets') and self.server.websockets:
            asyncio.create_task(self._broadcast({
                'type': 'node_removed',
                'node_id': node_id
            }))

    def _handle_connection_made(self, node_id, socket1, socket2):
        """Handle connection made event."""
        if self.server and hasattr(self.server, 'websockets') and self.server.websockets:
            asyncio.create_task(self._broadcast({
                'type': 'connection_made',
                'node_id': node_id,
                'socket1': socket1.name,
                'socket2': socket2.name
            }))

    def _handle_connection_removed(self, node_id, socket):
        """Handle connection removed event."""
        if self.server and hasattr(self.server, 'websockets') and self.server.websockets:
            asyncio.create_task(self._broadcast({
                'type': 'connection_removed',
                'node_id': node_id,
                'socket': socket.name
            }))

    def _handle_node_executed(self, node_id, node):
        """Handle node executed event."""
        if self.server and hasattr(self.server, 'websockets') and self.server.websockets:
            asyncio.create_task(self._broadcast({
                'type': 'node_executed',
                'node_id': node_id,
                'outputs': {
                    name: socket.get_value()
                    for name, socket in node.output_sockets.items()
                }
            }))

    async def _broadcast(self, message):
        """Broadcast a message to all connected clients."""
        if self.server and hasattr(self.server, 'websockets') and self.server.websockets:
            websockets.broadcast(self.server.websockets, json.dumps(message))

    async def _start_server(self):
        self.server = await websockets.serve(
            self._handle_websocket, 
            'localhost', 
            8765
        )
        await self.server.wait_closed()

    def run(self):
        # Get the path to the UI files
        ui_dir = Path(__file__).parent / 'ui'
        index_path = ui_dir / 'index.html'
        
        # Open the browser
        webbrowser.open(f'file://{index_path.absolute()}')

        # Start the WebSocket server
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self._start_server())
        except KeyboardInterrupt:
            pass
        finally:
            loop.close() 