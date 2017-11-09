#coding=utf-8


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


if __name__ == '__main__':
    import weakref
    stock = weakref.WeakValueDictionary()   # 1
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
               Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese.kind] = cheese # 2
    print(sorted(stock.keys())) # 3
    del catalog
    print(sorted(stock.keys())) # 4
    print(cheese)
    del cheese  # 全局变量要主动删除，否则不会删除, 指是弱引用
    print(sorted(stock.keys()))