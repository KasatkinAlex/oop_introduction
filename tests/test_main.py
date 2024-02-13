from main import Category, Product
import pytest

@pytest.fixture()
def category_test():
    return Category("Fruit", "Fruit from Africa", ["bananas", "oranges", "apples"])


def test_init_category(category_test):
    assert category_test.title == "Fruit"
    assert category_test.description == "Fruit from Africa"
    assert category_test.products == ["bananas", "oranges", "apples"]
    assert category_test.total_number_categories == 1
    assert category_test.total_number_unique_products == 3


@pytest.fixture()
def product_test():
    return Product("apple", "red apples", 78.2, 120)


def test_init_product(product_test):
    assert product_test.title == "apple"
    assert product_test.description == "red apples"
    assert product_test.price == 78.2
    assert product_test.quantity_in_stock == 120
