import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


def dm01():
    data=pd.read_csv('../data/train.csv')
    print(data.head())
    x=data[['Pclass','Sex','Age']]
    y=data['Survived']

    avg=x['Age'].mean()
    x['Age']=x['Age'].fillna(avg)
    x=pd.get_dummies(x,columns=['Sex'])
    # x.drop(['Sex_female'],axis=1,inplace=True)
    x.drop(['Sex_female'],axis='columns',inplace=True)
    print(x.head(),type(x))




if __name__ == '__main__':
    dm01()