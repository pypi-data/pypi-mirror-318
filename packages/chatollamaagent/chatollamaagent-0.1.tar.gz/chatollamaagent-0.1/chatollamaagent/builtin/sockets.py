from typing import Dict, Any
from ..core.socket import Socket

class FloatSocket(Socket):
    """Socket type for float values."""
    
    # Allow connection to other FloatSockets
    whitelist = {"FloatSocket"}
    blacklist = set()  # No blacklisted types
    socket_color = "#4CAF50"  # Material Design green 500
    
    def __init__(self, name: str, is_input: bool = True):
        super().__init__(name, "FloatSocket", is_input)
        self.value = 0.0  # Default value
        
    def set_value(self, value: Any):
        """Ensure value is converted to float."""
        try:
            float_value = float(value)
            super().set_value(float_value)
        except (ValueError, TypeError):
            print(f"Warning: Could not convert {value} to float, using 0.0")
            super().set_value(0.0)
            
    @staticmethod
    def get_ui_definition() -> Dict[str, Any]:
        """Define the UI for float input."""
        return {
            "inputs": [{
                "type": "float",
                "label": "Value",
                "default": 0.0,
                "min": float('-inf'),
                "max": float('inf'),
                "step": 0.1
            }],
            "color": "#4CAF50"  # Include color in UI definition
        } 

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