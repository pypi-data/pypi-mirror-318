"""Helper module to simplify route creation."""
from fastapi import APIRouter
from typing import Callable, Any, Dict
import sys

def create_route(path: str = "/", method: str = "get") -> Callable:
    """
    Decorator to create routes with minimal boilerplate.
    
    Args:
        path: Route path, defaults to "/"
        method: HTTP method, defaults to "get"
        
    Returns:
        Decorated function
    """
    def decorator(func: Callable) -> Callable:
        # Get the module where the decorated function is defined
        module = sys.modules[func.__module__]
        
        # Create router if it doesn't exist
        if not hasattr(module, 'router'):
            module.router = APIRouter()
            
        # Add route to the router
        getattr(module.router, method)(path)(func)
        return func
    
    return decorator