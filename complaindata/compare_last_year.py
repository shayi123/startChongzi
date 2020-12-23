import pandas as pd
from pandas.api.types import CategoricalDtype
import openpyxl

file_zixun_this_year = 'E:/投诉分析/202011/咨询投诉清单宽表202011.xlsx'
file_guzhang_this_year = 'E:/投诉分析/202011/移动信号直派单202011.xlsx'

zixun_this_year = pd.read_excel(file_zixun_this_year)
guzhang_this_year = pd.read_excel(file_guzhang_this_year, sheet_name='详单')
# print(guzhang_this_year.head())
zixun_city = pd.Series(zixun_this_year.loc[:, '地市'].value_counts(), name='投诉单')
guzhang_city = pd.Series(guzhang_this_year.loc[:, '本地网'].value_counts(), name='故障单')
guzhang_city.index = list(map(lambda x: x[-4::-1][::-1], guzhang_city.index))
# print(zixun_city)
# print(guzhang_city)
this_year = pd.concat([guzhang_city, zixun_city], axis=1)
print(this_year)
last_year = this_year
combine = pd.concat([this_year, last_year], keys=['2020', '2019'], axis=1)
print(combine)

# 输出到excel 1、创建文件用于接收数据 2、dataFrame输出到excel
outwb = openpyxl.Workbook()
outsheet = outwb.create_sheet(index=0)
save_path = './out2.xlsx'
outwb.save(save_path)
combine.to_excel(save_path, 'Sheet1')
