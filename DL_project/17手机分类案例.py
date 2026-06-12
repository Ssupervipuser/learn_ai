import numpy as np
import pandas as pd
import torch

from sklearn.model_selection import train_test_split

from torch.utils.data import TensorDataset


def create_datasete():
    data=pd.read_csv('../data/手机价格预测.csv')
    print(data.head())
    x,y=data.iloc[:,:-1],data.iloc[:,-1]

    #数据类型转换
    x=np.array(x).astype(np.float32)
    y=np.array(y).astype(np.int64)
    #数据集划分
    #1.分成训练集和临时集
    x_trian,x_temp,y_train,y_temp=train_test_split(x,y,test_size=0.2,random_state=42,shuffle=True,stratify=y)
    #2.验证集和测试集
    x_val,x_test,y_val,y_test=train_test_split(x_temp,y_temp,test_size=0.5,random_state=42,shuffle=True,stratify=y_temp)

    #创建训练集对象，验证集对象，测试集对象
    train_dataset=TensorDataset(torch.from_numpy(x_trian),torch.from_numpy(y_train))
    val_dataset=TensorDataset(torch.from_numpy(x_val),torch.from_numpy(y_val))
    test_dataset=TensorDataset(torch.from_numpy(x_test),torch.from_numpy(y_test))

    #类别总数
    class_=np.unique(y)
    class_number=len(class_)
    return train_dataset,val_dataset,test_dataset,x_trian.shape[1],class_number





if __name__ == '__main__':
    create_datasete()