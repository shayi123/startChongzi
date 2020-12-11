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
# print(func1, func2, func3)
print(func2())