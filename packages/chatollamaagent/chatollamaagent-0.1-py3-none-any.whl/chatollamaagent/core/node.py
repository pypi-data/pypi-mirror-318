from typing import List, Dict, Any, Type, Optional
from chatollama import Event
from .socket import Socket, FlowSocket

class Node:
    """Base class for all nodes in the system."""
    
    # Class-level attributes for node registration
    node_type: str = "base_node"  # Override in subclasses
    node_title: str = "Base Node"  # Override in subclasses
    
    def __init__(self):
        # Data sockets
        self.input_sockets: Dict[str, Socket] = {}
        self.output_sockets: Dict[str, Socket] = {}
        
        # Flow connections (separate from socket system)
        self.flow_in: Optional['Node'] = None  # Previous node in flow
        self.flow_out: Optional['Node'] = None  # Next node in flow
        
        self.position = (0, 0)  # Position in the node editor
        self.on_execute = Event()
        self.on_socket_connected = Event()
        self.on_socket_disconnected = Event()
        
    def add_input(self, name: str, socket_class: Type[Socket]) -> Socket:
        """Add an input socket to the node."""
        socket = socket_class(name, is_input=True)
        socket.node = self
        self.input_sockets[name] = socket
        return socket
        
    def add_output(self, name: str, socket_class: Type[Socket]) -> Socket:
        """Add an output socket to the node."""
        socket = socket_class(name, is_input=False)
        socket.node = self
        self.output_sockets[name] = socket
        return socket
        
    def remove_socket(self, name: str):
        """Remove a socket from the node."""
        if name in self.input_sockets:
            socket = self.input_sockets[name]
            socket.disconnect()
            del self.input_sockets[name]
        elif name in self.output_sockets:
            socket = self.output_sockets[name]
            socket.disconnect()
            del self.output_sockets[name]
    
    def connect_flow(self, next_node: 'Node') -> bool:
        """Connect this node's flow output to another node's input."""
        if self.flow_out:
            # Disconnect existing flow connection
            self.flow_out.flow_in = None
            self.flow_out = None
            
        self.flow_out = next_node
        next_node.flow_in = self
        return True
        
    def disconnect_flow(self):
        """Disconnect this node's flow connections."""
        if self.flow_out:
            self.flow_out.flow_in = None
            self.flow_out = None
        if self.flow_in:
            self.flow_in.flow_out = None
            self.flow_in = None
    
    def execute(self) -> Optional['Node']:
        """
        Execute the node's operation and return the next node in flow.
        """
        # Get input values
        inputs = {name: socket.get_value() for name, socket in self.input_sockets.items()}
        
        # Process inputs
        outputs = self.process(inputs)
        
        # Set output values
        for name, value in outputs.items():
            if name in self.output_sockets:
                self.output_sockets[name].set_value(value)
        
        # Return next node in flow
        return self.flow_out
        
    def process(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process the inputs and return outputs.
        Override this in subclasses to implement node behavior.
        """
        return {}
        
    @classmethod
    def get_ui_definition(cls) -> Dict[str, Any]:
        """
        Get the UI definition for this node type.
        Override this in subclasses to define custom UI.
        """
        return {
            "type": cls.node_type,
            "title": cls.node_title,
            "category": "General",
            "description": "",
            "inputs": [],
            "outputs": []
        }
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert node to dictionary for serialization."""
        return {
            "type": self.node_type,
            "position": self.position,
            "inputs": {
                name: socket.to_dict() 
                for name, socket in self.input_sockets.items()
            },
            "outputs": {
                name: socket.to_dict() 
                for name, socket in self.output_sockets.items()
            },
            "flow_out": self.flow_out.node_type if self.flow_out else None
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Node':
        """Create node from dictionary."""
        node = cls()
        node.position = tuple(data["position"])
        
        # Recreate sockets
        for name, socket_data in data["inputs"].items():
            socket = Socket.from_dict(socket_data)
            socket.node = node
            node.input_sockets[name] = socket
            
        for name, socket_data in data["outputs"].items():
            socket = Socket.from_dict(socket_data)
            socket.node = node
            node.output_sockets[name] = socket
            
        return node 