"""Example FastAPI application using dynamic router."""
from fastapi import FastAPI
from fastapi_dynamic_router import DynamicRouter
import uvicorn

app = FastAPI(title="Dynamic Router Example")
router = DynamicRouter(app)

# Register routes from the routes directory
router.register_routes("routes")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)