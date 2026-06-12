import torch
import numpy as np
import matplotlib.pyplot as plt


data = torch.arange(0, 10, 2)
print(data, type(data))

data = torch.linspace(0, 10, 4)
print(data, type(data))

print('查看随机数种子')
print(torch.initial_seed())
torch.manual_seed(50)
def f01():
    data1 = torch.randn(300, 500)
    # print(data, type(data))
    data1=data1*10+5
    out1=data1.flatten()
    plt.hist(out1,bins=100)
    plt.show()


def f02():
    data2 = torch.rand(300, 500)
    print(data2.shape)

    print(data2, type(data2))
    out=data2.flatten()
    print()
    plt.hist(out)
    plt.show()



data = torch.randint(1, 4, [2, 3])
print(data, type(data))

# -----------------------------
data = torch.zeros(5, 3)
print(data, type(data))

data = torch.zeros_like(data)
print(data, type(data))

data = torch.full([2, 3], 2)
print(data, type(data))

data = torch.full_like(data, 20)
print(data, type(data), data.dtype)

# ----------------------------------------

# tensor->numpy
data_t = torch.tensor([2, 3, 4])
print(data_t)
data_n = data_t.numpy()
print(data_n)
print(type(data_t))
print(type(data_n))

data_n[0] = 1
print(data_t)
print(data_n)

# numpy->tensor
datan = np.array([2,3,4])
datat=torch.from_numpy(datan)

if __name__ == '__main__':
    f01()