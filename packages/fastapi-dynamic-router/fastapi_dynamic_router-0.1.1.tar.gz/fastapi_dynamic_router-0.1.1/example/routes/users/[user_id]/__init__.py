from fastapi_dynamic_router import create_route

@create_route("/")
def get_user(user_id: str):
    return {"message": f"User details for ID: {user_id}"}