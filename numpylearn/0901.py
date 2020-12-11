import numpy as np

np.arange(2, 4, 0.3)
# 使用索引数组进行索引
a = np.arange(12)**2  # the first 12 square numbers
i = np.array([1, 1, 2, 4])
print(a[i])  # the elements of a at the positions i
j = np.array([[1, 2], [3, 4]])  # a bidimensional array of indices
print(a[j])  # the same shape as j

b = np.arange(12).reshape(3, 4)  # 多维矩阵
print(b)
i = np.array([[1, 2], [0, 0]])
j = np.array([[2, 1], [2, 2]])
ll = [i, j]
print(b[i, j])
print(b[ll])
print(b[:, j])

c = np.arange(5)
d = np.arange(5)
print(c)
c[[0, 0, 2]] = [1, 2, 3]  # 索引列表包含重复值时，也是按照顺序分配就行
d[[0, 0, 2]] += 1  # ???? 为什么d[0]不是2,因为不是叠加，是覆盖：相当于d[0]+1,d[0]+1,d[2]+1
print(d)




