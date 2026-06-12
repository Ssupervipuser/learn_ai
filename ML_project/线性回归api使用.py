from sklearn.linear_model import LinearRegression

def demo01():
    #准备数据
    x=[[160],[166],[172],[174],[180]]
    y=[56.3,60.6,65.1,68.5,75]
    #创建模型对象
    model=LinearRegression()
    #训练模型
    model.fit(x,y)
    print('weight:',model.coef_)
    print('bias:',model.intercept_)

    #模型预测
    res=model.predict([[176]])
    print('预测结果为：',res)



if __name__ == '__main__':
    demo01()