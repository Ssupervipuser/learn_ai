import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.preprocessing import StandardScaler
def dm01():
    data=pd.read_csv('../data/train.csv')
    # print(data.head())
    x=data[['Pclass','Sex','Age']]
    y=data['Survived']

    avg=x['Age'].mean()
    x['Age']=x['Age'].fillna(avg)

    x=pd.get_dummies(x,columns=['Sex'])
    # x.drop(['Sex_female'],axis=1,inplace=True)
    x.drop(['Sex_female'],axis='columns',inplace=True)
    print(x.head(),type(x))

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=22)
    #3.特征工程


    #4.模型训练
    model=DecisionTreeClassifier()
    model.fit(x_train,y_train)

    #5.模型预测
    y_predict=model.predict(x_test)

    print(f'预测结果:',y_predict)

    #6.模型评估
    print(f'准确率：',model.score(x_test,y_test))
    print(f'分类报告：',classification_report(y_test,y_predict))

    #7.绘图
    plt.figure(figsize=(80,40),dpi=100)
    #决策树分类器，填充颜色，最大层数
    plot_tree(model,filled=True,max_depth=10)

    plt.savefig('cart.png')
    plt.show()


if __name__ == '__main__':
    dm01()