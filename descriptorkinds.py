#coding=utf-8


class Overriding:   # 1
    """也称数据描述符或强制描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)    # 2

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:  # 3
    """没有``__get__``方法的覆盖型描述符"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:    # 4
    """也称非数据描述符或遮盖型描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:  # 5
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self): # 6
        print('-> Managed.spam({})'.format(display(self)))
