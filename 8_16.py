#coding=utf-8

import weakref


s1 = {1, 2, 3}
s2 = s1 #1


def bye():  #2
    print('Gone with the wind...')


ender = weakref.finalize(s1, bye)   #3
print(ender.alive)  #4
del s1  #5
print(ender.alive)
s2 = 'spam'
print(ender.alive)
