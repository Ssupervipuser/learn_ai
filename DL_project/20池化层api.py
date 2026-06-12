import torch
import torch.nn as nn


# 演示单通道池化
def f01():
    # 创建一个单通道3*3的二维矩阵
    inputs = torch.tensor([
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ])

    # 创建最大池化层
    pool1 = nn.MaxPool2d(kernel_size=2, stride=1, padding=0)
    out = pool1(inputs)
    print(out, out.shape)
    # 创建平均池化层
    pool2 = nn.AvgPool2d(kernel_size=2, stride=1, padding=0)
    out1 = pool2(inputs)
    print(out1, out1.shape)


def f02():
    # 创建一个3通道3*3的二维矩阵
    inputs = torch.tensor([

        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]
        ],
        [
            [11, 22, 33],
            [44, 55, 66],
            [77, 88, 99]
        ]

    ])
    # 创建最大池化层
    pool1 = nn.MaxPool2d(kernel_size=2, stride=1, padding=0)
    out = pool1(inputs)
    print(out, out.shape)
    # 创建平均池化层
    pool2 = nn.AvgPool2d(kernel_size=2, stride=1, padding=0)
    out1 = pool2(inputs)
    print(out1, out1.shape)


if __name__ == '__main__':
    # f01()
    f02()
