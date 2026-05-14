"""
KNN算法（K Nearest Neighbors），K临近算法
    原理：
        基于欧式距离（或者其他距离计算方式）计算，测试集 和每个训练集之间的距离，然后根据距离升序排列，找到最近的K个样本
        基于K个样本投票，票数最多的就作为最终预测结果 ——》分类
        基于k个样本计算 平均值，作为最终预测结果 ——》回归问题

    实现思路
        1.分类问题
            适用于有特征，有标签，且标签是不连续的（离散的）
        2.回归
            适用于有特征，有标签，且标签是连续的

    KNN算法，分类问题思路
        1.计算测试集和每个训练的样本之间的 距离
        2.基于距离进行升序排列
        3.找到最近的k个样本
        4.k个样本进行投票
        5.票最多的结果，作为最终的预测结果

    代码实现思路
    1.导包
    2.准备数据集（测试集和训练集）
    3.创建（KNN 分类模型对象）
    4.模型训练
    5.模型预测

"""

from sklearn.neighbors import KNeighborsClassifier

# 2.准备数据集（测试集和训练集）
x_train=[
    [0],
    [1],
    [2],
    [3],

]
y_train=[0,0,1,1]
x_test=[
    [5]
]
# 3.创建（KNN 分类模型对象）
#estimator:估计器，模型对象
estimator=KNeighborsClassifier(n_neighbors=2)


# 4.模型训练
#传入训练集的特征数据，训练集的标签数据
estimator.fit(x_train,y_train)

# 5.模型预测
#传入测试集的特征数据，获取到预测结果
y_predict=estimator.predict(x_test)

print(f'预测值为：{y_predict}')







