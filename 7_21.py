#coding=utf-8

from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch #1
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)  #2
def _(text):    #3
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral) #4 numbers.Integral是int的虚拟超类(抽象基类)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)    #5
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


if __name__ == '__main__':
    print(htmlize({3, 2, 1}))
    print(htmlize(abs))
    print(htmlize('Heimlich & Co.\n- game'))
    print(htmlize(42))
    print(htmlize(['alpha', 66, {3, 2, 1}]))

