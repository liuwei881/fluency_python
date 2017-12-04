#coding=utf-8

# abc.Iterator源码
# 摘自Lib/_collections_abc.py(https://hg.python.org/cpython/file/3.4/Lib/_collections_abc.py#193)


class Iterator(Iterable):
    __slots__ = ()

    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            if (any("__next__" in B.__dict__ for B in C.__mro__) and
                    any("__iter__" in B.__dict__ for B in C.__mro__)):
                return True
            return NotImplemented