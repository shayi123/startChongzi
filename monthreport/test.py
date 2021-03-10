import pandas as pd
import numpy as np

writer = pd.ExcelWriter('C:/Users/shelly/Desktop/周报数据源/xx周.xlsx')
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 23, 45]]))

# print(df2)
df2.index = df2.loc[:, 2]
# print(df2)

x = ['杭州分公司', '宁波分公司', '温州分公司', '金华分公司', '嘉兴分公司', '绍兴分公司', '衢州分公司', '湖州分公司', '台州分公司', '丽水分公司', '舟山分公司']
# list[start:end:step] '##分公司'变为'##'
print(x[0][-4::-1])
