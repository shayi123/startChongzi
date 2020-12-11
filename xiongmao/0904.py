import pandas as pd
import numpy as np

dates2 = pd.date_range('20200901', periods=4)
df2 = pd.DataFrame({'A': 1.,
                    'B': dates2,
                    'C': pd.Series([1, 2, 3, 4]),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
# print(df2.index)
# print(df2.columns)
# print('#######')
# print(df2.dtypes)

df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                   "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
print('##### the original df #####')
print(df)
df['grade'] = df['raw_grade'].astype('category')
print('#### df-grade raw #####')
print(df['grade'])
df['grade'].cat.categories = ["very good", "good", "very bad"]  # 设置级别，三个级别，然后实际value（a，b，e）分别对应一个级别，详见下一行打印结果
print('#### df-grade three level #####')
print(df['grade'])
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium",
                                              "good", "very good"])
print('#### df-grade five level #####')
print(df['grade'])
print('##### df with category type #######')
print(df)
df['raw_grade'] = ['a', 'b', 'c', 'd', 'e', 'a']
# ？？？？？？？？？如何可以让raw_grade和grade联动
print('#### change df raw_grade #######')
print(df)

