import torch.nn as nn


#1.均匀分布初始化
def dm01():
    #1.创建一个线性层
    linear=nn.Linear(5,5)
    #2.对权重w进行随机初始化，从0-1均匀分布产生参数
    nn.init.uniform_(linear.weight)
    #3.对偏置b进行随机初始化
    nn.init.uniform_(linear.bias)
    #4.
    print(linear.weight.data)
    print(linear.bias.data)

#2.固定初始化https://www.bilibili.com/video/BV1c5yrBcEEX/?spm_id_from=333.788.player.switch&vd_source=c17e5dfc5f61fa885254eb32803f9fbb&p=43
def dm02():
    linear=nn.Linear(5,3)
    nn.init.constant_(linear.weight,3)
    nn.init.constant_(linear.bias,3)
    print(linear.weight.data)
    print(linear.bias.data)


#3.全0初始化
def dm03():
    linear=nn.Linear(5,5)
    nn.init.zeros_(linear.weight)
    nn.init.zeros_(linear.bias)
    print(linear.weight.data)
    print(linear.bias.data)

#4.全1初始化
def dm04():
    linear=nn.Linear(5,3)
    nn.init.ones_(linear.weight)
    nn.init.ones_(linear.bias)
    print(linear.weight.data)
    print(linear.bias.data)



#5.正态分布随机初始化
def dm05():
    linear=nn.Linear(5,3)
    nn.init.normal_(linear.weight)
    nn.init.normal_(linear.bias)
    print(linear.weight.data)
    print(linear.bias.data)

#6.kaiming初始化
def km():
    linear=nn.Linear(5,3)
    #开明正态分布初始化
    nn.init.kaiming_normal_(linear.weight)

    print(linear.weight.data)

    #凯明均匀分布初始化
    nn.init.kaiming_uniform_(linear.weight)

    print(linear.weight.data)


#7.xavier均匀分布初始化
def xv():
    linear=nn.Linear(5,3)
    nn.init.xavier_normal_(linear.weight)
    print(linear.weight.data)

    nn.init.xavier_uniform_(linear.weight)
    print(linear.weight.data)


if __name__ == '__main__':
    # dm01()
    # dm02()
    # dm03()
    # dm04()
    # dm05()
    # km()
    xv()