import numpy as np
import matplotlib.pyplot as plt
import torch

def f01():
    #0表示全黑，HWC H:高 W:宽 C:通道
    img1=np.zeros((200,200,3))
    plt.imshow(img1)
    plt.show()

def f02():
    img2=torch.full(size=(200,200,3),fill_value=255)
    plt.imshow(img2)
    # plt.axis('off')
    plt.show()


def f03():
    img=plt.imread('img_gril.jpg')
    print(img.shape)#默认通道是BGR
    #颜色顺序转换成RGB
    img=img[:,:,::-1]
    plt.imshow(img)
    plt.imsave('img_new_g.jpg',img)
    plt.show()

if __name__ == '__main__':
    # f01()
    # f02()
    f03()