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

# data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
# print(sorted(data, key=itemgetter(0)))
#
# s = sorted(student_objects, key=attrgetter('age'))
# print(sorted(s, key=attrgetter('grade'), reverse=True))

# decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
# decorated.sort()
# # print(decorated)
# print([student for grade, i, student in decorated])

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
standard_way = sorted(data, key=itemgetter(0), reverse=True)
double_reversed = list(reversed(sorted(reversed(data), key=itemgetter(0))))
assert standard_way == double_reversed
print(standard_way)

