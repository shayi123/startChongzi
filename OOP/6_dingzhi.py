class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object name : %s' % self.name

    __repr__ = __str__


print(Student('Shelly'))
s = Student('Shelly')
print(s)

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

ss = Chain('hello').status.kaola.first
print(ss)

# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000
# 其他例子，可以定制迭代器等 __iter__、__getitem__