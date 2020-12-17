import pandas as pd
from pandas.api.types import CategoricalDtype
import openpyxl

data2 = pd.read_excel('/Users/shelly/PycharmProjects/startChongzi/numpylearn/sales1.xlsx')
# print(data2.describe())
pay_methods = pd.Series(data2.loc[:, '支付方式'].value_counts(), name='个数')
print(pay_methods)
# apply(lambda x: format(x, '.2%'))
proportion = pd.Series((pay_methods/pay_methods.sum()), name='比例')
print(proportion)
out = pd.concat([pay_methods, proportion], axis=1)
# 设置缺省index：全部地市+其他
arr_default = ['现金', '支付宝付款码', '微信付款码', '支付宝扫一扫', '其他']
out.loc['其他'] = 0
# 不在指定范围的数量累计到其他，如外省投诉
for x in proportion.index:
    if x not in arr_default:
        out.loc['其他'] += out.loc[x]
out = pd.DataFrame(out, index=arr_default).fillna(0)
out['个数'] = out['个数'].astype('int32')
out['比例'] = out['比例'].apply(lambda x: format(x, '.2%'))
print(out)
# df[np.logical_and(df['one']> 5,df['two']>5)] 或者 df[(df['one']> 5) & (df['two']>5)]
# 第一步多列筛选；第二步指定列进行字符频率统计
selection = data2.loc[(data2['支付方式'].isin(['支付宝付款码', '微信付款码'])) & (data2['一级类目'].isin(['环球美食', '个人洗护', '美容彩妆']))]. \
                loc[:, '一级类目'].value_counts()
print(selection)
# 指定多列统计字符频率
selection2 = data2.loc[:, ['支付方式', '一级类目']].value_counts()
selection2.name = '订单数'
print(selection2)
# series生成DataFrame
multicolumn = pd.DataFrame(selection2)
print(multicolumn)

# 输出到csv
# multicolumn.to_csv('./multi.csv')

# 自定义排序
custom_order = CategoricalDtype(['现金', '支付宝付款码', '微信付款码', '支付宝扫一扫', '其他'], ordered=True)
out.index = out.index.astype(custom_order)
final = out.sort_index()
# print(final)
# 输出到excel
# 1、创建文件用于接收数据
# 2、dataFrame输出到excel
outwb = openpyxl.Workbook()
outsheet = outwb.create_sheet(index=0)
save_path = '/Users/shelly/PycharmProjects/startChongzi/numpylearn/out.xlsx'
outwb.save(save_path)
# selection2.to_excel(save_path, 'Sheet1')

