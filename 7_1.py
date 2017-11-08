#coding=utf-8


def deco(func):
    def inner():
        print('running inner()')
    return inner


if __name__ == '__main__':
    @deco
    def target():
        print('running target()')
    target()
    print(target)