"""
冒泡排序介绍：
原理：
    相邻元素两两比较，大的往后走，这样第一轮比较完毕后，最大值就在最大索引处
    重复此动作，直至排序完成

流程：假设一共5个元素
    第几轮（索引）         该轮比较的总次数            公式
    1                       4                   5-1-0=4
    2                       3                   5-1-1=3
    3                       2
    4                       1
要点：
    1.比较的总轮数        列表长度-1
    2.每轮比较的总次数      列表长度-1-论述的索引（从0开始）
    3.谁和谁比较         索引j和j+1 位置的元素比较
时间复杂度
    最优：
    最坏：
冒泡排序是稳定算法

"""

def bubble_sort(my_list):
    #1.获取列表的长度
    n=len(my_list)
    #2外循环控制比较的轮数
    for i in range(n-1):
        #3.内循环控制比较的总次数
        for j in range(n-1-i):
            if my_list[j]>my_list[j+1]:
                my_list[j],my_list[j+1]=my_list[j+1],my_list[j]

    return my_list



if __name__ == '__main__':
    my_list=[1,3,2,6,5,7]
    # print(bubble_sort(my_list))

for i in range(1,len(my_list)-1):
    print(i)

















