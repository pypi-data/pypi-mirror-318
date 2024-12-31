"""Helper module to simplify route creation."""
from fastapi import APIRouter
from typing import Callable, Any, Dict

def create_route(path: str = "/", method: str = "get") -> Callable:
    """
    Decorator to create routes with minimal boilerplate.
    
    Args:
        path: Route path, defaults to "/"
        method: HTTP method, defaults to "get"
    """
    router = APIRouter()
    
    def decorator(func: Callable) -> Dict[str, Any]:
        getattr(router, method)(path)(func)
        # Store the router instance in the module's namespace
        func.__module__.__dict__['router'] = router
        return func
    
    return decorator