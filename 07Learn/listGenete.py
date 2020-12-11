# 一 列表生成式
# 二 一边循环一边计算的机制，称为生成器：generator
import os
# [exp for val in collection if condition]
print(list(range(1, 11)))
l1 = [x * x for x in range(4)]
print(l1)
l2 = [x * x for x in range(4) if x % 2 != 0]
print(l2)
# 生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir('..')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)
print([s.lower() for s in ['ABdfEW', 'asdQWEFDde', 'djiDEe']])
# [exp for val in collection if condition] if在for后面作为筛选条件
L = ['Hello', 10, 'World', None]
print([s.lower() for s in L if isinstance(s, str)])

print('# if放在for前面是表达式，必须有else，才能对所有情况应用生成式')
print([x if x % 2 == 0 else -x for x in range(1, 10)])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

print('二 一边循环一边计算的机制，称为生成器：generator。')
# 列表生成式 List L ; generator g;
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(L)
print('next()可以用到list上吗?', 'list object is not an iterator')
# next(L)
print(g)
for nn in g:
    print(nn)

# 打印斐波那契额数列
# generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，
# 遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。


def fib(max):
    print('fib list:')
    cnt, a, b = 0, 0, 1
    while cnt < max:
        # 在循环过程中不断调用yield，就会不断中断
        yield b
        a, b = b, a+b
        cnt = cnt+1
    return 'done'


if __name__ == '__main__':
    # print(fib(6))
    # fib 是生成器 generator，所以"fib(6)"不会打印出数列
    # 而是"<generator object fib at 0x1023c6360>"
    # 即普通函数调用直接返回结果；generator函数的“调用”实际返回一个generator对象
    g = fib(6)
    # print('print each num')
    # for n in g:
    #      print(n)
    print('print return value')
    i = 0
# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
    while True:
        try:
            # print('fib:', next(g))
            i = i+1
            print('fib', i, ':', next(g))  # 或者for循环打印，必须捕获StopIteration错误
        except StopIteration as e:
            # 为什么没有打印出'done'
            print('Generator return value:', e.value)
            break
