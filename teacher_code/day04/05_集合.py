
# 空集合
a = set()
print(a, type(a)) # set() <class 'set'>

# 定义非空的集合 todo 集合能自动去重
a = {1,2,3,4,4,4,4}
print(a) # {1, 2, 3, 4}

# 向集合的右边队尾添加元素
a = {1, 2, 3, 4}
a.add(5) # 集合.add(新元素)
print(a)
a.add(5) # 重复添加、自动去重
print(a)
a.add(6)
print(a)

# 删除指定的元素
a.remove(2)
print(a) # {1, 3, 4, 5, 6}

# 从队头取出元素
ret = a.pop()
print(ret) # 把最左边的元素拿出来了
print(a) # 原来的集合中，该元素不存在了


# todo 列表、元组、集合 互相转换
# todo 列表、元组  转 集合 的时候，会自动去重！
# 列表可以存储重复元素的，可以利用集合对他进行去重

# 列表转集合
a_list = [1,1,1,2,2,2,2,3,3]
ret_set = set(a_list) # 转换为集合，目的是去重
print(ret_set) # {1, 2, 3}
print('*'*10)

# 元组转集合
a_tuple = (1, 2, 3)
print(set(a_tuple)) # {1, 2, 3}
print('*'*10)

# 集合转列表
print(list(ret_set)) # 再转换为列表 [1, 2, 3]
# 元组转列表
print(list(a_tuple)) # [1, 2, 3]
print('*'*10)

# 列表转元组
new_tuple = tuple(a_list)
print(new_tuple)

# 集合转元组
new_tuple = tuple(ret_set)
print(new_tuple)

