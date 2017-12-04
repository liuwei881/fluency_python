#coding=utf-8

from array import array
import reprlib
import math
import functools
import operator
import itertools
import numbers


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    # 详见https://github.com/fluentpython/example-code

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    def __matmul__(self, other):
        try:
            return sum(a * b for a, b in zip(self, other))
        except TypeError:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other

    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self) == len(other)) and all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented
