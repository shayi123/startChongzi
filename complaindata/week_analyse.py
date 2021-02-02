from complaindata.month_report import MonthReport
import pandas as pd

if __name__ == '__main__':
    file_tousu_this_month = 'E:/投诉分析/202101/咨询投诉清单宽表20210125-0131.xlsx'
    file_guzhang_this_month = 'E:/投诉分析/202101/移动信号直派单20210125-0131.xlsx'
    file_tousu_last_month = 'E:/投诉分析/202101/咨询投诉清单宽表20210118-0124.xlsx'
    file_guzhang_last_month = 'E:/投诉分析/202101/移动信号直派单20210118-0124.xlsx'
    save_path = './week.xlsx'
    last = '1月18~24'
    this = '1月25~31'

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
    tousu_this_month.__export__(combine, save_path)
