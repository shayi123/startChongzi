from complaindata.month_report import MonthReport
import pandas as pd

if __name__ == '__main__':
    file_tousu_this_week = 'E:/投诉分析/202101/咨询投诉清单宽表20210301-0307.xlsx'
    file_guzhang_this_week = 'E:/投诉分析/202101/移动信号直派单20210301-0307.xlsx'
    file_tousu_last_week = 'E:/投诉分析/202101/咨询投诉清单宽表20210222-0228.xlsx'
    file_guzhang_last_week = 'E:/投诉分析/202101/移动信号直派单20210222-0228.xlsx'
    save_path = './week.xlsx'
    last = '2月22~28'
    this = '3月01~07'

    # 先传last month，再传this month
    tousu_this_month = MonthReport(file_tousu_this_week)
    tousu_last_month = MonthReport(file_tousu_last_week)
    guzhang_this_month = MonthReport(file_guzhang_this_week)
    guzhang_last_month = MonthReport(file_guzhang_last_week)

    last_month = pd.concat([guzhang_last_month.calculate_guzhang('本地网', '详单'), tousu_last_month.__calculate__('地市', 'sheet1')], axis=1)
    this_month = pd.concat([guzhang_this_month.calculate_guzhang('本地网', '详单'), tousu_this_month.__calculate__('地市', 'sheet1')], axis=1)
    combine = pd.concat([last_month, this_month], keys=[last, this], axis=1)
    combine['合计涨幅(单量)'] = (combine.iloc[:, 2] + combine.iloc[:, 3]) - (combine.iloc[:, 0] + combine.iloc[:, 1])
    combine['合计涨幅'] = (combine['合计涨幅(单量)']/(combine.iloc[:, 0] + combine.iloc[:, 1])).apply(lambda x: format(x, '.2%'))
    print(combine)
    tousu_this_month.__export__(combine, save_path)
