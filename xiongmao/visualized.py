import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
# ts.plot()
# plt.show()
# print(ts.index)
df1 = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df1 = df1.cumsum()
plt.figure()
df1.plot()
plt.legend(loc='best')
plt.show()
