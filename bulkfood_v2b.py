#coding=utf-8


class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight    # 1
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    # @property   # 2
    # def weight(self):   # 3
    #     return self.__weight    # 4
    #
    # @weight.setter  # 5
    # def weight(self, value):
    #     if value > 0:
    #         self.__weight = value   # 6
    #     else:
    #         raise ValueError('value must be > 0')   # 7
    def get_weight(self):   # 1
        return self.__weight

    def set_weight(self, value):    # 2
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')
    weight = property(get_weight, set_weight)   # 3