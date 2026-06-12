import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader
from torch import nn, optim


def create_datasete():
    data=pd.read_csv('../data/手机价格预测.csv')
    # print(data.head())
    x,y=data.iloc[:,:-1],data.iloc[:,-1]

    #数据类型转换
    x=np.array(x).astype(np.float32)
    y=np.array(y).astype(np.int64)
    #数据集划分
    #1.分成训练集和临时集
    x_trian,x_temp,y_train,y_temp=train_test_split(x,y,test_size=0.2,random_state=42,shuffle=True,stratify=y)
    #2.验证集和测试集
    x_val,x_test,y_val,y_test=train_test_split(x_temp,y_temp,test_size=0.5,random_state=42,shuffle=True,stratify=y_temp)

    #创建训练集对象，验证集对象，测试集对象
    train_dataset=TensorDataset(torch.from_numpy(x_trian),torch.from_numpy(y_train))
    val_dataset=TensorDataset(torch.from_numpy(x_val),torch.from_numpy(y_val))
    test_dataset=TensorDataset(torch.from_numpy(x_test),torch.from_numpy(y_test))

    #类别总数
    class_=np.unique(y)
    class_number=len(class_)
    return train_dataset,val_dataset,test_dataset,x_trian.shape[1],class_number

#自定义神经网络模型
class MyModel(nn.Module):
    def __init__(self,feature_number,class_number):
        super().__init__() #初始化父类
        self.linear1=nn.Linear(feature_number,128)
        self.linear2=nn.Linear(128,256)
        self.linear3=nn.Linear(256,class_number)
        self.activation=nn.ReLU()

    def forward(self,x):
        #第一层
        x=self.linear1(x)
        #激活函数
        a=self.activation(x)
        x=self.linear2(a)
        a=self.activation(x)
        x=self.linear3(a)
        return x

#          训练集         验证集         特征数量        种类数量
def train(train_dataset,val_dataset,feature_number,class_number):
    #构建dataloader
    train_dataloader=DataLoader(train_dataset,batch_size=32,shuffle=True)
    val_dataloader=DataLoader(val_dataset,batch_size=1,shuffle=False)
    #创建模型
    model=MyModel(feature_number,class_number)
    #定义优化器
    optimizer=optim.Adam(model.parameters(),lr=0.001)

    #等间隔学习率衰减

    s_lr=optim.lr_scheduler.StepLR(optimizer,step_size=150,gamma=0.5)
    #创建损失函数
    loss_fn=nn.CrossEntropyLoss()
    #创建空列表
    loss_epoch_train=[]
    loss_epoch_val=[]
    epochs=300
    #开启对轮数epochs的循环
    for epoch in range(epochs):
        #记录训练集总损失
        total_loss=0.0
        #记录验证机的总损失
        total_eval_loss=0.0
        #将model设置为训练模式
        model.train()
        #将每个批次训练
        for i,(x,y) in enumerate(train_dataloader):
            #前向传播
            pred=model(x)
            #计算总损失
            loss=loss_fn(pred,y)
            #梯度清零
            optimizer.zero_grad()
            #反向传播
            loss.backward()
            #梯度下降
            optimizer.step()
            #记录当前总损失
            total_loss+=loss.item()
        loss_epoch_train.append(total_loss/len(train_dataloader))
        print(f'epoch={epoch},train_loss={total_loss/len(train_dataloader)}')
        for i ,(x,y) in enumerate(val_dataset):
            model.eval()#设置模型为验证模式
            #前向传播
            pred=model(x)
            loss=loss_fn(pred,y)
            total_eval_loss+=loss.item()
        loss_epoch_val.append(total_eval_loss/len(val_dataset))
        #更新学习率
        s_lr.step()
        #每20轮保存一次模型
        if epoch%20==0:
            print('save model')
            torch.save(model.state_dict(),f'./model/model_{epoch}.pth')

    #画图
    plt.plot(np.array(range(epochs)),np.array(loss_epoch_train),color='r',label='train_loss')
    plt.plot(np.array(range(epochs)),np.array(loss_epoch_val),color='b',label='val_loss')
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid()
    plt.show()

def model_test(test_dataset,feature_number,class_numer):
    #创建test dataloader
    test_dataloader=DataLoader(test_dataset,batch_size=1,shuffle=False)
    #创建模型
    mymodel=MyModel(feature_number,class_number)
    mymodel.eval()#开启推理模式
    #加载模型参数
    mymodel.load_state_dict(torch.load('./model/model_280.pth'))
    score=0.0
    for i,(x,y) in enumerate(test_dataset):
        #前向传播
        pred=mymodel(x)
        #获取最大概率的索引
        id=torch.argmax(pred.detach(),dim=-1)
        #比较预测索引和真实索引
        if id.item()==y.item():
            score+=1
    #最终的准确率
    print(f'score={score/len(test_dataset)}')


if __name__ == '__main__':
    train_dataset,val_dataset,test_dataset,feature_number,class_number=create_datasete()
    # print(feature_number,class_number)
    train(train_dataset,val_dataset,feature_number,class_number)
    # model_test(test_dataset,feature_number,class_number)