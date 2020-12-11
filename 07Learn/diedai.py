from collections import Iterable, Iterator

print('可以直接作用于for循环的对象统称为可迭代对象：Iterable')
print(isinstance('1ber', Iterable))

print('可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator')
print(isinstance((x for x in range(10)), Iterator))
print('生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。把list、dict、str等Iterable变成Iterator可以使用iter()函数：')
print(isinstance(iter('aaa'), Iterator))
print(isinstance('aaa', Iterator))
list1 = ['q', 5, 3, '3r']
for x in list1:
    print(x)

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(list1):
    print(i, value)

for x, y, z in [(1, 'w', 'ww'), (2, 'q', 'qq'), (3, 'e', 'ee')]:
    print(x, y, z)

print('dict迭代')
d = {1: 'a', 2: 'b', 3: 'c'}

for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print('key: ')
    print(k)
    print(' value: ' + v)
