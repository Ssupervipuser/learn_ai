# from copy import copy # 浅拷贝
# from copy import deepcopy # 深拷贝
from copy import copy, deepcopy

print('*'*10, '可变类型浅拷贝,id变')
# 可变类型浅拷贝的现象：深层的元素发生改变，都变
a = [1,2,3]
b = [11,22,33]

lst1 = [a, b]
# lst1 ==> [[1,2,3], [11,22,33]]
lst2 = copy(lst1)

print(id(lst1), lst1)
print(id(lst2), lst2)
a[0] = 100
print(id(lst1), lst1)
print(id(lst2), lst2)

print('*'*10, '不可变类型浅拷贝,id不变')
a = (1,2,3)
b = (11,22,33)
tup1 = (a, b)
tup2 = copy(tup1)
print(id(tup1), tup1)
print(id(tup2), tup2)

# todo 用深拷贝！
print('*'*10, '可变类型深拷贝, id变')
# 可变类型深拷贝的现象：深层的元素发生改变，深拷贝出来的对象不变
a = [1,2,3]
b = [11,22,33]

lst1 = [a, b]
lst2 = deepcopy(lst1)

print(id(lst1), lst1)
print(id(lst2), lst2)
a[0] = 100
print(id(lst1), lst1)
print(id(lst2), lst2)

print('*'*10, '不可变类型深拷贝, id不变')
a = (1,2,3)
b = (11,22,33)
tup1 = (a, b)
tup2 = deepcopy(tup1)
print(id(tup1), tup1)
print(id(tup2), tup2)

"""
元组 tuple (a,) 、字符串 str 'abc' 、数值 int float bool(True False)
不可变类型，深浅拷贝，id都不变：
    不可变类型、深浅拷贝，复制的都是引用 
    tup2 = tup1
    tup2 = copy.copy(tup1)
    tup2 = copy.deepcopy(tup1)
    
列表 list [] 、集合 set() {a,} 、字典 dict {k:v,}
可变类型，深浅拷贝，id发生变化
    浅拷贝 只复制内存地址，原来的lst中的元素中的元素值发生变化，新的lst也跟着变化
    深拷贝 完全复制一份儿，和原来完全不相关

"""