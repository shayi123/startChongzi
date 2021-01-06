import pandas as pd
from pandas.api.types import CategoricalDtype
import openpyxl

file_zixun_this_year = 'E:/投诉分析/202011/咨询投诉清单宽表202011.xlsx'
file_guzhang_this_year = 'E:/投诉分析/202011/移动信号直派单202011.xlsx'
file_zixun_last_year = 'E:/投诉分析/202011/咨询投诉工单清单201911total.xlsx'
file_guzhang_last_year = 'E:/投诉分析/202011/移动信号用户障碍单报表201911.xlsx'

# this year
zixun_this_year = pd.read_excel(file_zixun_this_year)
guzhang_this_year = pd.read_excel(file_guzhang_this_year, sheet_name='详单')
zixun_city = pd.Series(zixun_this_year.loc[:, '地市'].value_counts(), name='投诉单')
guzhang_city = pd.Series(guzhang_this_year.loc[:, '本地网'].value_counts(), name='故障单')
guzhang_city.index = list(map(lambda x: x[-4::-1][::-1], guzhang_city.index))
this_year = pd.concat([guzhang_city, zixun_city], axis=1)
print(this_year)

# last year
zixun_last_year = pd.read_excel(file_zixun_last_year)
guzhang_last_year = pd.read_excel(file_guzhang_last_year, sheet_name='详单')
zixun_city_0 = pd.Series(zixun_last_year.loc[:, '地市'].value_counts(), name='投诉单')
guzhang_city_0 = pd.Series(guzhang_last_year.loc[:, '本地网'].value_counts(), name='故障单')
guzhang_city_0.index = list(map(lambda x: x[-4::-1][::-1], guzhang_city_0.index))
last_year = pd.concat([guzhang_city_0, zixun_city_0], axis=1)
print(last_year)

# combine
combine = pd.concat([last_year, this_year], keys=['2019', '2020'], axis=1)

# compare
combine['涨幅（单量）'] = (combine.iloc[:, 2] + combine.iloc[:, 3]) - (combine.iloc[:, 0] + combine.iloc[:, 1])
combine['涨幅（比例）'] = (combine['涨幅（单量）']/(combine.iloc[:, 0] + combine.iloc[:, 1])).apply(lambda x: format(x, '.2%'))
print(combine)

# 输出到excel 1、创建文件用于接收数据 2、dataFrame输出到excel
outwb = openpyxl.Workbook()
outsheet = outwb.create_sheet(index=0)
save_path = './out2.xlsx'
outwb.save(save_path)
combine.to_excel(save_path, 'Sheet1')
