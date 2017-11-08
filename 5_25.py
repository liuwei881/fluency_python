#coding=utf-8

from operator import methodcaller

s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))
hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))