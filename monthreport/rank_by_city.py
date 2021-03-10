from pandas.api.types import CategoricalDtype


class RankByCity(object):
    custom_order = CategoricalDtype(['杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '丽水', '台州', '舟山', '全省'],
                                    ordered=True)

    @staticmethod
    def rank(df, city_col_name, irregular_city_list=[]):
        """
        :param df: 被排序的DataFrame
        :param city_col_name: 将此列作为索引
        :param irregular_city_list: 修订city_col_name列中不合规范的item。规范为custom_order
        :return: 排序后的DataFrame
        """
        # 需要改为全省
        if irregular_city_list:
            a = df.loc[df[city_col_name].isin(irregular_city_list)].index.tolist()
            if a:
                df.loc[a, city_col_name] = '全省'

        df.index = df[city_col_name]
        df.index = df.index.astype(RankByCity.custom_order)
        df = df.sort_index()
        return df
