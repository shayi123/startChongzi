class Student(object):
    # 属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）
    def __init__(self, name, score):
        self.__name = name
        self.score = score

    # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
    # 并且，调用时，不用传递该参数
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def print_score(self):
        print('%s: %s' % (self.__name, self.score))


stu1 = Student('Bart Simpson', 59)

print(stu1)
print(Student)
# print(stu1.__name) 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name
print(stu1.get_name())
print(stu1.score)
# print(Student.name) # AttributeError: type object 'Student' has no attribute 'name'
# print(stu1.self)  # AttributeError: 'Student' object has no attribute 'self'
# python最强大的是可以动态增加实例的属性 eg：
stu1.sex = 'girl'
print('new attribute: ', stu1.sex)

# 在Python中，实例的变量名如果以两个下划线__开头，就变成了一个私有变量（private）