import json


def read_json(file_json):
    """Считывание файла json и создание списка экземпляров класса
    return: словарь Category : 'список экземляров класса Category', Product : 'список экземпляров класса Product
    """
    with open(file_json, "rt", encoding="utf-8") as file:
        file_lst = json.load(file)
    return file_lst
