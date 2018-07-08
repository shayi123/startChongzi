# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
# 返回的函数并没有立刻执行，直到调用它才执行
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)被调用，立刻被执行，因此i的当前值被传入f()
    return fs


func1, func2, func3 = count()
print(func1, func2, func3)
print(func1(), func2(), func3())


#错误示范
def count_false():
    fs = []
    for i in range(1, 4):
        def f():
            print('run inner_f()')
            return i*i  # 每次执行到这里就return，但是func1等被调用时才执行。局部变量i已经变化了
        print('out of inner_f()')
        fs.append(f)
    return fs


func1, func2, func3 = count_false()
print(func1, func2, func3)
print(func1(), func2(), func3())