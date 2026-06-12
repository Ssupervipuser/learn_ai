"""
torch.tensor  根据指定数据创建张量
torch.Tensor  根据指定形状创建张量，其他也可以用来创建指定数据的张量
torch.IntTensor torch.FloatTensor torch.DoubleTensor


"""

import torch
import numpy as np

# torch.tensor  根据指定数据创建张量
def dem01():
    #一维
    t1=torch.tensor(10)
    print(f't1:{t1},type:{type(t1)}')
    print('-'*20)
    
    #二维
    data=[
        [1,2,3],[4,5,6]
    ]
    t2=torch.tensor(data)
    print(f't2:{t2},type:{type(t2)}')
    print('-' * 20)
    
    #numpy nd数组
    data=np.random.randint(0,10,size=(2,3))
    t3=torch.tensor(data)
    print(f't3:{t3},type:{type(t3)}')
    print('-' * 20)
    
    
    
# torch.Tensor  根据指定形状创建张量，其他也可以用来创建指定数据的张量
def dm02():
    data=torch.Tensor(2,3)
    data=torch.Tensor([10])
    data=torch.Tensor([10,20])
    print(data)
    print('-*20')
    # 一维
    t1 = torch.Tensor(10)
    print(f't1:{t1},type:{type(t1)}')
    print('-' * 20)

    # 二维
    data = [
        [1, 2, 3], [4, 5, 6]
    ]
    t2 = torch.Tensor(data)
    print(f't2:{t2},type:{type(t2)}')
    print('-' * 20)

    # numpy nd数组
    data = np.random.randint(0, 10, size=(2, 3))
    t3 = torch.Tensor(data)
    print(f't3:{t3},type:{type(t3)}')
    print('-' * 20)

# torch.IntTensor torch.FloatTensor torch.DoubleTensor
def dm03():
    data=torch.IntTensor(2,3)
    print(data)
    data=torch.ShortTensor()
    print(data)

if __name__ == '__main__':
    # dem01()
    # dm02()
    dm03()


