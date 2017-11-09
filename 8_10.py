#coding=utf-8

a = [10, 20]
b = [a, 30]
a.append(b)
print(a)

from copy import deepcopy, copy
c = deepcopy(a)
d = copy(a)
print(c)
print(d)