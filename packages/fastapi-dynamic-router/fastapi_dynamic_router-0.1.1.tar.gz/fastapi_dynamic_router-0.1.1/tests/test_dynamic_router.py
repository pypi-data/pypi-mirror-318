"""Test cases for FastAPI Dynamic Router."""
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_dynamic_router import DynamicRouter
from pathlib import Path

@pytest.fixture
def app():
    app = FastAPI()
    return app

@pytest.fixture
def client(app):
    return TestClient(app)

def test_init_app(app):
    router = DynamicRouter(app)
    assert hasattr(app.state, 'dynamic_router_config')

def test_default_config(app):
    router = DynamicRouter(app)
    assert app.state.dynamic_router_config['case_sensitive'] is True
    assert app.state.dynamic_router_config['prefix'] == ''

def test_invalid_routes_path(app):
    router = DynamicRouter(app)
    with pytest.raises(FileNotFoundError):
        router.register_routes('nonexistent_path')