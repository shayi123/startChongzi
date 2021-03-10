import pandas as pd
import numpy as np

a = [['a', '1.2', '4.2'], ['b', '70', '0.03'], ['x', '5', '0']]
df = pd.DataFrame(a, columns=['col1', 'col2', 'col3'])
print(df)
print(df.dtypes)
df = df.apply(pd.to_numeric, errors='ignore')
print(type(df.loc[0, 'col1']))
print(type('a') == "<class 'str'>")
for col in df.columns:
    df[col] = df[col].map(lambda x: x if type(x) == type('a') else int(x))

print('~~~~')
print(df)
print(df[:])
