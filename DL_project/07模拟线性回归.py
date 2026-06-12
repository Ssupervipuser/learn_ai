import torch
from torch.utils.data import TensorDataset  #构造数据集对象
from torch.utils.data import DataLoader     #数据加载器
from torch import nn        #nn模块中有平方损失函数和假设函数
from torch import optim     #optim模块中有优化器函数
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False        #用来正常显示负号

#1.定义函数，创建数据集对象
def create_dataset():
    x,y,coef=make_regression(
        n_samples=100,      #100条样本
        n_features=1,
        noise=10,
        coef=True,
        bias=14.5,
        random_state=3
    )
    #2把上述数据封装成张量对象
    x=torch.tensor(x,dtype=torch.float)
    y=torch.tensor(y,dtype=torch.float)

    return x,y,coef

def img(x,y,coef,bias):
    plt.scatter(x,y)

    x1=torch.tensor([x.min(),x.max()])
    y1=torch.tensor([v*coef+bias for v in x1])

    #绘制直线图
    plt.plot(x1,y1,label='real',color='r')
    plt.grid()
    plt.legend()



    plt.show()

#定义函数表示训练模型
def train(x,y,coef):
    #1.创建数据集对象，把tensor->数据集对象->数据加载器
    dataset=TensorDataset(x,y)
    # for data in dataset:
    #     print('dataset:',data)
    #2.创建数据加载器对象
    dataloader=DataLoader(dataset,batch_size=16,shuffle=True)

    #3.创建初始的线性回归模型
    #               输入维度特征  输出维度特征
    model=nn.Linear(1,1)
    #4.创建损失函数对象
    criterion=nn.MSELoss()

    #5.创建优化器对象
    optimizer=optim.SGD(model.parameters(),lr=0.01)

    for x,y in dataloader:
        x=x.type(torch.float32)
        #前向传播
        y_pre=model(x)
        # print('y_pre',y_pre)
        # print('y',y)
        loss=criterion(y_pre,y.reshape(-1,1).type(torch.float32))
        #梯度清零
        optimizer.zero_grad()
        #反向传播
        loss.backward()
        #梯度下降
        optimizer.step()

        break




    #6.具体的训练过程
    #






if __name__ == '__main__':
    x,y,coef=create_dataset()
    # img(x,y,coef,14.5)
    # print(x,y,coef)

    train(x,y,coef)