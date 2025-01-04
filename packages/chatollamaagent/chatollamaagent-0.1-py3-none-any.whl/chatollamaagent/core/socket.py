from typing import Dict, Any, Optional, Set

class Socket:
    """Base class for all sockets in the node system."""
    
    # Class-level attributes for connection rules
    whitelist: Set[str] = set()  # Socket types that can connect to this socket
    blacklist: Set[str] = set()  # Socket types that cannot connect to this socket
    socket_color = "#666666"  # Default socket color
    
    def __init__(self, name: str, socket_type: str, is_input: bool = True):
        self.name = name
        self.socket_type = socket_type
        self.is_input = is_input
        self.node = None  # Set when added to a node
        self.connected_to = None  # Reference to connected socket
        self.value = None  # Current value
        
    @property
    def is_connected(self) -> bool:
        """Check if the socket is connected to another socket."""
        return self.connected_to is not None
        
    def can_connect_to(self, other_socket: 'Socket') -> bool:
        """
        Check if this socket can connect to another socket.
        Connection is allowed if:
        1. One socket is input and other is output
        2. Neither socket has blacklisted the other's type
        3. At least one socket has whitelisted the other's type OR both have empty whitelists
        """
        # Check input/output compatibility
        if self.is_input == other_socket.is_input:
            return False  # Can't connect inputs to inputs or outputs to outputs
            
        # Check blacklists first - if either socket blacklists the other, no connection
        if self.socket_type in other_socket.blacklist or other_socket.socket_type in self.blacklist:
            return False
            
        # If both whitelists are empty, allow connection (unless same type)
        if not self.whitelist and not other_socket.whitelist:
            return self.socket_type == other_socket.socket_type
            
        # Check whitelists - at least one socket must whitelist the other's type
        can_connect = (other_socket.socket_type in self.whitelist or 
                      self.socket_type in other_socket.whitelist)
        
        return can_connect
        
    def connect_to(self, other_socket: 'Socket') -> bool:
        """Connect this socket to another socket."""
        if not self.can_connect_to(other_socket):
            return False
            
        # Disconnect existing connections
        self.disconnect()
        other_socket.disconnect()
        
        # Make new connection
        self.connected_to = other_socket
        other_socket.connected_to = self
        return True
        
    def disconnect(self):
        """Disconnect this socket from any connections."""
        if self.connected_to:
            other = self.connected_to
            self.connected_to = None
            other.connected_to = None
            
    def get_value(self) -> Any:
        """Get the current value of the socket."""
        if self.is_input and self.connected_to:
            return self.connected_to.get_value()
        return self.value
        
    def set_value(self, value: Any):
        """Set the value of the socket."""
        if value != self.value:
            self.value = value
            
    @staticmethod
    def get_ui_definition() -> Dict[str, Any]:
        """
        Get the UI definition for this socket type.
        Override this in subclasses to define custom UI.
        """
        return {
            "inputs": []  # List of input definitions
        }
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert socket to dictionary for serialization."""
        return {
            "name": self.name,
            "type": self.socket_type,
            "is_input": self.is_input,
            "value": self.value
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Socket':
        """Create socket from dictionary."""
        socket = cls(data["name"], data["type"], data["is_input"])
        socket.value = data.get("value")
        return socket 

class FlowSocket(Socket):
    """Socket type for execution flow control."""
    
    whitelist = {"FlowSocket"}
    blacklist = set()
    socket_color = "#FF5722"  # Material Design deep orange
    
    def __init__(self, name: str, is_input: bool = True):
        super().__init__(name, "FlowSocket", is_input)
        self.value = None
        
    def connect_to(self, other_socket: 'Socket') -> bool:
        """Override to enforce single output connection rule."""
        if not self.is_input and self.connected_to:
            # Flow outputs can only connect to one input
            return False
        return super().connect_to(other_socket) 