from sklearn.preprocessing import StandardScaler #模型预处理
from sklearn.model_selection import train_test_split #数据集划分
from sklearn.linear_model import SGDRegressor #梯度下降回归模型
from sklearn.metrics import mean_squared_error,mean_absolute_error,root_mean_squared_error  #模型评估
import pandas as pd
import numpy as np

# data_url = "http://lib.stat.cmu.edu/datasets/boston"
# raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
# data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
# target = raw_df.values[1::2, 2]


df=pd.read_csv('../data/boston.csv')
# print(df.info())
# print(df.columns)
feature_columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT']

label_column='MEDV'

data=df[feature_columns]
target=df[label_column]


#划分数据集
x_train,x_test,y_train,y_test=train_test_split(data,target,test_size=0.2,random_state=28)

#数据预处理
#创建标准化对象
transfer=StandardScaler()

x_train=transfer.fit_transform(x_train)
x_test=transfer.transform(x_test)


model=SGDRegressor(fit_intercept=True,learning_rate='constant',eta0=0.01)

model.fit(x_train,y_train)

y_predict=model.predict(x_test)

print(f'权重：{model.coef_}')
print(f'偏执：{model.intercept_}')

print(mean_squared_error(y_test,y_predict))
print(mean_absolute_error(y_test,y_predict))
print(root_mean_squared_error(y_test,y_predict))

















