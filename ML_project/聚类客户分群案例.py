import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score,calinski_harabasz_score


def dm01():
    data = pd.read_csv('../data/customers.csv')

    x = data.iloc[:, [3, 4]]
    # print(x)

    sse = []
    sc = []
    ch=[]
    for i in range(2, 11):
        km = KMeans(n_clusters=i, max_iter=100, random_state=22)
        y_pred = km.fit_predict(x)
        #inertia_->sse值
        sse.append(km.inertia_)
        sc.append(silhouette_score(x, y_pred))
        # ch.append(calinski_harabasz_score(x,y_pred))

    plt.plot(range(2, 11), sse)
    plt.title('sse')
    plt.grid()
    plt.show()

    plt.plot(range(2, 11), sc)
    plt.title('sc')
    plt.grid()
    plt.show()

    # plt.plot(range(2, 11), ch)
    # plt.title('ch')
    #
    # plt.grid()
    # plt.show()


def dm02():
    data = pd.read_csv('../data/customers.csv')

    x = data.iloc[:, [3, 4]]
    # 创建kmeans
    km = KMeans(n_clusters=5)
    y_pred = km.fit_predict(x)
    print(y_pred)
    # 可视化
    plt.scatter(x.values[y_pred == 0, 0], x.values[y_pred == 0, 1])
    plt.scatter(x.values[y_pred == 1, 0], x.values[y_pred == 1, 1])
    plt.scatter(x.values[y_pred == 2, 0], x.values[y_pred == 2, 1])
    plt.scatter(x.values[y_pred == 3, 0], x.values[y_pred == 3, 1])
    plt.scatter(x.values[y_pred == 4, 0], x.values[y_pred == 4, 1])
    plt.show()




    # 布尔索引测试
    list1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    arr1 = np.array(list1)
    # print(arr1[[True,False,True,False],0])y_pred=[0 0 1 1 2]
    y_pred = np.array(y_pred)
    # print(y_pred==0)


if __name__ == '__main__':
    dm01()
    # dm02()