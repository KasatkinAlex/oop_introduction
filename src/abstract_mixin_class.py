from abc import ABC, abstractmethod


class AbstractProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def price(self):
        return


class MixinRepr:

    def __init__(self, *args, **kwargs):
        super().__init__()
        print(self.__repr__())

    def __repr__(self):
        """ Функция возвращает строковое отображение объекта при его создании """
        values_lst = []
        for k, v in self.__dict__.items():
            values_lst.append(str(v))
        return f"|Класс: {self.__class__.__name__} Атрибуты: {" ". join(values_lst)}| "
