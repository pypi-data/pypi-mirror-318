"""Module for handling route registration logic."""
from pathlib import Path
from fastapi import FastAPI, APIRouter
import importlib.util

class RouteRegistrar:
    """Handles the registration of routes and routers."""
    
    def __init__(self, app: FastAPI):
        self.app = app
        
    def register_router(self, file_path: Path, prefix: str) -> None:
        """
        Register an APIRouter from a route file.
        
        Args:
            file_path: Path to the route file
            prefix: URL prefix for the router
        """
        module_name = file_path.parent.name
        
        # Import the module
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None or spec.loader is None:
            return
            
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Check for APIRouter instance
        if hasattr(module, 'router') and isinstance(module.router, APIRouter):
            if not self.app.state.dynamic_router_config['case_sensitive']:
                prefix = prefix.lower()
                
            full_prefix = f"{self.app.state.dynamic_router_config['prefix']}/{prefix}".rstrip('/')
            self.app.include_router(module.router, prefix=full_prefix)