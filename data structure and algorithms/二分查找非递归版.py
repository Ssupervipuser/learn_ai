def binary_search(my_list,target):
    #1.定义变量，start，end分别表示列表的开始和 结束索引
    start=0
    end=len(my_list)-1

    #2.循环查找，只要条件满足就一直找
    while start<=end:
        #3.计算中间值的索引
        mid=(start+end)//2
        #4.比较要查找的元素 和中值
        if my_list[mid]==target:
            return True
        elif target<my_list[mid]:
            #5.如果要查找的元素比中值小，去前半段找。修改end的值
            end=mid-1
        elif my_list[mid]<target:
            start=mid+1
    return False




if __name__ == '__main__':
    my_list = [1, 2, 9, 44, 56, 69, 77, 99]
    print(binary_search(my_list, 19))
    print(binary_search(my_list, 99))