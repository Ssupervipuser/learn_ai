my_list = [1,2,3,4,5,6,7,8,9,10]
def fun(i):
    return i%2==1

my_iterable=filter(fun,my_list)
newlist=list(my_iterable)
print(newlist)

my_iterable=filter(lambda x: x%2==1,my_list)
print(list(my_iterable))

#根据条件函数，将条件映射到每一个要处理的数据中，处理之后返回新的数据

lst=list(range(10))
ret=list(map(lambda x:x**2,lst))
print(ret)

#todo round函数练习
#把里表中的所有数字，全部按四舍五入编程3位小数
lst=[0.2135,1.64684,0.12124856]

lst2=[round(i,3) for i in lst]
print(lst2)

lst2=list(map(lambda i :round(i,3),lst))
print(lst2)