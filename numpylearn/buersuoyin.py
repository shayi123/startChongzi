import numpy as np

a = np.arange(12).reshape(3,4)
b1 = np.array([False,True,True])
b2 = np.array([True,False,True,False])
# print(a)
# print(a[b1, :])
# print(a[:, b2])
# print(a[b1, b2])

arr2 = np.arange(32).reshape((8, 4))
# 选取指定区域
print(arr2)
print(arr2[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
# 使用ix_()函数实现，笛卡尔积获取索引位置
# np.ix_函数就是输入数组，产生笛卡尔积的映射关系
print(arr2[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])

# 3 维
a = np.array([2, 3, 4, 5])
b = np.array([8, 5, 4])
c = np.array([5, 4, 6, 8, 3])
ax, bx, cx = np.ix_(a, b, c)
print('aaaa')
print(a)
print('axaxaxax')
print(ax)
print(a.shape)
print(ax.shape)
print(np.ix_(a, b, c))
print(np.ix_([1, 5, 7, 2], [0, 3, 1, 2]))
