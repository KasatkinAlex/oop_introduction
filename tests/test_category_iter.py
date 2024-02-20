import pytest
from src.category import Category
from src.product import Product
from src.categoru_iter import CategoryIter


@pytest.fixture()
def test_category_iter():
    return CategoryIter(Category("Fruit", "Яблоки", [Product("apple", "red apples", 78.2, 120)]))


def test_iter(test_category_iter):
    for i in test_category_iter:
        assert str(i) == "apple, 78.2, Остаток: 120 шт"
