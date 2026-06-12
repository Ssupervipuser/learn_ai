import torch
import torch.nn as nn

def dm01():
    #1.手动创建样本的真实值
    y_true=torch.tensor([1,2])

    #2.手动创建样本的预测值
    y_pred=torch.tensor([[0.1,0.8,0.1],[0.7,0.2,0.1]],requires_grad=True)

    #3.创建多分类交叉熵损失函数
    loss_fn=nn.CrossEntropyLoss()

    #4.计算损失值
    loss=loss_fn(y_pred,y_true)
    print(loss)

def dm02():
    y_true=torch.tensor([0,1,0],dtype=torch.float32)
    y_pred=torch.tensor([0.6901,0.5423,0.2639])

    loss_fn=nn.BCELoss()

    loss=loss_fn(y_pred,y_true)
    print(loss)

if __name__ == '__main__':
    dm01()