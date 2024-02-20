class Product:
    """Класс для предоставления продуктов"""
    title: str
    description: str
    price: float
    quantity: int

    def __init__(self, title, description, price, quantity):
        self.title = title
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.title}, {self.__price}, Остаток: {self.quantity} шт"

    def __add__(self, other):
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def add_product(cls, title, description, price, quantity, lst_product: []):
        """
        Создает товар и если он новый выдаст обьект класса
        если он уже есть в списке меняет остаток в списке
        :param title: имя товара
        :param description: опсание товара
        :param price: цена
        :param quantity: остаток
        :param lst_product: список товаров в категории
        :return: обьект класса или изменение остатка
        """
        product = cls(title, description, price, quantity)
        for i in lst_product:
            if product.title == i.title:
                i.quantity += product.quantity
                if product.price > i.price:
                    i.price = product.price
                print("Такой товар уже есть, его количество добавили в список")
                return lst_product
        return product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("цена введена некорректная")
        else:
            if new_price < self.__price:
                q = input("Подтвердите понижение цены Y-подтверждаю N-нет")
                if q.lower() == "y":
                    self.__price = new_price
            else:
                self.__price = new_price

    @price.deleter
    def price(self):
        self.__price = 0
