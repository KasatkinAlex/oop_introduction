from src.utils import *
from src.product import Product
from src.category import Category


file_lst = read_json("products.json")
class_object_category_lst = []


for i in file_lst:
    class_object_product_lst = []
    product_list_category = []

    for product in i["products"]:
        object_class_product = Product(product["name"], product["description"], product["price"], product["quantity"])
        class_object_product_lst.append(object_class_product)

    object_class_category = Category(i["name"], i["description"], class_object_product_lst)
    class_object_category_lst.append(object_class_category)

print(class_object_category_lst[0].printing_product)
print(Category.total_number_categories)

