import pandas as pd
from pandas.api.types import CategoricalDtype
import openpyxl

# 读取投诉分析表
file_path = './投诉分析表202011汇总.xlsx'
data = pd.read_excel(file_path)

# 按照地市统计投诉数量
city = pd.Series(data.loc[:, '本地网'].value_counts(), name='个数')
proportion = pd.Series(city/city.sum(), name='比例')
out = pd.concat([city, proportion], axis=1)
print(out)
print('～～～～上面是原始统计～～～下面是归并其他～～～～')
# 设置缺省index：全部地市+其他
arr_default = ['杭州', '宁波', '温州', '金华', '嘉兴', '绍兴', '衢州', '湖州', '台州', '丽水', '舟山', '其他']
out.loc['其他'] = 0
# 不在指定范围的数量累计到其他，如外省投诉
for x in proportion.index:
    if x not in arr_default:
        out.loc['其他'] += out.loc[x]
out = pd.DataFrame(out, index=arr_default).fillna(0)
out['个数'] = out['个数'].astype('int32')
out['比例'] = out['比例'].apply(lambda x: format(x, '.2%'))
print(out)

# 自定义排序
# custom_order = CategoricalDtype(['杭州', '宁波', '温州', '金华', '嘉兴', '绍兴', '衢州', '湖州', '台州', '丽水', '舟山', '其他'], ordered=True)
# out.index = out.index.astype(custom_order)
# final = out.sort_index()
final = out

# 输出到csv
# final.to_csv('./out1.csv')

# 输出到excel 1、创建文件用于接收数据 2、dataFrame输出到excel
outwb = openpyxl.Workbook()
outsheet = outwb.create_sheet(index=0)
save_path = './out.xlsx'
outwb.save(save_path)
final.to_excel(save_path, 'Sheet1')


