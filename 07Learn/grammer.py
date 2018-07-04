list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[0:3])
print(list1[:3])
print(list1[-5:-2])
print(list1[-3:])
print(list1[-3:0])
print(list1[-3:-1])
print(list1[3:8:2])
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):

