import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ss = pd.read_csv('/Users/shelly/Desktop/ss.csv')
sc = pd.read_csv('/Users/shelly/Desktop/sc.csv')

# print(ss.head())
compare = pd.merge(ss, sc, on=['skuID'])
compare['diff'] = compare['totalCount-ss']-compare['totalCount-sc']
print(compare.head())




