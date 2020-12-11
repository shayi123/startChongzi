# normalize name


def normalize(name):
    return name.capitalize()


if __name__ == '__main__':
    print('A'.lower())
    print('A'.lower)
    ss = normalize('asD')
    print(ss)
    L1 = ['AdmIn', 'anny', 'LUCY', 'sandY', 'wILl']
    L2 = list(map(normalize, L1))
    print(L2)
    print(L2[0][0].lower())
    print(L2[0][0])
    # 错误示范 'str' object does not support item assignment ：L2[0][0] = L2[0][0].lower()
    L2[0] = L2[0][0].lower() + L2[0][1:]
    print(L2[0])
