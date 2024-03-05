from src.product import Product
from src.abstract_mixin_class import MixinRepr


class Smartphone(Product, MixinRepr):
    """Класс-наследник от Product для категории товаров смартфоны"""

    efficiency: float  # производительность
    model: str  # модель
    internal_memory: int  # обьем встроенной памяти

    def __init__(self, title, description, price, quantity, efficiency, model, internal_memory, color):
        self.efficiency = efficiency
        self.model = model
        self.internal_memory = internal_memory
        super().__init__(title, description, price, quantity, color)


p = Smartphone(1, 2, 3, 4, 5, 6, 7, 8)