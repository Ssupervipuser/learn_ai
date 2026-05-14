"""
插入排序介绍
    原理：
        1.首先设置一个分界值，通过该分界值将数组分成左右两个部分
        2.将大于或等于分界值的数据集中到数组右边， 小于分界值的数据集中到数组的左边
        此时，左边部分中个元素都小于或等于分界值，而右边部分个元素都大于或等于分界值

        3.然后，左边和右边的数据可以独立排序，对于左侧的数据，又可以取一个分界值
        4.重复上述过程，通过递归将作责部分拍好后，在递归排右边
"""


def quick_sort(my_list,start,end):
    """

    :param my_list:
    :param start: 0
    :param end: len(my_list)-1
    :return:
    """
    #核心细节，如果start>=end，递归结束，说明排序好了
    if start>=end:
        return

    #1.定义变量left 和right，分别表示分界值左，有的索引
    left=start
    right=end
    #2.定义变量mid，表示分界值，假设列表的起始值为分界值
    mid=my_list[start]
    #3.具体的查找过程，只要left比right小，就一直找
    while left<right:
        #4.把分界值右边比分界值小的数据放到分界值左边
        #循环操作，只要分界值右边的数据比分界值大，right-1，直至循环结束
        while my_list[right]>=mid and left<right:
            right=right-1
        #走到这里说明my_list[right]比分界值小，放左侧
        my_list[left]=my_list[right]
        #5.把分界值左边比分界值大的数据放到右边
        while my_list[left]<mid and left<right:
            left=left+1
        my_list[right]=my_list[left]
    #6.走到这里，循环结束，分界值的位置已经找到，赋值即可
    my_list[right]=mid
    #7.递归方式，处理分界值左侧的数据
    quick_sort(my_list,start,left-1)
    #8.递归方式，处理分界值右侧的数据
    quick_sort(my_list,right+1,end)


if __name__ == '__main__':
    my_list=[5,8,2,1,9,6,7,4]
    quick_sort(my_list, 0, len(my_list) - 1)
    print(my_list)