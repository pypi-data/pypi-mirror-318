from fastapi_dynamic_router import create_route

@create_route("/")
def list_users():
    return {"message": "List of users"}