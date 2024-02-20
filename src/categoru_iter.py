class CategoryIter:

    def __init__(self, category_object):
        self.category_object = category_object

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < len(self.category_object.products):
            self.value += 1
            return self.category_object.products[self.value - 1]
        else:
            raise StopIteration
