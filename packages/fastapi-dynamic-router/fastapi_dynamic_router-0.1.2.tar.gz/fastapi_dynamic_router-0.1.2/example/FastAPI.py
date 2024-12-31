from fastapi import FastAPI
from fastapi_dynamic_router import DynamicRouter

# Create FastAPI app
app = FastAPI()

# Initialize the router
router = DynamicRouter(app)

# Register routes from a directory
router.register_routes('routes')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)