"""User details endpoint."""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_user(user_id: str):
    return {"message": f"User details for ID: {user_id}"}