from src.product import Product
from src.abstract_mixin_class import MixinRepr


class Category(MixinRepr):
    """Класс для предоставления категорий"""
    title: str
    description: str
    products: list

    total_number_categories = 0
    total_number_unique_products: int

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.__products = products
        Category.total_number_categories += 1
        super().__init__()

    def add_product(self, product_object):
        """ Добавление товара в категорию """
        if not isinstance(product_object, Product):
            return "товар не является объектом Product"
        elif product_object.quantity <= 0:
            raise ValueError("товар с нулевым количеством не может быть добавлен")
        else:
            self.__products.append(product_object)
            self.total_number_unique_products = len(set(self.__products))

    @property
    def products(self):
        return self.__products

    @property
    def product(self):
        q = []
        for i in self.__products:
            q.append(str(i))
        return q

    def __str__(self):
        return f"{self.title}, количество продуктов: {len(self)} шт"

    def __len__(self):
        total_number = 0
        for i in self.__products:
            total_number += i.quantity
        return total_number

    def medium_price(self):
        """ Подсчитывает средний ценник всех товаров """
        try:
            total_price = 0
            for i in self.__products:
                total_price += i.price
            medium_price = total_price/len(self.__products)
        except ZeroDivisionError:
            medium_price = 0
        return medium_price


if __name__ == "__main__":
    category = Category("Fruit", "Яблоки", [Product("apple", "red apples", 78.2, 120)])
    product = Product("apple", "big", 52.2, 0)
    category.add_product(product)
