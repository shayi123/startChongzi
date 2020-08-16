# 今天开始学习数据分析，从numpy和pandas学起

# 读取文件
import numpy as np
import pandas as pd

data = np.genfromtxt('/Users/shelly/PycharmProjects/startChongzi/ExcelData/sales.csv', dtype=float, delimiter=',', skip_header=1, usecols=7, encoding='utf-8')
print(data.size)
