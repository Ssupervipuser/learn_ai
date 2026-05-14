import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris  #加载鸢尾花测试集
from sklearn.model_selection import train_test_split  #分割训练集和测试集的
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score          #模型评估




#1. 定义函数，加载鸢尾花数据集，查看数据集
def dm01_loadiris():
    iris_data=load_iris()
    # print(f'数据集: {iris_data}')    #字典形态
    # print(type(iris_data))        #查看数据类型

    print(f'数据集所有的键：{iris_data.keys()}')

    #查看数据集键对应的值
    print(iris_data.data)       #dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
    #查看标签对应的名称
    print(f'标签对应的名称{iris_data.target_names}')       #['setosa' 'versicolor' 'virginica']
    print(f'特征对应的名称{iris_data.feature_names}')      #['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    # print(f'数据集的描述：{iris_data.DESCR}')
    # print(f'数据集的框架{iris_data.frame}')
    # print(f'数据集的文件名{iris_data.filename}')
    # print(f'数据集的数据模块{iris_data.data_module}')

#定义函数绘制数据集的散点图
def dm02_showiris():
    #1.加载数据集
    iris_data=load_iris()
    #2.把数据集封装成Dtaframe对象
    iris_df=pd.DataFrame(iris_data.data,columns=iris_data.feature_names)

    #3.新增标签列
    iris_df['label']=iris_data.target
    # print(iris_df)

    #4.绘图
    # plt.figure(figsize=(20,20))
    #          数据集          x轴数据            y轴数据                 按什么分组       是否显示拟合回归线
    sns.lmplot(data=iris_df,x='sepal length (cm)',y='sepal width (cm)',hue='label',fit_reg=False)
    #5.设置标题
    plt.title('iris data')
    plt.tight_layout()
    plt.show()

    #定义函数，切分训练集和测试集
def dm03_split_train_test():
    iris_data=load_iris()

    #2.数据集的预处理，从150个特征标签中，按照8：2的笔记，切分训练集和测试集
    #返回值，第1个参数的训练集，第1个参数的测试集，第2个参数的训练集，第2个参数的测试集

    x_train,x_test,y_train,y_test=train_test_split(iris_data.data,iris_data.target,test_size=0.2,random_state=23)

    #3.打印切割后的结果
    print(f'训练集的特征：{x_train},个数：{len(x_train)}')
    print(f'训练集的标签：{y_train},个数：{len(y_train)}')
    print(f'测试集的特征：{x_test},个数：{len(x_test)}')
    print(f'测试集的特征：{y_test},个数：{len(y_test)}')


#定义函数，实现鸢尾花完整案例，加载数据，数据预处理，特征工程 ，模型训练，模型评估，模型预测

def dm04_iris_evaluate_test():
    iris_data=load_iris()

    #2.数据的预处理
    x_train,x_test,y_train,y_test=train_test_split(iris_data.data,iris_data.target,test_size=0.3,random_state=23)
    #3.特征工程（提取，预处理）
    #思考1：特征提取，因为源数据只有4个特征列，且都是我们用的，所以这里无需做特征提取
    #思考2：特征预处理：因为元数据的4列特征差值不大，所以我们无需做特征预处理，但是加入特征预处理会让我们的代码更完善，所以加入

    #1.创建标准化对象
    transfer=StandardScaler()

    #2.对特征列进行标准化，
    #fit_trasform :兼具训练和转换，适用于第一次标准化的时候使用，一般用于处理训练集
    x_train=transfer.fit_transform(x_train)
    #transform只有转换，适用于重复进行标准化时使用，一般用于对测试集进行标准化
    x_test=transfer.transform(x_test)
    # print(x_train)
    #4.训练模型
    # # 1.创建模型对象
    estimator=KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train,y_train)      #传入训练集的特征数据，训练集的标签数据

    #5.模型预测
    #场景1： 对刚才切分的测试集进行测试
    y_pre=estimator.predict(x_test)
    print(f'预测值为：{y_pre}')


    #场景2.对新的数据集进行测试
    #1.自定义测试数据集
    my_data=[[7.8,2.1,3.9,1.6]]

    #2.对数据集进行标准化处理
    my_data=transfer.transform(my_data)

    #3.模型预测
    y_pre_new=estimator.predict(my_data)
    print(f'预测值为：{y_pre_new}')

    #4.查看上述数据集，每种分类的预测概率
    y_pre_new=estimator.predict_proba(my_data)
    print(f'(各分类）预测概率为：{y_pre_new})')           #[[0.         0.66666667 0.33333333]])

    #6.模型评估
    #方式1. 直接评分，基于训练集的特征和训练集的标签
    print(f'正确率：{estimator.score(x_train,y_train)}')
    #方式2. 基于 测试集的标签和预测结果进行评分  方式2更准确
    print(f'正确率{accuracy_score(y_test,y_pre)}')



if __name__ == '__main__':
    # dm01_loadiris()
    # dm02_showiris()
    # dm03_split_train_test()
    dm04_iris_evaluate_test()