from src.product import Product


class Category:
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

    def add_product(self, product_object):
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



