'''
案例：按时网格搜索和交叉验证

交叉验证解释
    原理：
        把数据分成n份，列入分成4份
        第1次，把第1份数据作为验证集（测试集），其他作为训练集，训练模型，模型预测。 获取准确率-》准确率1
        第2次，把第2份数据作为验证集（测试集），其他作为训练集，训练模型，模型预测。 获取准确率-》准确率2
        第3次，把第3份数据作为验证集（测试集），其他作为训练集，训练模型，模型预测。 获取准确率-》准确率3
        第4次，把第4份数据作为验证集（测试集），其他作为训练集，训练模型，模型预测。 获取准确率-》准确率4

        假设第4次最好，则用全部数据（训练集+测试集）训练模型，再次用第4次的测试集对模型测试
    目的：
    为了让模型的最终结果更准确

网格搜索
    目的
    寻找最优超参数
    原理：
        接收超参可能出现的之，然后针对于超参的每个值，进行交叉验证，获取到最有超参组合
    超参数：
        需要用户手动录得数据，不哦那个的超参会影响模型结果

大白话：网络搜索+交叉验证，本质是使用GridSearchCV这个api，他会帮我们寻找最优超参（参考）
'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


#1.获取数据集
iris_data = load_iris()

#2.数据预处理
x_train,x_test,y_train,y_test=train_test_split(iris_data.data, iris_data.target,test_size=0.2,random_state=20)

#3.特征工程
#3.1创建标准化对象
transfer=StandardScaler()
#3.2对训练集和测试机的特征数据进行标准化
x_train=transfer.fit_transform(x_train)
x_test=transfer.transform(x_test)

#4.模型训练
#1.创建Knn分类对象
model=KNeighborsClassifier()
#2.使用网格搜索，指定参数范围
param_grid={'n_neighbors':range(1,11)}
#3.具体的网格搜索+交叉验证
#                      要计算最优超参的模型对象 该模型超参可能出现的值    交叉验证的折数， 这里是4*10=40
estimator=GridSearchCV(estimator=model,param_grid=param_grid,cv=4)

#具体训练
estimator.fit(x_train,y_train)
#5.模型评估

print(f'最优评分{estimator.best_score_}')
print(f'最优超参组合{estimator.best_params_}')
print(f'最优的估计器对象：{estimator.best_estimator_}')
print(f'具体的验证结果{estimator.cv_results_}')

#5. 得到最有模型后，对模型重新预测

estimator=KNeighborsClassifier(n_neighbors=6)
estimator.fit(x_train,y_train)
y_pre=estimator.predict(x_test)
print(f'准确率{accuracy_score(y_test,y_pre)}')






