# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
import functools


# 观察下面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。仅接收一个参数吗？？
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 相当于now = log(now)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
# 只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
@log
def now():
    print('2018-07-14')


# 需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# @functools.wraps(func) 的作用就类似于'wrapper.__name__ = func.__name__'
print(now.__name__)
print(now())
print(log(now))