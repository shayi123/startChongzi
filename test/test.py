import pandas as pd
import numpy as np

train = pd.read_csv('/Users/shelly/PycharmProjects/startChongzi/test/loans_data_train.csv')
test = pd.read_csv('/Users/shelly/PycharmProjects/startChongzi/test/test_loans_data_no_loan_status.csv')
df_y = train['loan_status']

df_y.value_counts()

df_y = np.where(((train['loan_status'] == 'Current') | (train['loan_status'] == 'Fully Paid')), 1, 0)

df1 = train.drop('loan_status', axis=1)
df = pd.concat([df1, test], axis=0)

df.info()
df = df.fillna(method='ffill')
df['bc_util'] = df['bc_util'].fillna(df['bc_util'].mean())

df_dummies = pd.get_dummies(df)

df_dummies.describe()
df_train_x = df_dummies.iloc[0:85454]
df_test_x = df_dummies.iloc[85454:105455]

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, class_weight={0.0: 0.85, 1.0: 0.15})
model.fit(df_train_x, df_y)
pridict = model.predict(df_test_x)
np.savetxt('/Users/shelly/PycharmProjects/startChongzi/test/pred3.txt', pridict)

# 老师的代码
import pandas as pd
import numpy as np

data = pd.read_csv('/Users/shelly/PycharmProjects/startChongzi/test/loans_data_train.csv')
data.shape
data.head()
data.info()

# 数据清洗
data['int_rate'] = data['int_rate'].str.rstrip('%').astype('float')
data['revol_util'] = data['revol_util'].str.rstrip('%').astype('float')
data[['int_rate', 'revol_util']].info()

null_rate = data.isnull().sum() / (len(data))
al = pd.DataFrame(list(zip(data.columns, null_rate, data.dtypes)), columns=['columns', 'null_rate', 'dtype'])
al = al.sort_values('null_rate', ascending=False)

from sklearn.preprocessing import Imputer

numColumns = data.select_dtypes(include=['float64', 'int64']).columns
imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
imr = imr.fit(data[numColumns])
data[numColumns] = imr.transform(data[numColumns])

# 对于object填充Unknown
objectColumns = data.select_dtypes(include=["object"]).columns
data[objectColumns] = data[objectColumns].fillna("Unknown")
data.isnull().sum().sum()

objectColumns = data.select_dtypes(include=["object"]).columns
data[objectColumns].shape
for v in objectColumns:
    print(data[v].value_counts())

# 特征抽象

data['loan_status'].value_counts()
data['loan_status'] = np.where((data['loan_status'] == 'Fully Paid') | (data['loan_status'] == 'Current'), 1, 0)
data['loan_status'].value_counts()

data[data["purpose"].isin(['other']) == False]

from sklearn.preprocessing import LabelEncoder

# 定义标签二值化方法
class_le = LabelEncoder()
# 标签二值化0->10，1->01
data["loan_status"] = class_le.fit_transform(data["loan_status"])

# 构建mapping，对有序变量"emp_length”、“grade”进行转换
mapping_dict = {
    "emp_length": {
        "10+ years": 10,
        "9 years": 9,
        "8 years": 8,
        "7 years": 7,
        "6 years": 6,
        "5 years": 5,
        "4 years": 4,
        "3 years": 3,
        "2 years": 2,
        "1 year": 1,
        "< 1 year": 0,
        "Unknown": 0
    },
    "grade": {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7
    }}  # 定义映射关系
data = data.replace(mapping_dict)  # 变量映射
data[['emp_length', 'grade']].head()

data.select_dtypes(include=["object"]).columns
data = pd.get_dummies(data)
data.info()
df_X = data.drop('loan_status', axis=1)
df_y = data['loan_status']

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
df_X_sc = sc.fit_transform(df_X)

import time
from sklearn import metrics  # 构建混淆矩阵
from sklearn.linear_model import LogisticRegression  # 导入逻辑回归
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier  # 导入集成算法

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(df_X_sc, df_y, test_size=0.3)

print("\n调用scikit的LogisticRegression() ")
model = LogisticRegression()
time_start = time.time()
model.fit(x_train, y_train)
print("模型训练用时 %fs" % (time.time() - time_start))
predicted = model.predict(x_test)
print(metrics.classification_report(y_test, predicted))
print(metrics.confusion_matrix(y_test, predicted))

print("\n调用scikit的RandomForestClassifier() ")
model = RandomForestClassifier(random_state=1, n_estimators=100, min_samples_split=8, min_samples_leaf=4)

model.fit(x_train, y_train)

print(model)
predicted = model.predict(x_test)
print(metrics.classification_report(y_test, predicted))
print(metrics.confusion_matrix(y_test, predicted))

from sklearn.metrics import classification_report

print(classification_report(y_test, predicted))