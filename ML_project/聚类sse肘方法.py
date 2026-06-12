from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score, calinski_harabasz_score

def dm01():
    x, y = make_blobs(n_samples=1000,
                      n_features=2,
                      centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
                      cluster_std=[0.4, 0.2, 0.2, 0.2],
                      random_state=22)

    # 定义sse列表，记录每个K值得sse值
    sse = []

    # for循环遍历，获取每个K值，计算其对应的sse值，并且添加到列表中
    for k in range(1, 100):
        # 创建Kmeans对象
        #           簇的数量        最大迭代次数
        model = KMeans(n_clusters=k, max_iter=100, random_state=22)
        model.fit(x)

        # 获取每个簇的sse值
        sse_value = model.inertia_
        sse.append(sse_value)

    plt.figure(figsize=(20, 10))
    plt.xticks(range(0, 100, 3))
    plt.xlabel("k")
    plt.ylabel('sse')
    plt.grid()
    plt.plot(range(1, 100), sse)
    plt.show()

#1、定义函数 演示 SC轮廓系数法

def dm02_sc():
    #定义sse列表，记录：每个K值的SSE值
    sc_list = []
    #1、生成数据集
    x,y= make_blobs(
        n_samples=1000,
        n_features=2,
        centers=[[-1,-1],[0,0],[1,1],[2,2]],
        cluster_std=[0.4,0.2,0.2,0.2],
        random_state=23
    )

    #2.for循环遍历，获取每个K值，计算其对应的sse值 ，并且添加到sse_list中
    for k in range(2,100):          #todo 注意！！！ SC簇间 所以 K至少是2
        #2.1创建Kmean对象
        #参1：簇的数量  参2：最大迭代次数  参3：固定随机种子
        model=KMeans(n_clusters=k,max_iter=100,random_state=23)
        #2.2训练
        model.fit(x)
        #2.3模型预测
        y_pred=model.predict(x)
        #2.4获取每个簇的sc值  【更改】
        sc_value=silhouette_score(x,y_pred)

        #2.5将每个k的对应的sse的值，添加到sse_list列表中  找拐点
        sc_list.append(sc_value)
    #3.绘制SC曲线 -》数据可视化
    # print(sse_list)
    #3.1创建画布
    plt.figure(figsize=(20,10))
    plt.title("sc value")
    #3.2x轴刻度
    plt.xticks(range(0,100,3))

    # 3.3 添加x轴和y轴标签
    plt.xlabel("k")
    plt.ylabel("sc_value")
    plt.grid()
    #or- : color =r     marker='o' linestyle='-'
    # plt.plot(range(1,100),sse_list,'or-')
    plt.plot(range(2, 100), sc_list)
    plt.show()


def dm03_ch():
    #定义sse列表，记录：每个K值的SSE值
    ch_list = []
    #1、生成数据集
    x,y= make_blobs(
        n_samples=1000,
        n_features=2,
        centers=[[-1,-1],[0,0],[1,1],[2,2]],
        cluster_std=[0.4,0.2,0.2,0.2],
        random_state=23
    )

    for k in  range(2,100):
        model=KMeans(n_clusters=k,max_iter=100,random_state=23)
        model.fit(x)
        y_pred=model.predict(x)
        #ch在调用过程中，要用到预测值
        ch_value=calinski_harabasz_score(x,y_pred)
        ch_list.append(ch_value)

    #3.绘制ch曲线 -》数据可视化
    # print(sse_list)
    #3.1创建画布
    plt.figure(figsize=(20,10))
    plt.title("ch value")
    #3.2x轴刻度
    plt.xticks(range(0,100,3))

    # 3.3 添加x轴和y轴标签
    plt.xlabel("k")
    plt.ylabel("ch_value")
    plt.grid()
    #or- : color =r     marker='o' linestyle='-'
    # plt.plot(range(1,100),sse_list,'or-')
    plt.plot(range(2, 100), ch_list)
    plt.show()




if __name__ == '__main__':

    # dm02_sc()

    dm03_ch()
