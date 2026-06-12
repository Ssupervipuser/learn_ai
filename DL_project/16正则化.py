#dropout 环节过拟合，它能够
import torch
from torch import nn

def f01():
    t1=torch.randint(0,10,size=(1,4)).float()
    linear=nn.Linear(4,5)
    #通常dropout层是放在激活函数之后的
    #正向传播
    l1=linear(t1)
    #创建dropout层
    drop=nn.Dropout(p=0.5)
    d1=drop(l1)
    print(d1)

def f02():
    #创建输入数据
    input=torch.randn(size=(5,2))

    #创建线性层
    linear1=nn.Linear(2,4)
    #前向传播
    l1=linear1(input)
    bn1d=nn.BatchNorm1d(num_features=4,eps=1e-5,momentum=0.1,affine=True)
    #批归一化处理
    out=bn1d(l1)
    print(l1)
    print(out)
    print('-------------内部参数')
    print(f'weight y{bn1d.weight.data}')
    print(f'bias β{bn1d.bias.data}')
    print(f'running_mean{bn1d.running_mean}')
    print(f'running_var{bn1d.running_var}')

if __name__ == '__main__':
    # f01()
    f02()