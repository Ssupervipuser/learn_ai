
"""多行注释
"""

# 多行字符串的定义
my_str = """多行字符串
1
2
"""
print(my_str)

my_str = '零一二三四五'
# 可以通过下标去取字符，但不能修改字符！
print(my_str[-1])
# my_str[0] = 'O' # 报错

print(my_str[::-1]) # 切片，倒排
print(my_str[-2:-4:-1]) # 四三

# 字符串的格式化
print(
    '姓名：%s，年龄：%d，性别：%s，身高：%.1f'
    % ('张三', 28, '女', 2.78)
)

# 不推荐这么写！这是多个变量一起按顺序进行定义、赋值
name, age, gender, high = '张三', 28, '女', 2.78
print(
    f'姓名：{name}，年龄：{age}，性别：{gender}，身高：{high}'
)

print(
    '姓名：{name}，年龄：{age}，性别：{gender}，身高：{high}'.format(
        age=18, gender='女', high=2.78, name='张三'
    )
)

print(
    '姓名：{}，年龄：{}，性别：{}，身高：{}'.format(
        '张三', 18, '女', 2.78
    )
)


# todo 查找字符串中指定的字符串
my_str = '你好AI大模型'
# 你要找的字符(串)的起始位置的下标
# 找不到就返回 -1
ret = my_str.find('你好')
print(ret)
ret = my_str.find('BCD')
print(ret)

# '被查找的原字符串'.find('要找的字符串', 查找范围起始下标, 查找范围结束下标)
# 查找范围的起始、结束下标，只能从左往右
ret = my_str.find('模', 0, 2)
print(ret)

# todo 替换字符串中的指定内容
my_str = '你好AI大模型你好AI大模型你好AI大模型'
new_str = my_str.replace('你', '我') # 全部替换！
print(new_str)

# 指定替换的次数！
new_str2 = my_str.replace('你', '我', 1)
print(new_str2, my_str)

# 指定替换的次数！
new_str2 = my_str.replace('你', '我', 2)
print(new_str2, my_str)


# todo 字符串分割
my_str = '你好AI大模型，你好AI大模型，你好AI大模型'
result_list = my_str.split('，')
print(result_list) # ['你好AI大模型', '你好AI大模型', '你好AI大模型']

# todo 拼接字符串
print('aaa'+'bbb')
ret = ''
for i_str in result_list:
    print(i_str)
    # 用 + 号 拼接字符串
    ret = ret + i_str
print(ret)

# result_list = ['你好AI大模型', '你好AI大模型', '你好AI大模型']
# todo 拼接后的字符串 =字符串A.join(字符串构成的列表)
# todo 用字符串A连接列表中的所有字符串
ret_str = '，'.join(result_list)
print(ret_str)
# 你好AI大模型，你好AI大模型，你好AI大模型

# 用+号连接每一个字符串，返回新的字符串
my_str_list = ['a', 'b', 'c']
ret_str = '+'.join(my_str_list)
print(ret_str) # a+b+c

# 需求：把列表中的字符串拼接起来
my_str_list = ['a', 'b', 'c']
# 用就用空字符串''拼接！
ret_str = ''.join(my_str_list)
print(ret_str) # abc

""" 总结规律、和列表对比 
返回下标或-1 = 字符串.find('目标字符串', 起始下标, 结束下标)
新字符串 = 字符串.replace('被替换的字符串', '新内容', 替换次数)
字符串构成的列表 = 字符串.split('分隔符字符串')
新字符串 = 分隔符字符串.join(字符串构成的列表)
新字符串 = ''.join(字符串构成的列表)

1. 原字符串无论调用什么样的方法函数，都不会被改变！这和列表不一样
2. 字符串方法都有返回值！这和列表不一样

print([1,2,3] + [4,5,6])
print('abc'+'def')
"""


a = [1,2,3]
print(str(a), type(str(a))) # [1, 2, 3] <class 'str'>

a_str = str(a)
print(a_str, type(a_str))

ret = eval(a_str)
print(ret, type(ret)) # [1, 2, 3] <class 'list'>

# todo eval(str) 能够把字符串转换成其他类型：长的像的类型
ret = eval('(1,2,3)')
print(ret, type(ret)) # (1, 2, 3) <class 'tuple'>

ret = eval('9527')
print(ret, type(ret)) # 9527 <class 'int'>

ret = eval('{"a": 123}')
print(ret, type(ret)) # {'a': 123} <class 'dict'>
