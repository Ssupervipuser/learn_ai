# todo for循环 可以遍历字符串、元组、字典、列表
my_str = '123456789'

# 遍历字符串
for i in my_str:
    # 把 my_str 这个字符串中每个字符都拿出来
    print(i) # 拿出来一个、打印输出一次
print('*'*10)
for i in my_str:
    pass # 过、啥也不干！
print('*'*10)
# 遍历字符串，跳过6不打印
for i in my_str:
    # 把 my_str 这个字符串中每个字符都拿出来
    if i != '6': # 逆向思维：不是6就打印！
        print(i) # 拿出来一个、打印输出一次
print('*'*10)
# 遍历字符串，打印到6(包括6)就不再打印了！
for i in my_str:
    # 把 my_str 这个字符串中每个字符都拿出来
    print(i)
    if i == '6':
        break
print('*'*10)
# 遍历字符串，跳过6不打印，要求用continue实现
for abc in my_str:
    # 把 my_str 这个字符串中每个字符都拿出来
    if abc == '6':
        continue
    print(abc)
print('*'*10)

for x in 'abcdefg':
    print(x)
    continue
else:
    print('这是for循环的else')
""" todo 
for循环和while不光在break、continue上是一样的用法
else的用法也是一样的
"""