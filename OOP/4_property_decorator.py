# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢
# Python内置的@property装饰器就是负责把一个方法变成属性调用的.
# 可以让调用者写出简短的代码，同时保证对参数进行必要的检查
# class Student(object):
#
#     def get_score(self):
#          return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value


class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，
# 负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
# 只定义getter方法，不定义setter方法就是一个只读属性：
class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value