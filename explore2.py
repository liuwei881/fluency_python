#coding=utf-8

from collections import abc
import keyword


class FrozenJSON:
    """
    一个只读接口,使用属性表示法访问JSON类对象
    """
    def __new__(cls, arg):  # 1
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls) # 2
        elif isinstance(arg, abc.MutableSequence):  # 3
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])  # 4