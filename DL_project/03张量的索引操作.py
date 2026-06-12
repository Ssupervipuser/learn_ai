"""

"""
import torch

torch.manual_seed(24)
t1=torch.randint(1,10,(5,5))
print(f't1:{t1}')
print('-'*20)

#todo 1.简单行列索引  格式：张良对象[行，列]
print(t1[1])
print(t1[1,:])
print(t1[:,2])
print('-'*20)


#todo 2.列表索引 格式[[行1,行2],[列1,列2]]

# 返回（1，2），（3，4）位置的元素
print(t1[1,3],[2,4])

#获取0，1行的1，2列共4个元素，广播机制
print(t1[[[0],[1]],[1,2]])

#todo 3.范围索引

#前3行，前2列
print(t1[:3,:2])

#第2行到最后一行，前两列的数据
print(t1[1:,:2])
print('-'*20)
#所有奇数行，偶数列
print(t1[1::2,::2])
print('-'*20)

#todo 4.布尔索引
#第3列，大于5的行数据
# print(t1[torch.tensor([True,False,False,True,True]),:])
print(t1[t1[:,2]>5])


#todo 5.多维索引
t2=torch.randint(1,10,(2,3,4))
print(f't2:{t2}')
"""
[
        [        
        [3, 4, 6, 5],
         [8, 8, 8, 3],
         [4, 9, 6, 7]
         ],

        [
        [2, 8, 8, 5],
         [6, 4, 2, 2],
         [2, 7, 9, 4]
        ]
]
"""
#获取0轴上的第一个数据
print(t2[0,:,:])

#获取1周上的第1个数据
print(t2[:,0,:])

#获取2轴上的第一个数据
print(t2[:,:,0])