import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
import openpyxl
from monthreport.rank_by_city import RankByCity
from month_report import MonthReport

file_guzhang = 'E:/投诉分析/202101/移动信号直派单20210222-0228.xlsx'
file_out = 'guzhang_reason.xlsx'

writer = pd.ExcelWriter(file_out)

guzhang_info = pd.read_excel(file_guzhang, '详单')
df_guzhang = guzhang_info[['本地网', '工单是否超时', '归档原因']]
# df_intime = pd.pivot_table(df_guzhang, index=['本地网'], columns=['工单是否超时'])
# print(df_intime)
ll = pd.crosstab(df_guzhang['本地网'], df_guzhang['归档原因'], margins=True, margins_name='全省', normalize='index')
ll = ll.applymap(lambda x: format(x, '.2%'))
print(ll)
# print(df_guzhang)
series_ontime = df_guzhang.groupby('本地网')['工单是否超时'].value_counts()
series_reason = df_guzhang.groupby('本地网')['归档原因'].value_counts()
series_ontime.name = None
series_reason.name = None
so = series_ontime.reset_index(name='单量')
# print(so)
so = pd.pivot_table(so, values='单量', index=['本地网'], columns=['工单是否超时'], aggfunc=np.sum, fill_value=0,
                    margins=True, margins_name='全省')
so['工单及时率'] = (so['否']/so['全省']).apply(lambda x: format(x, '.2%'))
# print(so)
so.to_excel(writer, sheet_name='sheet1')
# 原因
sr = series_reason.reset_index(name='单量')
# sr = pd.pivot_table(sr, values='单量', index=['本地网'], columns=['归档原因'], aggfunc=np.sum, fill_value=0,
                    # margins=True, margins_name='总计')
# sr = pd.crosstab(index=sr['本地网'], columns=sr['归档原因'], values=sr['单量'], margins=True, aggfunc=np.sum, margins_name='总计', normalize='index')
# sr = pd.crosstab(sr['本地网'], sr['归档原因'], values=sr['单量'], aggfunc=np.sum, margins=True, normalize='index')
# print(sr)
# print(type(sr))
ll.to_excel(writer, sheet_name='sheet2')
writer.save()


