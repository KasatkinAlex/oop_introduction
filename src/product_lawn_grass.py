from src.product import Product
from src.abstract_mixin_class import MixinRepr


class LawnGrass(Product, MixinRepr):

    producing_country: str  # страна-производитель
    germination_period: int  # срок прорастания

    def __init__(self, title, description, price, quantity, producing_country, germination_period, colour):
        self.producing_country = producing_country
        self.germination_period = germination_period
        super().__init__(title, description, price, quantity, colour)


p = LawnGrass(1, 2, 3, 4, 5, 6, 7)
