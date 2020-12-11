import numpy as np
import pandas as pd

# 用值列表生成 Series 时，Pandas 默认自动生成整数索引：
s = pd.Series([1, 3, np.nan, 4])
print(s)
# 用含日期时间索引与标签的 NumPy 数组生成 DataFrame：
dates = pd.date_range('20130101', periods=6)
dates2 = pd.date_range('20200901', periods=4)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
print('### Only Column A ####')
print(df['A'])
#  Excludes NA values by default.
df['A'].value_counts(ascending=True)

df2 = pd.DataFrame({'A': 1.,
                    'B': dates2,
                    'C': pd.Series([1, 2, 3, 4]),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
print(df2.dtypes)
print(df2.head(1))
print(df2.tail(2))
print(df2.index)  # 'C': pd.Series(1, index=list(range(4)), dtype='float32'),看看index的区别
print(df2.columns)
print(df2.describe())
print(df2.T)
print(df['A'])
print(df2['F'])
print(df2['B'])

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)
print(df1.index)
print(df1.columns)
print(df1.dropna(how='any'))
print(df1)
print(df1.fillna(value=6))
print(df1)
df3 = df.reindex(index=dates[0:2])
print('df3df3df3df3')
print(df3)
print(df1)
print(pd.isna(df1))
print(df1.mean())
print(df1.mean(1))
print(df1.mean)  # 获取方法签名
# 不同维度对象运算时，要先对齐。 此外，Pandas 自动沿指定维度广播。
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)  # shift表示移动
print(df)
print(s)
print(df.sub(s, axis='index'))
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower()  # 为什么没有推荐lower函数呢？？


