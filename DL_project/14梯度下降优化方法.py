import torch
import torch.nn as nn
from torch import optim

#梯度下降优化方法-》动量法
def dm01():
    #1.初始化权重参数
    w=torch.tensor([1.0],requires_grad=True)
    #2.定义损失函数
    loss_fn=((w**2)/2.0)
    #3.创建优化器——》基于SGD加入参数momentum，就是动量法
    optimizer=optim.SGD(params=[w],lr=0.01,momentum=0.9)
    #4.计算梯度值
    #梯度清零
    optimizer.zero_grad()
    #反向传播
    loss_fn.sum().backward()

    #参数更新
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')
    loss_fn=((w**2)/2.0)

    # 梯度清零
    optimizer.zero_grad()
    # 反向传播
    loss_fn.sum().backward()

    # 参数更新
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

#adagrad
def dm02():
    #1.初始化权重参数
    w=torch.tensor([1.0],requires_grad=True)
    #2.定义损失函数
    loss_fn=((w**2)/2.0)
    #3.创建优化器——》基于SGD加入参数momentum，就是动量法
    optimizer=optim.Adagrad(params=[w],lr=0.01)
    #4.计算梯度值
    #梯度清零
    optimizer.zero_grad()
    #反向传播
    loss_fn.sum().backward()

    #参数更新
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

    loss_fn=((w**2)/2.0)

    # 梯度清零
    optimizer.zero_grad()
    # 反向传播
    loss_fn.sum().backward()

    # 参数更新
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')


#rmsprop
def dm03():
    #1.初始化权重参数
    w=torch.tensor([1.0],requires_grad=True)
    #2.定义损失函数
    loss_fn=((w**2)/2.0)
    #3.创建优化器——》基于SGD加入参数momentum，就是动量法
    optimizer=optim.RMSprop(params=[w],lr=0.01)
    #4.计算梯度值
    #梯度清零
    optimizer.zero_grad()
    #反向传播
    loss_fn.sum().backward()

    #参数更新
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

    loss_fn=((w**2)/2.0)

    # 梯度清零
    optimizer.zero_grad()
    # 反向传播
    loss_fn.sum().backward()

    # 参数更新
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

#adam
def dm04():
    #1.初始化权重参数
    w=torch.tensor([1.0],requires_grad=True)
    #2.定义损失函数
    loss_fn=((w**2)/2.0)
    #3.                                    betas(梯度用的衰减系数，学习率)
    optimizer=optim.Adam(params=[w],lr=0.01,betas=(0.9,0.999))
    #4.计算梯度值
    #梯度清零
    optimizer.zero_grad()
    #反向传播
    loss_fn.sum().backward()

    #参数更新
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

    loss_fn=((w**2)/2.0)

    # 梯度清零
    optimizer.zero_grad()
    # 反向传播
    loss_fn.sum().backward()

    # 参数更新
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

if __name__ == '__main__':
    dm01()
    dm02()
    dm03()
    dm04()