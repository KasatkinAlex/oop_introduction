from src.product import Product


class Smartphone(Product):
    """Класс-наследник от Product для категории товаров смартфоны"""

    efficiency: float  # производительность
    model: str  # модель
    internal_memory: int  # обьем встроенной памяти

    def __init__(self, title, description, price, quantity, efficiency, model, internal_memory, color):
        super().__init__(title, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.internal_memory = internal_memory
