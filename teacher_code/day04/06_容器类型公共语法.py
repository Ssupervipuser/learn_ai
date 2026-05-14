
a_dict = {'a':1, 'b':2}
print(len(a_dict))

print(max(a_dict)) # 对key进行求最大值
# print(sum(a_dict)) # 对key进行累加求和

# 对字典的所有key进行遍历，返回key的下标和key的字面量
for i in enumerate(a_dict):
    print(i, type(i))
for i,k in enumerate(a_dict):
    print(i, k)

for i in enumerate({1, 2, 3, 4}):
    print(i)
# todo 会把集合中的值，按大小进行排序，逐一返回序号和对应的值
# 注意：这个序号不是下标！
for 序号,v in enumerate({1, 2, 4, 3}):
    print(序号,v)
# enumerate({1, 2, 4, 3}) ==> 不是集合！会把集合中元素排序，返回有顺序的可迭代对象

# del 删除列表、字典中的元素
# 按下标删除列表中的元素
a_list = [1,2,3,4]
del a_list[0]
print(a_list)

# 按key删除字典中的键值对
a_dict = {'a':1, 'b':2}
del a_dict['a']
print(a_dict)


# todo 切片操作 是根据下标来进行的！ 所以只能对 列表、元组、字符串进行切片



# 运算符操作
print((1,2)+(3,)) # (1, 2, 3)
print([1,2]*5)

a_str = '1223'
b_list = [1,2,3]
c_tuple = (1,2,3)
d_dict = {'a':1, 'b':2}


if '1' in a_str:
    print('存在')

print(1 in b_list)
print(3 not in c_tuple)
print('a' in d_dict)

# todo 判断某个值是否在字典中，判断的是key键
print(1 in d_dict) # False
