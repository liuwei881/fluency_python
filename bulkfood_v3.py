#coding=utf-8


class Quantity: # 1
    def __init__(self, storage_name):
        self.storage_name = storage_name    # 2

    def __set__(self, instance, value): # 3
        if value > 0:
            instance.__dict__[self.storage_name] = value    # 4
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity('weight') # 5
    price = Quantity('price')   # 6

    def __init__(self, description, weight, price): # 7
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price