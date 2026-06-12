import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np


def f01():
    #读入图片
    img=plt.imread('img_gril.jpg')
    print(f'img.shape{img.shape}')#img.shape(800, 800, 3)
    img2=torch.tensor(img,dtype=torch.float32)

    #转成CHW
    img2=img2.permute(2,0,1)
    print(f'img2.shape{img2.shape}')#img2.shapetorch.Size([3, 800, 800])
    img3=img2.unsqueeze(0)
    print(f'img3.shape{img3.shape}')#img3.shapetorch.Size([1, 3, 800, 800])

    #创建卷积层
    conv=nn.Conv2d(in_channels=3,out_channels=4,kernel_size=3,stride=1,padding=0)
    #卷积计算
    conv_img=conv(img3)

    #输出
    print(f'conv_img.shape={conv_img.shape}')#conv_img.shape=torch.Size([1, 4, 798, 798])

    #查看提取到的4个特征图
    img4=conv_img[0]
    print(f'img4.shape={img4.shape}')#img4.shape=torch.Size([4, 798, 798])

    #
    img5=img4.permute(1,2,0)
    print(f'img5.shape{img5.shape}')

    feature_map=img5[:,:,2].detach().numpy()
    plt.imshow(feature_map)
    plt.show()




if __name__ == '__main__':
    f01()