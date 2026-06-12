import torch
from torch import optim
import matplotlib.pyplot as plt

#1.等间隔学习率衰减
def dm01():
    #1.定义变量，记录初始的学习率，训练的轮数，每轮训练的皮次数
    lr,epochs,iteration=0.1,200,10
    #2.创建数据集
    y_true=torch.tensor([0])
    x=torch.tensor([1.0],dtype=torch.float32)
    w=torch.tensor([1.0],requires_grad=True,dtype=torch.float32)
    #初始化优化器
    optimizer=optim.SGD([w],lr=0.01,momentum=0.9)
    #                           优化器         每次间隔的轮数 衰减率
    s_lr=optim.lr_scheduler.StepLR(optimizer,step_size=50,gamma=0.5)
    lr_list=[]
    epoch_list=[]
    for epoch in range(200):
        #得到当前的学习率，放到列表中
        lr_list.append(s_lr.get_last_lr())
        epoch_list.append(epoch)
        for i in range(iteration):
            #前向传播
            loss=((w*x-y_true)**2)/2.0
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        #每次进行梯度下降旧更新学习率
        s_lr.step()
    plt.plot(epoch_list, lr_list, label="Step LR Scheduler")
    plt.xlabel("Epoch")
    plt.ylabel("Learning rate")
    plt.legend()
    plt.show()


#指定间隔学习率衰减
def dm02():
    #参数初始化
    LR,max_epoch,iteration=0.1,200,10
    #初始化模型参数
    w=torch.tensor([1.0],requires_grad=True,dtype=torch.float32)
    x=torch.tensor([1.0])
    y_true=torch.tensor([0])

    #定义优化器
    optimizer=optim.SGD([w],lr=LR,momentum=0.9)
    #设置指定间隔学习率衰减
    s_lr=optim.lr_scheduler.MultiStepLR(optimizer,milestones=[77,99,133],gamma=0.5)
    lr_list = []
    epoch_list = []
    for epoch in range(max_epoch):
        # 得到当前的学习率，放到列表中
        lr_list.append(s_lr.get_last_lr())
        epoch_list.append(epoch)
        for i in range(iteration):
            # 前向传播
            loss = ((w * x - y_true) ** 2) / 2.0
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        # 每次进行梯度下降旧更新学习率
        s_lr.step()
    plt.plot(epoch_list, lr_list)
    plt.xlabel("Epoch")
    plt.ylabel("Learning rate")
    plt.legend()
    plt.show()


def dm02():
    #参数初始化
    LR,max_epoch,iteration=0.1,200,10
    #初始化模型参数
    w=torch.tensor([1.0],requires_grad=True,dtype=torch.float32)
    x=torch.tensor([1.0])
    y_true=torch.tensor([0])

    #定义优化器
    optimizer=optim.SGD([w],lr=LR,momentum=0.9)
    #设置指定间隔学习率衰减
    s_lr=optim.lr_scheduler.ExponentialLR(optimizer,gamma=0.5)
    lr_list = []
    epoch_list = []
    for epoch in range(max_epoch):
        # 得到当前的学习率，放到列表中
        lr_list.append(s_lr.get_last_lr())
        epoch_list.append(epoch)
        for i in range(iteration):
            # 前向传播
            loss = ((w * x - y_true) ** 2) / 2.0
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        # 每次进行梯度下降旧更新学习率
        s_lr.step()
    plt.plot(epoch_list, lr_list)
    plt.xlabel("Epoch")
    plt.ylabel("Learning rate")
    plt.legend()
    plt.show()






if __name__ == '__main__':
    # dm01()
    dm02()