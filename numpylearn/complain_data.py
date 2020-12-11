import pandas as pd
from pandas.api.types import CategoricalDtype
import openpyxl

data2 = pd.read_excel('/Users/shelly/PycharmProjects/startChongzi/numpylearn/sales.xlsx')
pay_methods = pd.Series(data2.loc[:, '支付方式'].value_counts(), name='个数')
print(pay_methods)
proportion = pd.Series((pay_methods/pay_methods.sum()).apply(lambda x: format(x, '.2%')), name='比例')
print(proportion)
# 设置缺省值
out = pd.concat([pay_methods, proportion], axis=1)
out = pd.DataFrame(out, index=['现金', '支付宝付款码', '微信付款码', '支付宝扫一扫']).fillna(0)
out['个数'] = out['个数'].astype('int32')
print(out)
# df[np.logical_and(df['one']> 5,df['two']>5)] 或者 df[(df['one']> 5) & (df['two']>5)]
# 第一步多列筛选；第二步指定列进行字符频率统计
selection = data2.loc[(data2['支付方式'].isin(['支付宝付款码', '微信付款码'])) & (data2['一级类目'].isin(['环球美食', '个人洗护', '美容彩妆']))]. \
                loc[:, '一级类目'].value_counts()
print(selection)

# 自定义排序
custom_order = CategoricalDtype(['现金', '支付宝付款码', '微信付款码', '支付宝扫一扫'], ordered=True)
out.index = out.index.astype(custom_order)
final = out.sort_index()

# 输出到excel
# 1、创建文件用于接收数据
# 2、dataFrame输出到excel
outwb = openpyxl.Workbook()
outsheet = outwb.create_sheet(index=0)
save_path = '/Users/shelly/PycharmProjects/startChongzi/numpylearn/out.xlsx'
outwb.save(save_path)
final.to_excel(save_path, 'Sheet1')

