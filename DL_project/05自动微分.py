import torch
#标量张量计算梯度
#1.定义变量，记录初始的权重w旧

w=torch.tensor(10,dtype=torch.float,requires_grad=True)

#2.定义loss变量，表示损失函数
loss=2*w**2

#3打印梯度函数类型
print({type(loss.grad_fn)})

#4.计算梯度，梯度=损失函数的导数，计算完毕后，会记录到w.grad属性中
loss.backward()

#5.带入权重更新公式，w新=w旧=学习率*梯度
w.data=w.data-0.01*w.grad

print(w)



#1定义初始权重
w=torch.tensor(10,requires_grad=True,dtype=torch.float)


#3更新
for i in range(1,101):
    #前向传播
    loss=w**2+20
    #梯度清零
    if w.grad is not None:
        w.grad.zero_()
    #反向传播
    loss.sum().backward()

    #梯度更新w.data=w.data-0.01*w.grad
    # print(f'梯度值为：{w.grad}')
    w.data = w.data - 0.01 * w.grad

    print(f'第{i}次，权重初始值：{w}，(0.01*w.grad):{0.01*w.grad},loss:{loss.item()}')

# print(w)