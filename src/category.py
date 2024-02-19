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

    def add_product(self, product_object: list):
        self.__products.append(product_object)
        self.total_number_unique_products = len(self.__products)

    @property
    def products(self):
        return self.__products

    @property
    def product(self):
        q = []
        for i in self.__products:
            str_print = f"{i.title}, {i.price}, Остаток: {i.quantity}"
            q.append(str_print)
        return q


