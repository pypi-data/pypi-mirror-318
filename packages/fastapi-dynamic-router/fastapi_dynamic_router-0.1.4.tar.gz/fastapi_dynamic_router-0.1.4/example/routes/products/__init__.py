"""Products endpoints."""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_products():
    return {"message": "List of products"}