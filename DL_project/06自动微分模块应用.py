import torch

#1.定义特征
x=torch.ones(2,5)
print(x)

#2.定义标签真实值
y=torch.zeros(2,3)
print(y)

#3.初始化
w=torch.randn(5,3,requires_grad=True )
print(w)
# todo y=xw+b
b=torch.randn(3,requires_grad=True)

#4.正向传播计算出预测值z
z=torch.matmul(x,w)+b
print(z)

#5.定义损失函数
loss=torch.nn.MSELoss()
loss=loss(z,y)
print('loss',loss)
#6.进行自动微分，求导，结合反向传播更新权重
loss.sum().backward()
#7.打印w，b用来更新的梯度
print(f'w的梯度：{w.grad}')
print(f'b的梯度：{b.grad}')


