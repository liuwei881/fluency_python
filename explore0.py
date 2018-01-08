#coding=utf-8

from collections import abc
import keyword
   

class FrozenJSON:
    """
    一个只读接口, 使用属性表示法访问JSON类对象
    """
    # def __init__(self, mapping):
    #     self.__data = dict(mapping) # 1
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):  # 1
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):    # 2
        if hasattr(self.__data, name):
            return getattr(self.__data, name)   # 3
        else:
            return FrozenJSON.build(self.__data[name])  # 4

    @classmethod
    def build(cls, obj):    # 5
        if isinstance(obj, abc.Mapping):    # 6
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):  # 7
            return [cls.build(item) for item in obj]
        else:   # 8
            return obj