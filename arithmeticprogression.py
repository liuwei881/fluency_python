#coding=utf-8


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):  # 1
        self.begin = begin
        self.step = step
        self.end = end  # None -> 无穷数列

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)   # 2
        forever = self.end is None  # 3
        index = 0
        while forever or result < self.end:     # 4
            yield result    # 5
            index += 1
            result = self.begin + self.step * index     # 6