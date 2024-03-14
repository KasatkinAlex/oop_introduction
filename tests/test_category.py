from src.category import Category
from src.product import Product
import pytest


@pytest.fixture()
def category_test():
    return Category("Fruit", "Яблоки", [Product("apple", "red apples", 78.2, 120)])


def test_init_category(category_test):
    assert category_test.title == "Fruit"
    assert category_test.description == "Яблоки"
    # assert category_test.total_number_categories == 1


def test_add_product(category_test):
    """Тест на добавление товара Product"""
    category_test.add_product(Product("banana", "big", 52.2, 100))
    assert category_test.total_number_unique_products == 2


def test_add_product_now(category_test):
    """Тест на добавление товара не обьект класса Product"""
    assert category_test.add_product(1) == "товар не является объектом Product"


def test_printing_product(category_test):
    assert category_test.product == ["apple, 78.2, Остаток: 120 шт"]


def test_str(category_test):
    assert str(category_test) == "Fruit, количество продуктов: 120 шт"


def test_medium_price(category_test):
    assert category_test.medium_price() == 78.2


def test_medium_price_zero():
    category = Category(1, 2, [])
    assert category.medium_price() == 0
