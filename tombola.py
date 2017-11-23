#coding=utf-8

import abc


class Tombola(abc.ABC):     # 1
    @abc.abstractmethod
    def load(self, iterable):   # 2
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):     # 3
        """随机删除元素,然后将其反回
        如果实例为空,这个方法应该抛出`LookupError`
        """

    def loaded(self):   # 4
        """如果至少有一个元素, 返回`True`,否则返回`False`"""
        return bool(self.inspect())     # 5

    def inspect(self):
        """返回一个有序元组, 由当前元素构成"""
        items = []
        while True:     # 6
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)    # 7
        return tuple(sorted(items))