"""
演示特征预处理---归一化操作

特征工程的目的和步骤
    目的：
    利用专业的北京知识和技巧处理数据，用于提升模型的性能
    步骤：
    1.特征提取
    2.特征预处理
    3.特征降维
    4.特征选择
    5.特征组合

归一化介绍：
目的：防治因为量纲（单位）问题，导致特征列的方差相差较大，影响模型的最终结果

x'=(当前值-该列最小值）/（该列最大值-该列最小值）
x''=x'*(mx-mi）+mi

x' 基于董事算出来的结果
x'‘ 最终的结果
mx  区间最大值
mi 区间最小值
弊端：
容易收到最大值和最小值的影响，所以他一般用于处理小数据集

"""

from sklearn.preprocessing import MinMaxScaler,StandardScaler

#1.准备数据集
x_train=[[90,2,10,40],[60,4,15,45],[75,3,13,46]]

#2.创建归一化对象
transfer=MinMaxScaler(feature_range=(0,1))

#3.对数据集进行归一化操作
x_train_new=transfer.fit_transform(x_train)

print(x_train_new)