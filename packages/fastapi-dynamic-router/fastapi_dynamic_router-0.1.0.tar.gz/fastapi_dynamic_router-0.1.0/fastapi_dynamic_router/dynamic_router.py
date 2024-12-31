"""Main module for FastAPI Dynamic Router."""
from pathlib import Path
from typing import Optional, Union
from fastapi import FastAPI

from .route_registrar import RouteRegistrar
from .directory_processor import DirectoryProcessor

class DynamicRouter:
    """
    A class to handle dynamic route registration in FastAPI applications.
    """
    
    def __init__(self, app: Optional[FastAPI] = None):
        """
        Initialize the DynamicRouter extension.
        
        Args:
            app: Optional FastAPI application instance
        """
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: FastAPI) -> None:
        """
        Initialize the extension with the FastAPI application.
        
        Args:
            app: FastAPI application instance
        """
        self.app = app
        
        # Store configuration in state
        if not hasattr(app, 'state'):
            app.state.dynamic_router_config = {}
        app.state.dynamic_router_config.update({
            'case_sensitive': True,
            'prefix': ''
        })
        
        self.route_registrar = RouteRegistrar(app)
        self.directory_processor = DirectoryProcessor(self.route_registrar)

    def register_routes(self, routes_path: Union[str, Path]) -> None:
        """
        Register routes from the specified directory.
        
        Args:
            routes_path: Path to the routes directory
        """
        if isinstance(routes_path, str):
            routes_path = Path(routes_path)

        if not routes_path.exists():
            raise FileNotFoundError(f"Routes directory not found: {routes_path}")

        self.directory_processor.process_directory(routes_path)