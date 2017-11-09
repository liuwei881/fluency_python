#coding=utf-8


class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    bus1 = HauntedBus(['Alice', 'Bill'])
    print(bus1.passengers)  #1
    bus1.pick('Charlie')
    bus1.drop('Alice')
    print(bus1.passengers)
    bus2 = HauntedBus() #2
    bus2.pick('Carrie')
    print(bus2.passengers)
    bus3 = HauntedBus() #3
    print(bus3.passengers)  #4
    bus3.pick('Dave')
    print(bus2.passengers)  #5
    print(bus2.passengers is bus3.passengers)   #6
    print(bus1.passengers)  #7
