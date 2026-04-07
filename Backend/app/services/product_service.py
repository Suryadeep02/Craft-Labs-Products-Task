from app.models.product import Product
from app.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo= repo

    def get_all_products(self) -> list[Product]:
        return self.repo.get_all_products()

    def get_third_product(self) -> Product| None:
        products = self.repo.get_all_products()     
        return products[2] if len(products) >=3 else None