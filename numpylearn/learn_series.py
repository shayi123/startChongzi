import pandas as pd
import numpy as np

s = pd.Series([-1.10, 2, -3.33, 4])
# 索引
print(s[[1, 3, 2]])
# 切片
print(s[1:3])
print(s.index)
print(s.values)
print(s)
print(type(s.values))

df1 = pd.DataFrame({'float': [1.0],
                    'int': [1],
                    'datetime': [pd.Timestamp('20180310')],
                    'string': ['foo']})
int_values = [1, 2, 3, 4, 5]
text_values = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
float_values = [0.0, 0.25, 0.5, 0.75, 1.0]
df2 = pd.DataFrame({"int_col": int_values, "text_col": text_values,
                    "float_col": float_values})
print(df1)
print(df2)
# 行索引
print(df1.index)
# 列索引
print(df1.columns)
# 数据维度
print(df2.ndim)
# 列数据类型
print(df2.dtypes)
# df形状
print(df2.shape)
df3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("WXYZ"))
print('@@@@@@@@@@@@@###############$$$$$$$$$$')
print(df3)
print(df3["W", "X"])
# loc取列
print(df3.loc[:, "W"])
# 错误的 print(df3[:, "X"])
# 错误的 print(df3["a"])
# loc取行
print(df3.loc['a'])
print(df3.loc['b':'c'])
print(df3.loc[['a', 'c']])

w = df3['W'].values
print(type(w))
print(type(df3['W']))
print(w.max()//3)
df3['Q'] = df3['W'] + df3['X']
print(df3)
print('@@@@@@@@@')
df3.rename({'a': 'rr'}, inplace=True)
print(df3)