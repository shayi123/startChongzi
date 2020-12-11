import pandas as pd
import numpy as np

# df1 = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range('1/1/2000', periods=1000), columns=['A', 'B', 'C', 'D'])
# df1.to_csv('test1.csv')
print(pd.read_csv('test1.csv', parse_dates=['Date']))  # ????parse_dates : bool???
