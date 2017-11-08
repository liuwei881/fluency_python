#coding=utf-8


class Poem(object):
    """In Python returning `self` in the instance method
    is one way to implement the fluent pattern.
    """
    def __init__(self, content):
        self.content = content

    def indent(self, spaces):
        self.content = " " * spaces + self.content
        return self

    def suffix(self, content):
        self.content = self.content + " - " + content
        return self


if __name__ == '__main__':
    a = Poem("test").indent(4).suffix('zouni').content
    print(a)