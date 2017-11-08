#coding=utf-8


class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager


if __name__ == '__main__':
    # avg = Averager()
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg(13))