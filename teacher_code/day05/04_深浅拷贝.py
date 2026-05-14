
# 浅拷贝 copy()函数： id变，但依旧指向原来的东西（对象）
# 运行的代码中，一切皆对象
# 计算机世界中，一切皆文件

lst1 = [1, 2, [3, 4]]
lst2 = lst1.copy() # todo 浅拷贝

print('list1: ', lst1, id(lst1))
print('list2: ', lst2, id(lst2))

lst1[2][0] = 5

print('list1: ', lst1, id(lst1))
print('list2: ', lst2, id(lst2))

# todo 浅拷贝会发生现象：
# todo 通过浅拷贝复制的新对象 id变了
# todo 原对象的值改变，新对象的值也跟着变

# lst3 = [1, 2, [3, 4]]
# print('list3: ', lst3, id(lst3))

print('*'*5)
# todo 深拷贝
from copy import deepcopy # 导包
# import random
lst1 = [1, 2, [3, 4]]
# 对list1进行深拷贝，返回新的list2
lst2 = deepcopy(lst1)
print('list1: ', lst1, id(lst1))
print('list2: ', lst2, id(lst2))

lst1[2][0] = 5 # 此时修改list1中的元素，list2的元素不变

print('list1: ', lst1, id(lst1))
print('list2: ', lst2, id(lst2))

# todo 通过copy.deepcopy(lst)函数 复制的对象
# todo id发生变化，原对象发生改变，新对象不跟着变

print('*'*5)
# todo 对比下边2组代码的运行结果，得到结论：就用深拷贝！
lst1 = [1, 2, [3, 4]]
lst2 = lst1.copy() # 浅拷贝 浅层 直接包含的元素
lst3 = deepcopy(lst1)
lst1[0] = 5
print(id(lst1), lst1)
print(id(lst2), lst2)
print(id(lst3), lst3)
print('*'*5)
lst1 = [1, 2, [3, 4]]
lst2 = lst1.copy() # 浅拷贝 浅层 直接包含的元素
lst3 = deepcopy(lst1)
lst1[2][0] = 5
print(id(lst1), lst1)
print(id(lst2), lst2)
print(id(lst3), lst3)



