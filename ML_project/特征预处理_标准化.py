"""
演示特征预处理---标准化操作

特征工程的目的和步骤
    目的：
    利用专业的北京知识和技巧处理数据，用于提升模型的性能
    步骤：
    1.特征提取
    2.特征预处理
    3.特征降维
    4.特征选择
    5.特征组合

标准化介绍：
目的：防治因为量纲（单位）问题，导致特征列的方差相差较大，影响模型的最终结果，
所以通过公式把各列的值 映射到均值为0，标准差为1的正太分布序列

x'=(当前值-该列的品均值）/该列的标准差
x''=x'*(mx-mi）+mi

x' 基于董事算出来的结果
x'‘ 最终的结果
mx  区间最大值
mi 区间最小值

适用于大数据集的处理

方差计算公式，该列每个值，和该列均值的差的平方求和的品均值
标准差计算公式 反差开平方根

"""

from sklearn.preprocessing import MinMaxScaler,StandardScaler

#1.准备数据集
x_train=[[90,2,10,40],[60,4,15,45],[75,3,13,46]]

#2.创建标准化对象
transfer=StandardScaler()

#3.对数据集进行归一化操作
x_train_new=transfer.fit_transform(x_train)


#4.打印处理后的数据
print('标准化后的数据集为：\n')
print(x_train_new)


#5. 打印数据集的均值和方差
print(f'数据集的均值为：{transfer.mean_}')
print(f'数据集的方差为：{transfer.var_}')
print(f'数据集的标准差为：{transfer.scale_}')










