#coding=utf-8


import itertools    # 1

from tombola import Tombola
from bingo import BingoCage


class AddableBingoCage(BingoCage):      # 2
    def __add__(self, other):
        if isinstance(other, Tombola):  # 3
            return AddableBingoCage(self.inspect() + other.inspect())   # 4
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()    # 5
        else:
            try:
                other_iterable = iter(other)
            except TypeError:   # 6
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)   # 7
        return self