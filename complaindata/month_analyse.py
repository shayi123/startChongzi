from complaindata.month_report import MonthReport
import pandas as pd

if __name__ == '__main__':
    file_tousu_this_month = 'E:/投诉分析/202011/咨询投诉清单宽表202011.xlsx'
    file_guzhang_this_month = 'E:/投诉分析/202011/移动信号直派单202011.xlsx'
    file_tousu_last_month = 'E:/投诉分析/202011/咨询投诉清单宽表202010.xlsx'
    file_guzhang_last_month = 'E:/投诉分析/202011/移动信号直派单202010.xlsx'
    save_path_tousu = './202011tousu.xlsx'
    save_path_guzhang = './202011guzhang.xlsx'
    last = '10月'
    this = '11月'

    # 先传last month，再传this month
    tousu_this_month = MonthReport(file_tousu_this_month)
    tousu_last_month = MonthReport(file_tousu_last_month)
    guzhang_this_month = MonthReport(file_guzhang_this_month)
    guzhang_last_month = MonthReport(file_guzhang_last_month)

    last_month = pd.concat([guzhang_last_month.calculate_guzhang('本地网', '详单'), tousu_last_month.__calculate__('地市', 'Sheet1')], axis=1)
    this_month = pd.concat([guzhang_this_month.calculate_guzhang('本地网', '详单'), tousu_this_month.__calculate__('地市', 'Sheet1')], axis=1)
    combine = pd.concat([last_month, this_month], keys=[last, this], axis=1)
    combine['合计涨幅(单量)'] = (combine.iloc[:, 2] + combine.iloc[:, 3]) - (combine.iloc[:, 0] + combine.iloc[:, 1])
    combine['合计涨幅'] = (combine['合计涨幅(单量)']/(combine.iloc[:, 0] + combine.iloc[:, 1])).apply(lambda x: format(x, '.2%'))
    print(combine)
    # 投诉
    tousu_this_month = MonthReport(file_tousu_this_month)
    tousu_last_month = MonthReport(file_tousu_last_month)
    combine_tousu = pd.concat([tousu_this_month.__calculate__('地市', 'Sheet1'), tousu_last_month.__calculate__('地市', 'Sheet1')], axis=1)
    combine_tousu['涨幅(比例)'] = (
                (combine_tousu.iloc[:, 0] - combine_tousu.iloc[:, 1]) / combine_tousu.iloc[:, 1]). \
        apply(lambda x: format(x, '.2%'))
    combine_tousu['涨幅（单数)'] = combine_tousu.iloc[:, 0] - combine_tousu.iloc[:, 1]
    print(combine_tousu)
    tousu_this_month.__export__(combine_tousu, save_path_tousu)

    # 故障
    guzhang_this_month = MonthReport(file_guzhang_this_month)
    guzhang_last_month = MonthReport(file_guzhang_last_month)
    combine_guzhang = pd.concat([guzhang_this_month.calculate_guzhang('本地网', '详单'), guzhang_last_month.calculate_guzhang('本地网', '详单')], axis=1)
    combine_guzhang['涨幅(比例)'] = (
                (combine_guzhang.iloc[:, 0] - combine_guzhang.iloc[:, 1]) / combine_guzhang.iloc[:, 1]). \
        apply(lambda x: format(x, '.2%'))
    combine_guzhang['涨幅（单数)'] = combine_guzhang.iloc[:, 0] - combine_guzhang.iloc[:, 1]
    print(combine_guzhang)
    guzhang_this_month.__export__(combine_guzhang, save_path_guzhang)
