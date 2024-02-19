from src.category import Category
from src.product import Product
import pytest


@pytest.fixture()
def category_test():
    return Category("Fruit", "Яблоки", [Product("apple", "red apples", 78.2, 120)])


def test_init_category(category_test):
    assert category_test.title == "Fruit"
    assert category_test.description == "Яблоки"
    # assert category_test.products == ["bananas", "oranges", "apples"]
    assert category_test.total_number_categories == 1
    # assert category_test.total_number_unique_products == 1


def test_add_product(category_test):
    category_test.add_product(["banana", "big", 52.2, 100])
    assert category_test.total_number_unique_products == 2


def test_printing_product(category_test):
    assert category_test.product == ["apple, 78.2, Остаток: 120"]
