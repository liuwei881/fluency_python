#coding=utf-8


def quantity(storage_name): # 1

    def qty_getter(instance):   # 2
        return instance.__dict__[storage_name]  # 3

    def qty_setter(instance, value):    # 4
        if value > 0:
            instance.__dict__[storage_name] = value # 5
        else:
            raise ValueError('value must be > 0')
    return property(qty_getter, qty_setter) # 6


class LineItem:
    weight = quantity('weight') # 1
    price = quantity('price')   # 2

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight    # 3
        self.price = price

    def subtotal(self):
        return self.weight * self.price # 4