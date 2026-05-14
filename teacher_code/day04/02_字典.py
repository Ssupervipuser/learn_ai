my_dict = {} # 空字典
my_dict = dict() # 空字典
my_dict = {
    'name': 'smart',
    'age': 18,
    'city': '上海'
}
print(type(my_dict)) # <class 'dict'>

# 通过key键 取value值
print(my_dict['name'])
print(my_dict.get('name'))
print('*'*5)

# 没有gender这个k，所以会报错！
# print(my_dict['gender'])

# print(my_dict[city]) # 这也是个错误！

# 根据key去修改value的值
my_dict['age'] = 91
print(my_dict)

# 根据键key，取出value值，取出之后原字典就没有这个键值对了！
ret = my_dict.pop('age')
print(ret) # dict.pop(key) 返回 和 k对应的 v
print(my_dict) # 原字典中就没有这个kv了

print('*'*5)
# 直接遍历字典，逐一返回key键
for key in my_dict:
    print(key)

# 通过对 dict.values() 进行遍历，逐一获得每个 v
for value in my_dict.values():
    print(value)

# dict_values(['smart', '上海'])
print(my_dict.values())

# 通过对 dict.items() 进行遍历，逐一获得每对 kv
for k,v in my_dict.items():
    print(k, v)