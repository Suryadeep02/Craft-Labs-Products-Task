from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService

router = APIRouter(prefix='/products', tags=['products'])

def get_service() -> ProductService:
    return ProductService(repo=ProductRepository())

@router.get("/", response_model=list[Product])
def list_products():
    return get_service().get_all_products()