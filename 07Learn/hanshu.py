from functools import reduce


def gaojie(a, b, f):
    return f(a) + f(b)


def sophistic(x):
    return x * x


def add(a, b):
    return a + b


def is_odd(n):
    return n % 2 == 1

'''
and逻辑运算符
'''
def not_empty(s):
    return s and s.strip()


if __name__ == '__main__':
    print('高阶函数')
    zhihe = gaojie(2, -4, abs)
    print(zhihe)
    print('一种高阶函数--map,接收一个函数和一个序列:map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回')
    r = map(sophistic, [1, 2, 3, 4, 5])
    print(r)
    print(list(r))
    print('一种高阶函数--reduce：类似于递归：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)')
    print('因此，传入reduce的函数必须接受两个参数')
    p = reduce(add, [1, 2, 3, 4])
    print(p)
    print(sum([1, 2, 3, 4]))
    print('map reduce 联合应用--请看P1.python')
    print('filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素')
    print('由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素')
    print(list(filter(is_odd, [1, 3, 3, 4, 6, 5, 4])))
    print(list(filter(not_empty, ['a', ' ', '', None, 'b', 'c'])))
    print('一种高阶函数sorted：按照制定规则对序列排序')
    print(sorted([36, 5, -12, 9, -21], key=abs))
    print('忽略大小写，且降序')
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
    print('字典的排序见P2.python')
