#coding=utf-8

from array import array
import math


class Vector2d:
    typecode = 'd'  # 1

    def __init__(self, x, y):
        self.x = float(x)   # 2
        self.y = float(y)

    def __iter__(self):     # 3
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)   # 4

    def __str__(self):  # 5
        return str(tuple(self))

    def __bytes__(self):    # 6 7
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):    # 8
        return tuple(self) == tuple(other)

    def __abs__(self):  # 9
        return math.hypot(self.x, self.y)

    def __bool__(self): # 10
        return bool(abs(self))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)


if __name__ == '__main__':
    print(format(Vector2d(1, 1), 'p'))
    print(format(Vector2d(1, 1), '.3ep'))
    print(format(Vector2d(1, 1), '.5fp'))