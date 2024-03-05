from src.abstract_mixin_class import MixinRepr


class Order(MixinRepr):
    """ Класс «Заказ», в котором будет ссылка на то, какой товар был куплен, количество купленного товара,
    а также итоговая стоимость"""
    name: str  # название товара
    quantity: int  # количество товара
    price: int  # цена товара

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.__price = price
        print(self.__str__())
        super().__init__()

    @property
    def price(self):
        return self.__price

    @property
    def get_total_cost(self):
        if isinstance(self.quantity, int) and isinstance(self.__price, int):
            return self.quantity * self.__price
        return 0
    
    def __str__(self):
        return f"Товар {self.name}, Кол-во {self.quantity}, Общая стоимость {self.get_total_cost} "

    
q = Order("qwerty", 10, 10)
