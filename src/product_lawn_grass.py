from src.product import Product


class LawnGrass(Product):

    producing_country: str  # страна-производитель
    germination_period: int  # срок прорастания

    def __init__(self, title, description, price, quantity, producing_country, germination_period, colour):
        super().__init__(title, description, price, quantity, colour)
        self.producing_country = producing_country
        self.germination_period = germination_period
