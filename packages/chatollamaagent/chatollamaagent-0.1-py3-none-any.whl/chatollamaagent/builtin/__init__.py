from typing import List, Type
import inspect
from ..core.socket import Socket

# Remove direct Node import, we'll get it when needed
def get_all_nodes() -> List[Type['Node']]:
    """Get all node classes defined in the builtin nodes module."""
    from ..core.node import Node  # Import here instead
    from . import nodes
    return [
        cls for _, cls in inspect.getmembers(nodes, inspect.isclass)
        if issubclass(cls, Node) and cls != Node
    ]

def get_all_sockets() -> List[Type[Socket]]:
    """Get all socket classes defined in the builtin sockets module."""
    from . import sockets
    return [
        cls for _, cls in inspect.getmembers(sockets, inspect.isclass)
        if issubclass(cls, Socket) and cls != Socket
    ]

def register_builtins(agent) -> None:
    """Register all builtin nodes and sockets with the agent."""
    # Register sockets first
    for socket_class in get_all_sockets():
        agent.register_socket(socket_class)
        
    # Then register nodes
    for node_class in get_all_nodes():
        agent.register_node(node_class)

# Export everything for easy access
__all__ = [
    'register_builtins',
    'get_all_nodes',
    'get_all_sockets'
] 