"""
回顾：
    线性算法属于有监督学习之有特征，有标签，且标签是连续的
    线性回归分类：
        一元线性回归：1个特征列，1个标签列
        多元线性回归，多个特征列，1个标签列
    大白话：
        它是用线性公式来描述特征和标签之间的关系，方便做预测
        一元线性回归：y=w*x+b
        多元y=w1*x1+w2*x2+....+wn*xn+b=w^t*x+b
    如何衡量线性回归模型的好坏？
        思路：
            预测值和真实之间的误差，误差越小，模型越好
        具体方案
        1.最小二乘      每个样本误差平方和
        2.均方误差mse   每个样本误差平方和/样本总数
        3.均方根误差rmse 每个样本误差平方和/样本总数 开平方根
        4.平均绝对误差mae 每个样本误差绝对值和/样本总数

    如果和让损失函数最小？
        思路1：梯度下降法：全体都下降，随机梯度下降，小批量梯度下降（推荐）随机平均梯度下降（）
        思路2：正规方程发：
    线性模型评估方案
    MAE：
    RMSE：
    MSE
    机器学习开发流程：
        1.记载数据
        2.数据的预处理
        3.特征工程
        4.模型训练
        5.模型预测
        6.模型评估
"""
# from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,root_mean_squared_error
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
# print(data)
# print(target)

#2.数据预处理
x_train,x_test,y_train,y_test=train_test_split(data,target,test_size=0.2,random_state=27)

#3.特征工程
transfer=StandardScaler()

x_train=transfer.fit_transform(x_train)
x_test=transfer.transform(x_test)

#4.模型训练
model=LinearRegression(fit_intercept=True)
model.fit(x_train,y_train)

#5.模型预测
y_predict=model.predict(x_test)
print(f'预测值：{y_predict}')
print(f'权重：{model.coef_}')
print(f'偏置：{model.intercept_}')

#6.模型评估
print(f'平均绝对误差：{mean_absolute_error(y_test,y_predict)}')
print(f'均方误差：{mean_squared_error(y_test,y_predict)}')
print(f'均方根误差：{root_mean_squared_error(y_test,y_predict)}')