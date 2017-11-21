#coding=utf-8

from operator import itemgetter, attrgetter


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(student_objects, key=attrgetter('age')))
print(sorted(student_tuples, key=itemgetter(1, 2)))
print(sorted(student_objects, key=attrgetter('age')))