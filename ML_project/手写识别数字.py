import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
#保存模型
import joblib
from collections import Counter


#1.定义函数，接收用户传入的索引，展示，该索引对应的图片
def show_digit(idx):
    #1.读取数据集，获取到源数据
    df=pd.read_csv('./data/手写数字识别.csv')
    # print(df
    #2.判断传入的索引是否越界

    if idx<0 or idx>len(df)-1:
        print('索引越界')

    #3.走到这里说明没有越界，就正常获取数据
    x=df.iloc[:,1:]
    y=df.iloc[:,0]

    #4.查看用户传入的索引对应的图片是几？
    # print(f'该图片对应的数字是{y.iloc[idx]}')
    print(f'查看所有的标签分布情况：{Counter(y)}')  #Counter({1: 4684, 7: 4401, 3: 4351, 9: 4188, 2: 4177, 6: 4137, 0: 4132, 4: 4072, 8: 4063, 5: 3795})

    #5.查看下用户传入索引对应的图片形状
    # print(x.iloc[idx].shape)        #(784,)
    # print(x.iloc[idx].values)

    #6.把784转换成28，28
    x=x.iloc[idx].values.reshape(28,28)
    # print(x)


    #7.绘制图片
    plt.imshow(x,cmap='gray')
    plt.axis('off')
    plt.show()

#2.#训练，保存模型
def train_model():
    #1.加载数据集
    df=pd.read_csv('./data/手写数字识别.csv')
    #2.数据预处理
    # 1.拆分出特征列
    x=df.iloc[:,1:]
    #2.拆分出标签列
    y=df.iloc[:,0]
    #3.打印特征和标签的形状
    print(f'x的形状：{x.shape}')        #x的形状：(42000, 784)
    print(f'y的形状：{y.shape}')        #y的形状：(42000,)
    print(f'查看所有的标签分布情况{Counter(y)}')
    #4.对特征列进行归一化
    x=x/255
    #5.拆分训练集和测试集
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10,stratify=y)

    #3.模型训练
    #1.创建模型对象
    estimator=KNeighborsClassifier(n_neighbors=3)
    #2.训练模型
    estimator.fit(x_train,y_train)

    #4.评估模型
    print(f'准确率{estimator.score(x_test,y_test)}')
    print(f'准确率{accuracy_score(y_test,estimator.predict(x_test))}')

    #5.保存模型
    joblib.dump(estimator,'./my_model/手写数字识别.pkl')
    print('保存成功')


#3.定义函数，测试模型
def use_model():
    #1.加载图片
    x= plt.imread('./data/demo.png')
    #2.绘制图片
    # print(x)
    # plt.imshow(x,cmap='gray')
    # plt.axis('off')
    # plt.show()

    #2.加载模型
    estimator=joblib.load('./my_model/手写数字识别.pkl')

    #3.模型预测
    #1.查看数据集转换
    print(x.shape)
    print(x.reshape(1,784).shape)
    print(x.reshape(1,-1).shape)
    #2.数据集转换
    x=x.reshape(1,-1)

    #3.模型预测
    y_pre=estimator.predict(x)
    print(f'预测值为：{y_pre}')


#4.测试
if __name__ == '__main__':
    # show_digit(9)
    # train_model()
    use_model()