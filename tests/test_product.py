import pytest
from src.product import Product

@pytest.fixture()
def product_test():
    return Product("apple", "red apples", 78.2, 120)


def test_init_product(product_test):
    assert product_test.title == "apple"
    assert product_test.description == "red apples"
    assert product_test.price == 78.2
    assert product_test.quantity == 120
