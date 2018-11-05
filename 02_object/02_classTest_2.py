# -*- coding: utf-8 -*-
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


bart = Student('Bart Simpson', 59)


bart.print_score()

print(bart._Student__name)
#外部代码给bart新增了一个__name变量
bart.__name = 'newName'
print(bart.__name)

print(bart.get_name())

# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。