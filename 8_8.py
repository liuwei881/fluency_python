#coding=utf-8


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.apppend(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    import copy
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3)) #1
    bus1.drop('Bill')
    print(bus2.passengers)  #2
    print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))    #3
    print(bus3.passengers)  #4