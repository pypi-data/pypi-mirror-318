from typing import Dict, Any
from ..core.node import Node
from .sockets import FloatSocket

class AddNode(Node):
    """Node that adds two float values."""
    
    node_type = "Add"
    node_title = "Add"
    
    def __init__(self):
        super().__init__()
        
        # Create input sockets
        self.add_input("A", FloatSocket)
        self.add_input("B", FloatSocket)
        
        # Create output socket
        self.add_output("Output", FloatSocket)
        
    def process(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Add the two input values."""
        # Get input values, default to 0.0 if not connected
        a = inputs.get("A", 0.0) or 0.0
        b = inputs.get("B", 0.0) or 0.0
        
        # Perform addition
        result = float(a) + float(b)
        
        return {
            "Output": result,
            "Flow": None  # Flow sockets don't need actual values
        }
    
    @classmethod
    def get_ui_definition(cls) -> Dict[str, Any]:
        """Define the UI for the Add node."""
        return {
            "type": cls.node_type,
            "title": cls.node_title,
            "category": "Math",
            "description": "Adds two float values together",
            "inputs": [
                {
                    "name": "A",
                    "type": "FloatSocket",
                    "description": "First value to add"
                },
                {
                    "name": "B",
                    "type": "FloatSocket",
                    "description": "Second value to add"
                }
            ],
            "outputs": [
                {
                    "name": "Output",
                    "type": "FloatSocket",
                    "description": "Sum of A and B"
                }
            ]
        }

class SubtractNode(Node):
    """Node that subtracts two float values."""
    
    node_type = "Subtract"
    node_title = "Subtract"
    
    def __init__(self):
        super().__init__()
        
        # Create input sockets
        self.add_input("A", FloatSocket)
        self.add_input("B", FloatSocket)
        
        # Create output socket
        self.add_output("Output", FloatSocket)
        
    def process(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Subtract B from A."""
        # Get input values, default to 0.0 if not connected
        a = inputs.get("A", 0.0) or 0.0
        b = inputs.get("B", 0.0) or 0.0
        
        # Perform subtraction
        result = float(a) - float(b)
        
        return {"Output": result}
    
    @classmethod
    def get_ui_definition(cls) -> Dict[str, Any]:
        """Define the UI for the Subtract node."""
        return {
            "type": cls.node_type,
            "title": cls.node_title,
            "category": "Math",
            "description": "Subtracts B from A",
            "inputs": [
                {
                    "name": "A",
                    "type": "FloatSocket",
                    "description": "Value to subtract from"
                },
                {
                    "name": "B",
                    "type": "FloatSocket",
                    "description": "Value to subtract"
                }
            ],
            "outputs": [
                {
                    "name": "Output",
                    "type": "FloatSocket",
                    "description": "Result of A - B"
                }
            ]
        }

class MultiplyNode(Node):
    """Node that multiplies two float values."""
    
    node_type = "Multiply"
    node_title = "Multiply"
    
    def __init__(self):
        super().__init__()
        
        # Create input sockets
        self.add_input("A", FloatSocket)
        self.add_input("B", FloatSocket)
        
        # Create output socket
        self.add_output("Output", FloatSocket)
        
    def process(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Multiply A and B."""
        # Get input values, default to 0.0 if not connected
        a = inputs.get("A", 0.0) or 0.0
        b = inputs.get("B", 0.0) or 0.0
        
        # Perform multiplication
        result = float(a) * float(b)
        
        return {"Output": result}
    
    @classmethod
    def get_ui_definition(cls) -> Dict[str, Any]:
        """Define the UI for the Multiply node."""
        return {
            "type": cls.node_type,
            "title": cls.node_title,
            "category": "Math",
            "description": "Multiplies two float values",
            "inputs": [
                {
                    "name": "A",
                    "type": "FloatSocket",
                    "description": "First value to multiply"
                },
                {
                    "name": "B",
                    "type": "FloatSocket",
                    "description": "Second value to multiply"
                }
            ],
            "outputs": [
                {
                    "name": "Output",
                    "type": "FloatSocket",
                    "description": "Product of A * B"
                }
            ]
        }

class DivideNode(Node):
    """Node that divides two float values."""
    
    node_type = "Divide"
    node_title = "Divide"
    
    def __init__(self):
        super().__init__()
        
        # Create input sockets
        self.add_input("A", FloatSocket)
        self.add_input("B", FloatSocket)
        
        # Create output socket
        self.add_output("Output", FloatSocket)
        
    def process(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Divide A by B."""
        # Get input values, default to 0.0 if not connected
        a = inputs.get("A", 0.0) or 0.0
        b = inputs.get("B", 0.0) or 0.0
        
        # Check for division by zero
        if b == 0:
            return {"Output": float('inf') if a >= 0 else float('-inf')}
        
        # Perform division
        result = float(a) / float(b)
        
        return {"Output": result}
    
    @classmethod
    def get_ui_definition(cls) -> Dict[str, Any]:
        """Define the UI for the Divide node."""
        return {
            "type": cls.node_type,
            "title": cls.node_title,
            "category": "Math",
            "description": "Divides A by B",
            "inputs": [
                {
                    "name": "A",
                    "type": "FloatSocket",
                    "description": "Numerator"
                },
                {
                    "name": "B",
                    "type": "FloatSocket",
                    "description": "Denominator"
                }
            ],
            "outputs": [
                {
                    "name": "Output",
                    "type": "FloatSocket",
                    "description": "Result of A / B"
                }
            ]
        } 