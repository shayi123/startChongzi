import pandas as pd
from pandas.api.types import CategoricalDtype
import openpyxl


class MonthReport(object):
    def __init__(self, one_month):
        self.one_month = one_month

    # 排序
    def rank(self, out, city):
        arr_default = ['杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '丽水', '台州', '舟山', '其他']
        out.loc['其他'] = 0
        # 不在指定范围的数量累计到其他，如外省投诉
        for x in city.index:
            if x not in arr_default:
                out.loc['其他'] += out.loc[x]
        out = pd.DataFrame(out, index=arr_default).fillna(0)
        return out

    def calculate_guzhang(self, key, sheet_name):
        data = pd.read_excel(self.one_month, sheet_name)
        city = pd.Series(data.loc[:, key].value_counts(), name='故障单')
        # index格式统一
        city.index = list(map(lambda x: x[-4::-1][::-1], city.index))
        out = pd.DataFrame(city)
        out = self.rank(out, city)
        out['故障单'] = out['故障单'].astype('int32')
        total = sum(out.iloc[:, 0])
        out.loc['全省'] = [total]
        return out

    def __calculate__(self, key, sheet_name):
        data = pd.read_excel(self.one_month, sheet_name)

        # 按照地市统计投诉数量
        city = pd.Series(data.loc[:, key].value_counts(), name='投诉单')
        # proportion = pd.Series(city / city.sum(), name='比例')
        out = pd.DataFrame(city)
        out = self.rank(out, city)
        out['投诉单'] = out['投诉单'].astype('int32')
        total = sum(out.iloc[:, 0])
        out.loc['全省'] = [total]
        return out

        # out = pd.concat([city, proportion], axis=1)
        # print(out)
        # print('～～～～上面是原始统计～～～下面是归并其他～～～～')
        # 设置缺省index：全部地市+其他
        # arr_default = ['杭州', '宁波', '温州', '金华', '嘉兴', '绍兴', '衢州', '湖州', '台州', '丽水', '舟山', '其他']
        # out.loc['其他'] = 0
        # # 不在指定范围的数量累计到其他，如外省投诉
        # for x in city.index:
        #     if x not in arr_default:
        #         out.loc['其他'] += out.loc[x]
        # out = pd.DataFrame(out, index=arr_default).fillna(0)
        # out['个数'] = out['个数'].astype('int32')
        # # out['比例'] = out['比例'].apply(lambda x: format(x, '.2%'))
        # return out

    def __export__(self, final, save_path):
        outwb = openpyxl.Workbook()
        # outsheet = outwb.create_sheet(index=0)
        outwb.save(save_path)
        final.to_excel(save_path, 'Sheet1')