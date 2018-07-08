from collections import Iterable


print(isinstance('1ber', Iterable))

list1 = ['q', 5, 3, '3r']
for x in list1:
    print(x)

for i, value in enumerate(list1):
    print(i, value)

for x, y, z in [(1, 'w', 'ww'), (2, 'q', 'qq'), (3, 'e', 'ee')]:
    print(x, y, z)

