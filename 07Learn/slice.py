# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：


def trim(s):
    # for (i, j) in zip(range(len(s)), range(len(s)-1, -1, -1)):
    if s == '':
        return s
    for i in range(len(s)):
        if s[i] != ' ':
            break    # 不等于空格时，break，跳出循环，得到第一个非空格的位置i
    # range(start, stop, step)
    for j in range(len(s)-1, -1, -1):
        if s[j] != ' ':
            break    # 不等于空格时，break，跳出循环，得到最后一个非空格的位置j
    # 切片：前包后不包
    ss = s[i: j+1]
    return ss


if __name__ == "__main__":
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')
