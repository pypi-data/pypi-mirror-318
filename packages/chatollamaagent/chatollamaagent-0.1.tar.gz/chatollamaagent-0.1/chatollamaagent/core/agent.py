from typing import Dict, Type, List, Any, Optional
from chatollama import Event
from .node import Node
from .socket import Socket

class Agent:
    """
    Main class for managing nodes and their execution in the system.
    Handles node registration, instantiation, and execution flow.
    """
    
    def __init__(self):
        self.nodes: Dict[str, Node] = {}  # Active node instances
        self.registered_nodes: Dict[str, Type[Node]] = {}  # Available node types
        self.registered_sockets: Dict[str, Type[Socket]] = {}  # Available socket types
        
        # Events
        self.on_node_added = Event()
        self.on_node_removed = Event()
        self.on_node_executed = Event()
        self.on_connection_made = Event()
        self.on_connection_removed = Event()
        
    def register_node(self, node_class: Type[Node]) -> bool:
        """
        Register a new node type.
        Returns False if node_type already exists.
        """
        print(f"Registering node class: {node_class}")
        node_type = node_class.node_type
        print(f"Node type: {node_type}")
        if node_type in self.registered_nodes:
            print(f"Warning: Node type '{node_type}' is already registered.")
            return False
            
        self.registered_nodes[node_type] = node_class
        print(f"Successfully registered node. Current nodes: {self.registered_nodes}")
        return True
        
    def register_socket(self, socket_class: Type[Socket]) -> bool:
        """
        Register a new socket type.
        Returns False if socket_type already exists.
        """
        socket_type = socket_class.__name__
        if socket_type in self.registered_sockets:
            print(f"Warning: Socket type '{socket_type}' is already registered.")
            return False
            
        self.registered_sockets[socket_type] = socket_class
        return True
        
    def create_node(self, node_type: str) -> Optional[Node]:
        """Create a new instance of a registered node type."""
        print(f"Creating node of type: {node_type}")
        if node_type not in self.registered_nodes:
            print(f"Error: Unknown node type '{node_type}'")
            return None
            
        node_class = self.registered_nodes[node_type]
        print(f"Found node class: {node_class}")
        node = node_class()
        print(f"Created node instance: {node}")
        node_id = f"{node_type}_{len(self.nodes)}"
        self.nodes[node_id] = node
        
        # Setup event forwarding
        node.on_execute.on(lambda n: self.on_node_executed.trigger(node_id, n))
        node.on_socket_connected.on(lambda s1, s2: self.on_connection_made.trigger(node_id, s1, s2))
        node.on_socket_disconnected.on(lambda s: self.on_connection_removed.trigger(node_id, s))
        
        self.on_node_added.trigger(node_id, node)
        return node
        
    def remove_node(self, node_id: str) -> bool:
        """Remove a node instance."""
        if node_id not in self.nodes:
            return False
            
        node = self.nodes[node_id]
        
        # Disconnect all sockets
        for socket in list(node.input_sockets.values()) + list(node.output_sockets.values()):
            socket.disconnect()
            
        del self.nodes[node_id]
        self.on_node_removed.trigger(node_id, node)
        return True
        
    def connect_sockets(self, from_node_id: str, from_socket: str, 
                       to_node_id: str, to_socket: str) -> bool:
        """Connect two nodes' sockets."""
        if from_node_id not in self.nodes or to_node_id not in self.nodes:
            return False
            
        from_node = self.nodes[from_node_id]
        to_node = self.nodes[to_node_id]
        
        if from_socket not in from_node.output_sockets:
            return False
        if to_socket not in to_node.input_sockets:
            return False
            
        output_socket = from_node.output_sockets[from_socket]
        input_socket = to_node.input_sockets[to_socket]
        
        return output_socket.connect_to(input_socket)
        
    def disconnect_socket(self, node_id: str, socket_name: str) -> bool:
        """Disconnect a node's socket."""
        if node_id not in self.nodes:
            return False
            
        node = self.nodes[node_id]
        if socket_name in node.input_sockets:
            node.input_sockets[socket_name].disconnect()
            return True
        elif socket_name in node.output_sockets:
            node.output_sockets[socket_name].disconnect()
            return True
            
        return False
        
    def connect_flow(self, from_node_id: str, to_node_id: str) -> bool:
        """Connect two nodes' flow."""
        if from_node_id not in self.nodes or to_node_id not in self.nodes:
            return False
            
        from_node = self.nodes[from_node_id]
        to_node = self.nodes[to_node_id]
        
        return from_node.connect_flow(to_node)
        
    def disconnect_flow(self, node_id: str) -> bool:
        """Disconnect a node's flow connections."""
        if node_id not in self.nodes:
            return False
            
        self.nodes[node_id].disconnect_flow()
        return True
        
    def execute_node(self, node_id: str) -> bool:
        """Execute a specific node and follow the flow."""
        if node_id not in self.nodes:
            return False
            
        current_node = self.nodes[node_id]
        executed_nodes = set()  # Track executed nodes to handle cycles
        
        while current_node:
            if current_node.id in executed_nodes:
                # We've hit a cycle, but that's okay - just stop here
                break
                
            executed_nodes.add(current_node.id)
            next_node = current_node.execute()
            
            # Trigger execution event
            self.on_node_executed.trigger(current_node.id, current_node)
            
            current_node = next_node
            
        return True
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert agent state to dictionary for serialization."""
        return {
            "nodes": {
                node_id: node.to_dict()
                for node_id, node in self.nodes.items()
            }
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Agent':
        """Create agent from dictionary."""
        agent = cls()
        
        # First create all nodes
        for node_id, node_data in data["nodes"].items():
            node_type = node_data["type"]
            if node_type in agent.registered_nodes:
                node = agent.registered_nodes[node_type].from_dict(node_data)
                agent.nodes[node_id] = node
                
        # Then restore connections
        # TODO: Implement connection restoration
        
        return agent 