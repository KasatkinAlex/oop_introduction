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
        self.products = products
        Category.total_number_categories += 1
        self.total_number_unique_products = len(products)
