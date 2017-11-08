#coding=utf-8

from operator import mul
from functools import partial

triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(1, 10))))