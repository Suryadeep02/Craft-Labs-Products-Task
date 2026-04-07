from app.models.product import Product

MOCK_PRODUCTS = [
    Product(id=1, name=" Samsmung S25 Ultra", description="Flagship smartphone from Samsung", price=99.00),
    Product(id=2, name= "Mechanical Keyboard", description="Cheery MX switches designed for gamign", price=49.99),
    Product(id=3, name= "Standing Desk", description="Height Adjustable electric standing desk", price=499.59),
    Product(id=4, name= "Samsung Refigertaor", description="Refrigerator for Hosuehold", price=199.49)
]


class ProductRepository: 
    def get_all_products(self) -> list[Product]:
        return MOCK_PRODUCTS
