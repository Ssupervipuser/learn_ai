list3=[i for i in range(10)]
print(list3)

#使用推导式的方式，转换成 元组，集合
my_tuple=tuple(i for i in list3)
print(my_tuple)
print(type(my_tuple))

my_set=set(i for i in list3)
print(my_set)
print(type(my_set))