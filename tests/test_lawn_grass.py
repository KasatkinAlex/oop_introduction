import pytest

from src.product_lawn_grass import LawnGrass


@pytest.fixture()
def lawn_grass_test():
    return LawnGrass ("qw", "qwerty", 120, 10, "USA", 12, "red")


def test_init(lawn_grass_test):
    assert lawn_grass_test.producing_country == "USA"
    assert lawn_grass_test.colour == "red"
