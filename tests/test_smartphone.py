import pytest

from src.product_smartpfone import Smartphone


@pytest.fixture()
def smartphone_test():
    return Smartphone("apple", "USA", 10000, 10, 16, 7, 128, "red")


def test_init(smartphone_test):
    assert smartphone_test.title == "apple"
    assert smartphone_test.model == 7
    assert smartphone_test.colour == "red"
