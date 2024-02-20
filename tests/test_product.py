import pytest
from src.product import Product
from src.category import Category


@pytest.fixture()
def product_test():
    return Product("apple", "red apples", 78.2, 120)


def test_init_product(product_test):
    assert product_test.title == "apple"
    assert product_test.description == "red apples"
    assert product_test.price == 78.2
    assert product_test.quantity == 120


def test_add_product_1(product_test):
    title = "Iphone 15"
    description = "128"
    price = 14000
    quantity = 100000
    lst = Category("Fruit", "Яблоки", [Product("apple", "red apples", 78.2, 120)])
    assert type(product_test.add_product(title, description, price, quantity, lst.products)) != list


def test_add_product_2(product_test):
    title = "apple"
    description = "128"
    price = 14000
    quantity = 100000
    lst = Category("Fruit", "Яблоки", [Product("apple", "red apples", 78.2, 120)])
    assert type(product_test.add_product(title, description, price, quantity, lst.products)) == list


def test_price(product_test):
    assert product_test.price == 78.2
    product_test.price = 100
    assert product_test.price == 100
    product_test.price = 0
    assert product_test.price == 100
    del product_test.price
    assert product_test.price == 0
