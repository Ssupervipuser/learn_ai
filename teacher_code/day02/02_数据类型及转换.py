# int 整数


# float 浮点数、小数


# bool 布尔、真假值


# str "字符串"


age = '18' # str
# 此时 age是字符串str, 不能做加法！
# print( age + 1 )

# 把age从字符串str转换成整数int
# 同时定义一个新的变量 来存储转换后的值
age_int = int(age)
# int + 1 就不错了！
print(age_int + 1)
# 查看age_int的类型，已经就是 int 整数了 ！
print(type(age_int))

# age_float = age转换为小数之后的值
age_float = float(age)
# 此时输出 18.0 <class 'float'>
print(age_float, type(age_float))


# 将 int\float 转换为字符串
age_str_1 = str(age_int)
# 18 <class 'str'>
print(age_str_1, type(age_str_1))

age_str_2 = str(age_float)
# 18.0 <class 'str'>
print(age_str_2, type(age_str_2))

# 下边两行会报错！
# name_str = '刘海柱'
# print(float(name_str))


# todo 关于bool的具体值
bool_1 = True
print(int(bool_1)) # 输出 1
bool_2 = False
print(int(bool_2)) # 输出 0
# todo 其实 True 就是 1 ， False 就是 0