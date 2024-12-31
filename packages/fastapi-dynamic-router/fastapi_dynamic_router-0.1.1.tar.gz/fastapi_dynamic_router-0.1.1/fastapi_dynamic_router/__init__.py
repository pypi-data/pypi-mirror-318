"""
FastAPI Dynamic Router
------------------
A FastAPI extension for automatic and dynamic route registration.
"""
from .dynamic_router import DynamicRouter
from .route_helper import create_route

__version__ = '0.1.1'
__all__ = ['DynamicRouter', 'create_route']