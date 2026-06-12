import torch
import numpy as np


def f01():
    # 1使用标量创建tensor
    out = torch.tensor(10)
    print(out, type(out), out.dtype)

    a = [5., 6., 7.]
    out1 = torch.tensor(a)
    print(out1, type(out1), out1.dtype)

    # 从numpy创建张量
    b = np.array([5, 6, 7])
    out2 = torch.tensor(b)
    print(out2, type(out2), out2.dtype)


def f02():
    out = torch.Tensor(2,3)
    print(out, out.shape,type(out), out.dtype)

    a=np.array([[5,6,7],[8,9,10]])
    out1=torch.Tensor(a)
    print(out1, out1.shape,type(out1), out1.dtype)

    b=[1,2,3]
    out2=torch.Tensor(b)
    print(out2,out2.shape,type(out2),out2.dtype)


#-----------------------------------------

def w1():
    ret=torch.tensor([1,2,3,4])
    print(ret)

    T1=torch.Tensor(2,3)
    T2=torch.Tensor([5,6,7])
    print(T1)
    print(T2)


    int1=torch.IntTensor(2,2)
    float2=torch.FloatTensor(2,2)
    double3=torch.DoubleTensor(2,2)

    #tensor


def tton():
    t=torch.tensor([[1,2],[3,4]])
    n=t.numpy()
    print(type(n))

def ntot():
    arr=np.array([[5,6],[7,8]])
    t=torch.from_numpy(arr)
    t2=torch.tensor(arr)
    print(type(t))
    print(type(t2))
    sclar_t=torch.tensor(100)
    out=sclar_t.item()
    print(out,type(out))




if __name__ == '__main__':
    # f01()
    # f02()
    # w1()
    # tton()
    ntot()