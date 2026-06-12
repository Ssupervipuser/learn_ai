"""

"""

import torch
import torch.nn as nn
from torchsummary import summary


#todo 1.搭建神经网络
class ModelDemo(nn.Module):
    #1.在init魔法方法中，完成初始化
    def __init__(self):
        super().__init__()
        #1.2搭建神经网络-》隐藏层+输出层

        self.linear1=nn.Linear(3,3)
        #1.3对隐藏层进行参数初始化
        nn.init.xavier_normal_(self.linear1.weight)
        nn.init.zeros_(self.linear1.bias)

        self.linear2=nn.Linear(3,2)
        nn.init.kaiming_normal_(self.linear2.weight)
        nn.init.zeros_(self.linear2.bias)

        self.output=nn.Linear(2,2)



    #todo 1.2前向传播，输入层-》隐藏层-》输出层
    def forward(self,x):
        #1.第一层隐藏层计算：加权求和+激活函数
        # x=self.linear1(x)
        # x=torch.sigmoid(x)

        #合并版
        x=torch.sigmoid(self.linear1(x))
        x=torch.relu(self.linear2(x))

        #输出层计算：加权求和+激活函数
        # dim=-1表示永远按最后一个维度开始计算
        x=torch.softmax(self.output(x),dim=-1)
        return x

#todo 2.模型训练
def train():
    #1.创建模型对象
    my_model=ModelDemo()

    #2.创建数据集样本
    data=torch.randn(size=(5,3))
    print(f'data:{data}')
    print(f'data.shape{data.shape}')
    print(f'data.requires_grad:{data.requires_grad}')
    output=my_model(data)

    print(f'data:{data}')
    print(f'data.shape{data.shape}')
    print(f'data.requires_grad:{data.requires_grad}')

    #4.计算和查看模型参数
    print('-----------------计算模型参数------------')

    summary(my_model,input_size=(5,3))
    print('-----------------查看模型参数------------')
    for name,param in my_model.named_parameters():
        print(f'name:{name},param:{param}')

if __name__ == '__main__':
    train()