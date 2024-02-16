from src.utils import *
from src.product import Product
from src.category import Category


file_lst = read_json("products.json")
class_object_category_lst = []
class_object_product_lst = []

for i in file_lst:
    product_list_category = []

    for product in i["products"]:
        object_class_product = Product(product["name"], product["description"], product["price"], product["quantity"])
        product_list_category.append(object_class_product.title)
        class_object_product_lst.append(object_class_product)

    object_class_category = Category(i["name"], i["description"], product_list_category)
    class_object_category_lst.append(object_class_category)

object_dict = dict()
object_dict["Category"] = class_object_category_lst
object_dict["Product"] = class_object_product_lst

print(object_dict["Category"][0].title)
print(object_dict["Product"][0].title)
print(Category.total_number_categories)
