import functools

# 偏函数实际上是利用了可变参数和关键字参数：*args, **kw
int2 = functools.partial(int, base=2)
print(int2('1010'))
print(int2('1010', base=10))

# 最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
int2 = functools.partial(int, base=2)
# 也就是 kw = { 'base': 2 }
# int('10010', **kw)
max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，相当于
# args = (10, 5, 6, 7)
# max(*args)