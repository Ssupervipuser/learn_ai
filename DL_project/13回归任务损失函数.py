import torch
import torch.nn as nn

#mae
def dm01():
    #1.定义变量，记录真实值
    y_true=torch.tensor([2.0,2.0,2.0],dtype=torch.float)
    #2.定义变量记录预测值
    y_pred=torch.tensor([1.0,1.0,1.9],requires_grad=True)
    #创建mse
    loss_fn=nn.L1Loss()
    loss=loss_fn(y_pred,y_true)
    print(loss)

#mse
def dm02():
    #1.定义变量，记录真实值
    y_true=torch.tensor([2.0,2.0,2.0],dtype=torch.float)
    #2.定义变量记录预测值
    y_pred=torch.tensor([1.0,1.0,1.9],requires_grad=True)
    #创建mse
    loss_fn=nn.MSELoss()
    loss=loss_fn(y_pred,y_true)
    print(loss)

def dm03():
    #1.定义变量，记录真实值
    y_true=torch.tensor([2.0,2.0,2.0],dtype=torch.float)
    #2.定义变量记录预测值
    y_pred=torch.tensor([1.0,1.0,1.9],requires_grad=True)
    #创建mse
    loss_fn=nn.SmoothL1Loss()
    loss=loss_fn(y_pred,y_true)
    print(loss)
if __name__ == '__main__':
    dm01()
    dm02()
    dm03()