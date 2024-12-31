"""Product reviews endpoint."""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_product_reviews(product_id: str):
    return {"message": f"Reviews for product ID: {product_id}"}