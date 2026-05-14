"""
二分查找，递归版
概述：
    属于查找类算法，相对效率较高，时间复杂度为O(log n)
前提：
    列表必须是有序的
原理：假设列表是升序的
    1.比较要查找的元素和 列表的中值，如果一样就返回True，程序结束
    2.如果要查找的元素比 中值小，去前半段查找
    3.如果要查找的元素比 中值大，去后半段找
    4.重复上述动作，直至找完，如果都找完，还找不到，返回False
"""

def binary_search_recursion(my_list,target):
    '''

    :param my_list: 待查找的列表
    :param target: 要查找的元素
    :return: True，False
    '''
    n=len(my_list)
    #2.判断列表为空
    if n==0:
        return False
    #3.获取列表的中值（的索引）
    mid=n//2
    #4.比较要查找的元素和中值
    if my_list[mid]==target:
        return True
    elif target<my_list[mid]:
        #5.如果要查找的元素比中值小，去前半段找，递归调用
        return binary_search_recursion(my_list[:mid],target)
    else:
        #6.查找的元素比中值大，去后半段查找，递归调用
        return binary_search_recursion(my_list[mid+1:],target)


if __name__ == '__main__':
    my_list=[1,2,9,44,56,69,77,99]
    print(binary_search_recursion(my_list,19))
    print(binary_search_recursion(my_list,99))