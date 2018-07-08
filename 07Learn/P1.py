from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
'''
字符串转为int数字，先不考虑溢出和负数
'''


def str2int(ss):
    # 传入reduce的函数
    def fn(x, y):
        return x * 10 + y

    # 传入map的函数
    def char2num(s):
        # 注意取字典内容用[]而不是()
        return DIGITS[s]

    # return reduce(fn, map(char2num, ss))
    # 简化写法，抽象fn
    return reduce(lambda x, y: x * 10 + y, map(char2num, ss))


if __name__ == '__main__':
    print(str2int('12890'))



