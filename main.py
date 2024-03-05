from src.utils import *
from src.product import Product
from src.category import Category
from src.categoru_iter import CategoryIter


file_lst = read_json("products.json")
class_object_category_lst = []


for i in file_lst:
    class_object_product_lst = []
    product_list_category = []

    for product in i["products"]:
        object_class_product = Product(product["name"], product["description"], product["price"], product["quantity"])
        # print(object_class_product.__repr__())
        class_object_product_lst.append(object_class_product)

    object_class_category = Category(i["name"], i["description"], class_object_product_lst)
    class_object_category_lst.append(object_class_category)

title = "Iphone 1"
description = "128"
price = 14000
quantity = 1

nwe_product = Product.add_product(title, description, price, quantity, class_object_category_lst[0].products)

if type(nwe_product) != list:
    class_object_category_lst[0].add_product(nwe_product)

# print(class_object_category_lst[0].product)
# print(class_object_category_lst[0])
# q = CategoryIter(category_object=class_object_category_lst[0])
# for i in q:
#     print(i)

product_1 = Product("name123", "discription", 10000, 2)
# print(product_1.__repr__())
# print(class_object_category_lst[0].__repr__())
