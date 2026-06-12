from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler


def dm01():
    # 1.准备数据
    data = load_iris()

    # 2.分割数据集
    x_train, x_test, y_trian, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=10)
    # 3预处理标准化数据
    transfer = StandardScaler()
    # 4.训练转化数据（制定数据标准规则）
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 5.创建模型对象
    model = KNeighborsClassifier()
    param_grid = {"n_neighbors": [1, 3, 5, 7, 9, 11]}
    model = GridSearchCV(estimator=model, param_grid=param_grid, cv=4)
    # 6.训练模型
    model.fit(x_train, y_trian)

    print(model.best_score_)
    print(model.best_params_)
    print(model.best_estimator_)
    print(model.cv_results_)

    model = KNeighborsClassifier(n_neighbors=7)
    model.fit(x_train, y_trian)

    # 7.打分
    score = model.score(x_test, y_test)
    print("正确率：", score)


from sklearn.pipeline import Pipeline


def dm02():
    data = load_iris()

    # 2.分割数据集
    x_train, x_test, y_trian, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=10)
    # 1.划分训练集和测试集（假设x_train,x_test,y_train,y_test已定义）
    # 2.定义Pipeline(管道)
    # 使用Pipeline将标谁化与模型结合，确保交叉验证时，
    # 只有训练集用于拟合Scaler,验证集使用相同的转换，防止数据泄漏。
    pipe = Pipeline([
        ('scaler',StandardScaler()),
        ('knn', KNeighborsClassifier())
    ])
    # 3.定义baram_dict
    # 字典中的键名需为”管道步名一参数名”
    param_dict ={'knn__n_neighbors':[3, 5, 7, 9]}
    # 4.初始化GridSearchCV
    estimator=GridSearchCV(pipe, param_dict, cv=4)
    # 5.训练模型
    estimator.fit(x_train, y_trian)
    # 6.获取结果
    print("最佳参数：",estimator.best_params_)
    print("最佳模型：",estimator.best_estimator_)

    if __name__ == '__main__':
        dm02()
