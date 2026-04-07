import pytest
from unittest.mock import MagicMock
from app.services.product_service import ProductService
from app.models.product import Product


@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def service(mock_repo):
    return ProductService(repo=mock_repo)

@pytest.fixture 
def sample_products():
    return [
        Product(id=1, name=" Samsmung S25 Ultra", description="Flagship smartphone from Samsung", price=99.00),
        Product(id=2, name= "Mechanical Keyboard", description="Cheery MX switches designed for gamign", price=49.99),
        Product(id=3, name= "Standing Desk", description="Height Adjustable electric standing desk", price=499.59)
    ]

def test_get_third_product_returns_third(service, mock_repo, sample_products):
    mock_repo.get_all_products.return_value = sample_products

    result = service.get_third_product()
    assert result is not None
    assert result.id == 3
    assert result.name == "Standing Desk"

    mock_repo.get_all_products.assert_called_once();