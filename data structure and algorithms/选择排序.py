"""
选择排序介绍
原理：
    每轮都假设该轮最前边的哪个元素值为最小值，然后去剩下的元素列表中找真正的最小值，最终交换即可，本轮就找到了本轮的最小值，重复即可

    第一轮，假设1=0位置的元素是最小值，然后用min_index记录他的索引，然后去剩下所有元素中找真正的最小值，找到后就用min_index记录，最终判断i
    第一轮完毕后，最小值就在最小索引处
流程：
    第几轮         该轮比较的总次数            公式
    1               4                       索引0和1，2，3，4比较
    2               3                       索引1 和 2，3，4
    3               2                       索引2和 3，4比较
    4               1

要点：
    1.比较的总轮数。 列表长度-1
    2.每轮比较的总次数  i+1~n




"""

def select_sort(my_list):
    n = len(my_list)
    #2.外循环，控制比较的轮数
    for i in range(n-1):
        #3.定义变量min_index，记录住本轮真正最小值的索引
        min_index=i
        #4.内循环，控制每轮比较的次数
        for j in range(i+1,n):
            #5.具体的比较过程，索引min_index（初始值为i）和索引j比较
            if my_list[j]<my_list[min_index]:
                #记录最值得索引
                min_index=j
            #6.走到这里，说明本轮已经找到了最小值，判断，并交换
        if min_index!=i:
            my_list[i],my_list[min_index]=my_list[min_index],my_list[i]

if __name__ == '__main__':
    my_list=[5,3,6,7,2]
    select_sort(my_list)
    print(my_list)
    n=len(my_list)
    print('*'*12)
    for i in range(n-1):
        print(i)
        for j in range(i+1,n):
            print(j)
        print('----')
