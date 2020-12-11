import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                   index=[2, 3, 6, 7])

print(pd.concat([df1, df4], axis=1, sort=False))
print('*******************')
print(pd.concat([df1, df4], sort=False))
print('*******************')
print(pd.concat([df1, df4], axis=1, sort=False, join='inner'))
print('*******************')
print(df1.append(df4, sort=False))

# Reshaping
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print('#######?????????#############')
print(df)
rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts)
print('@@@@@@@@@@@@@@@@@')
print(ts.resample('5Min'))

rng1 = pd.date_range('1/1/2012', periods=5, freq='M')
print(rng1)
ts1 = pd.Series(np.random.randn(len(rng1)), index=rng1)
print(ts1)
ps = ts1.to_period()
# Convert Series from DatetimeIndex to PeriodIndex with desired frequency (inferred from index if not passed)
print(ps)
ps.to_timestamp()
