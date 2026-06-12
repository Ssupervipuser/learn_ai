import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def linear_model():
    df = pd.read_csv("../data/boston.csv")
    data = df.iloc[:, :-1]
    label = df.iloc[:-1]
    x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.2, random_state=22, shuffle=True)
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)


def dm01():
    np.random.seed(85)
    x = np.random.uniform(-3, 3, size=100)
    y = 0.5 * x ** 2 + x + np.random.normal(0, 1, size=100)

    x = x.reshape(-1, 1)

    model = LinearRegression()
    model.fit(x, y)

    y_perdict = model.predict(x)
    plt.scatter(x, y)
    plt.plot(x, y_perdict, color='r')
    plt.show()


def dm02():
    # 1. 准备x, y数据, 增加上噪声.
    # 用于设置随机数生成器的种子（seed）, 种子一样, 每次生成相同序列.
    np.random.seed(85)
    # x: 随机数, 范围为 (-3, 3), 100个.
    x = np.random.uniform(-3, 3, size=100)
    # loc: 均值, scale: 标准差, normal: 正态分布.
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)
    # 2. 实例化 线性回归模型.
    estimator = LinearRegression()
    # 3. 训练模型
    X = x.reshape(-1, 1)
    X2 = np.hstack([X, X ** 2])
    estimator.fit(X2, y)

    # 4. 模型预测.
    y_predict = estimator.predict(X2)
    print("预测值:", y_predict)

    # 5. 计算均方误差 => 模型评估
    print(f'均方误差: {mean_squared_error(y, y_predict)}')
    # 6. 画图
    plt.scatter(x, y)  # 散点图
    # sort()  该函数直接返回一个排序后的新数组。
    # numpy.argsort()   该函数返回的是数组值从小到大排序时对应的索引值
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')  # 折线图(预测值, 拟合回归线)
    # plt.plot(x, y_predict)
    plt.show()  # 具体的绘图


def dm03():
    # 1. 准备x, y数据, 增加上噪声.
    # 用于设置随机数生成器的种子（seed）, 种子一样, 每次生成相同序列.
    np.random.seed(85)
    # x: 随机数, 范围为 (-3, 3), 100个.
    x = np.random.uniform(-3, 3, size=100)
    # loc: 均值, scale: 标准差, normal: 正态分布.
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)
    # 2. 实例化 线性回归模型.
    estimator = LinearRegression()
    # 3. 训练模型
    X = x.reshape(-1, 1)
    X2 = np.hstack([X, X ** 2, X ** 3, X ** 4, X ** 5, X ** 6, X ** 7, X ** 8, X ** 9, X ** 10])
    estimator.fit(X2, y)

    # 4. 模型预测.
    y_predict = estimator.predict(X2)
    print("预测值:", y_predict)

    # 5. 计算均方误差 => 模型评估
    print(f'均方误差: {mean_squared_error(y, y_predict)}')
    # 6. 画图
    plt.scatter(x, y)  # 散点图
    # sort()  该函数直接返回一个排序后的新数组。
    # numpy.argsort()   该函数返回的是数组值从小到大排序时对应的索引值
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')  # 折线图(预测值, 拟合回归线)
    # plt.plot(x, y_predict)
    plt.show()  # 具体的绘图


from sklearn.neighbors import KNeighborsRegressor


def dm02_knnapi_回归():


    estimator = KNeighborsRegressor(n_neighbors=2)
    X = [[0, 0, 1],
         [1, 1, 0],
         [3, 10, 10],
         [4, 11, 12]]
    y = [0.1, 0.2, 0.3, 0.4]
    estimator.fit(X, y)

    my_predict = estimator.predict([[3, 11, 10]])
    print('myret-->', my_predict)

#------------------------------------------------------------------------------------------------------------

def dm_minmax():
    data=[
        [90,2,10,40],
        [60,4,15,45],
        [75,3,13,46]
    ]

    scaler=MinMaxScaler()
    scaler.fit(data)
    data=scaler.transform(data)
    print(data)

def dm_standard():
    data = [
        [90, 2, 10, 40],
        [60, 4, 15, 45],
        [75, 3, 13, 46]
    ]
    scaler = StandardScaler()
    scaler.fit(data)
    data = scaler.transform(data)
    print(data)

#---------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score




















if __name__ == '__main__':
    # dm01()
    # dm02()

    # dm03()
    # dm02_knnapi_回归()
    # dm_minmax()

    # dm_standard()
    dm_irs()
