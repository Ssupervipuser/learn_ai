import torch
#                           构造数据集对象 数据加载器
from torch.utils.data import TensorDataset, DataLoader
from torch import nn
from torch import optim
from sklearn.datasets import make_regression  # 创建线性回归模型数据集
import matplotlib.pyplot as plt


# 1.定义函数，创建线性回归样本数据
def create_dataset():
    x, y, coef = make_regression(
        n_samples=100,
        n_features=1,
        noise=10,
        bias=14.5,
        coef=True,  # 是否返回系数
        random_state=3
    )
    # print(type(x))    #<class 'numpy.ndarray'>
    # 把数据转换成张量类型
    x = (torch.tensor(x, dtype=torch.float32)).detach()
    y = (torch.tensor(y, dtype=torch.float32)).detach()

    return x, y, coef


# 定义训练函数
def train(x, y, coef):
    # 1.创建数据集对象，把tensor->数据集对象->数据加载器
    dataset = TensorDataset(x, y)

    # 2.创建加载器对象
    dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

    # 3.创建初始的线性回归模型
    #               输入特征维度 输出特征维度
    model = nn.Linear(1, 1)

    # 4.创建损失函数对象
    criterion = nn.MSELoss()
    # 5.创建优化器对象
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    # 6.具体的训练过程
    # 训练轮数，每轮的平均损失值，训练总损失值，训练的样本数
    epochs, loss_list, total_loss, total_sample = 100, [], 0.0, 0
    for epoch in range(epochs):
        # 每轮是分批次训练，
        for train_x, train_y in dataloader:
            # 模型预测(前向传播）
            y_pre = model(train_x)
            # 计算损失值
            loss = criterion(y_pre, train_y.reshape(-1, 1))
            # 梯度清零+反向传播+梯度更新
            optimizer.zero_grad()
            loss.sum().backward()
            # 计算总损失和样本皮次数
            optimizer.step()
            total_loss += loss.item()
            total_sample += 1
        # 把本轮的平均损失，添加到列表中
        loss_list.append(total_loss / total_sample)
        # print(f'轮数{epoch + 1},平均损失值：{total_loss / total_sample}')

    # 7.打印最终训练结果
    print(f'{epochs}轮的平均损失分别为：{loss_list}')

    # 打印回归模型的w
    print(model.weight)
    # 打印回归模型的b
    print(model.bias)

    # 8.绘制损失曲线
    plt.plot(range(epochs), loss_list)
    plt.title('损失值曲线变化图')
    plt.grid()
    plt.show()

    # 9.绘制预测值和真实值的关系
    plt.scatter(x, y)
    y_pre=torch.tensor(data=[v*model.weight+model.bias for v in x])
    y_true=torch.tensor(data=[v*coef+14.5 for v in x])
    plt.plot(x,y_pre,color='red',label='预测值')
    plt.plot(x,y_true,color='b',label='真实值')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    x, y, coef = create_dataset()
    # print('x,y,coef',x,y,coef)
    train(x, y, coef)
