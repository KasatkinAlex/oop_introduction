import json


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
        self.total_number_categories += 1
        self.total_number_unique_products = len(products)


class Product:
    """Класс для предоставления продуктов"""
    title: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, title, description, price, quantity_in_stock):
        self.title = title
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock


def read_json(fail_json):
    """Считывание файла json и создание списка экземпляров класса
    return: словарь Category : 'список экземляров класса Category', Product : 'список экземпляров класса Product
    """
    with open(fail_json, "rt", encoding="utf-8") as fail:
        fail_lst = json.load(fail)

    class_object_category_lst = []
    class_object_product_lst = []

    for i in fail_lst:
        product_list_category = []

        for product in i["products"]:
            product_list_category.append(product["name"])
            object_class_product = Product(product["name"], product["description"], product["price"], product["quantity"])
            class_object_product_lst.append(object_class_product)

        object_class_category = Category(i["name"], i["description"], product_list_category)
        class_object_category_lst.append(object_class_category)

    object_dict = dict()
    object_dict["Category"] = class_object_category_lst
    object_dict["Product"] = class_object_product_lst

    return object_dict


object_dict_class = read_json("products.json")
print(object_dict_class["Category"][0].title)
print(object_dict_class["Product"][0].title)
