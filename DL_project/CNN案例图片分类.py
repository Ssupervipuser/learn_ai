import torch
import torch.nn as nn
from torchvision.datasets import CIFAR10
from torchvision.transforms import ToTensor  # pip install torchvision -i https://mirrors.aliyun.com/pypi/simple/
import torch.optim as optim
from torch.utils.data import DataLoader
import time
import matplotlib.pyplot as plt
from torchsummary import summary

# 每批次样本数
# BATCH_SIZE = 8

#创建数据集
def create_dataset():
    #创建训练集和测试集数据

    train=CIFAR10(root='data',train=True,transform=ToTensor())
    test=CIFAR10(root='data',train=False,transform=ToTensor())
    return train,test

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        #第一个卷积层
        self.conv1=nn.Conv2d(in_channels=3,out_channels=6,kernel_size=3,stride=1,padding=1)
        #创建池化层
        self.pool1=nn.MaxPool2d(kernel_size=2,stride=2)
        #第二个卷积层
        self.conv2=nn.Conv2d(in_channels=6,out_channels=16,kernel_size=3,stride=1,padding=1)
        #创建池化层
        self.pool2=nn.MaxPool2d(kernel_size=2,stride=2)
        #全连接层
        self.linear1=nn.Linear(1024,120)
        self.linear2=nn.Linear(120,84)
        self.out=nn.Linear(84,10)
        #激活函数
        self.activation=nn.ReLU()

    def forward(self,x):
        #卷积+激活+池化
        x=self.pool1(self.activation(self.conv1(x)))
        x=self.pool2(self.activation(self.conv2(x)))
        #n c h w ->n  c*h*w
        x=x.flatten(start_dim=1)
        #全连接+激活
        x=self.activation(self.linear1(x))
        x=self.activation(self.linear2(x))
        x=self.out(x)
        return x

def train_model(model,train_dataset):
    #创建dataloader
    dataloader=DataLoader(train_dataset,batch_size=4,shuffle=True)
    #创建优化器
    optimizer=optim.Adam(model.parameters(),lr=0.001)
    #创建损失函数
    loss_fn=nn.CrossEntropyLoss()
    #
    epochs=10
    for epoch in range(epochs):
        total_loss=0.0
        n=0.0
        model.train()
        for idx,(x,y) in enumerate(dataloader):
            #前向传播
            y_pred=model(x)
            #计算损失
            loss=loss_fn(y_pred,y)
            #梯度清零
            optimizer.zero_grad()
            #反向传播
            loss.backward()
            #梯度下降
            optimizer.step()
            total_loss+=loss.item()
            n+=1
        print(f'epoch={epoch},loss={total_loss/n}')
    torch.save(model.state_dict(),f'./model/model_cifa.pth')

if __name__ == '__main__':
    train_dataset,test_dataset=create_dataset()
    # print(f'数据集类别：{train_dataset.class_to_idx}')
    # #打印训练集和测试集的数据尺寸
    # print(f'训练集数据尺寸：{train_dataset.data.shape}')
    # print(f'测试集数据尺寸：{test_dataset.data.shape}')
    #
    # #图像展示
    # plt.imshow(train_dataset.data[0])
    # plt.title(train_dataset.targets[0])
    # plt.show()

    model=Net()
    # inputs=torch.randn(2,3,32,32)
    # p=model(inputs)
    # print(p.shape)
    train_model(model,train_dataset)