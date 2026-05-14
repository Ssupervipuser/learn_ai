# todo 组包：把多个值指向一个变量名
a = 1,2,3
print(a, type(a)) # (1, 2, 3) <class 'tuple'>

# todo 拆包：多个变量名依次指向每一个对象
a,b,c = (1,2,3)
print(a, b, c) # 1 2 3

# a, b = (1,2,3)
# print(a, b)

# 组包的示例
def func():
    return 1, 2
ret = func()
print(ret) # (1, 2)

# 拆包的示例
def func():
    return 1, 2
a, b = func()
print(a, b) # 1 2


# todo 先组包再拆包
# 先执行右边： 1,2,3 作为整体再去赋值 —— 组包
# 再执行等号和左边：a,b,c = 整体 —— 拆包
a, b, c = 1, 2, 3
print(a, b, c)

# 组包+拆包示例：两个变量交换值
a = 1
b = 2
a, b = b, a
print(a, b) # 2 1

# 下边代码的过程：
# 1. 1,2 组包
# 2. a,b= 拆包
# 3. b,a 组包
# 4. a,b= 拆包
a, b = 1, 2
# 先等候右边，再等号和左边
a, b = b, a

# 遍历字典的kv时，也发生了拆包
dt = {
    'name': 'lili',
    'age': 19
}
for itme in dt.items():
    print(itme) # ('age', 19)
for k, v in dt.items():
    print(k, v)

def func3(*args):
    # todo *args 元组不定长参数
    # 可以接收任意个参数，不指定参数名（形参）
    # *args 把所有参数展开
    print(*args) # 1 2 3 # todo拆包
    # args 所有参数按顺序放到元组中
    print(args) # (1, 2, 3)
    print(type(args)) # <class 'tuple'>
func3(1, 2, 3)

# todo 拓展： *a 对a进行拆包，a实际被定义的时候进行了组包
a = 1,2,3 # 组包
print(a) # (1,2,3)
print(*a) # 1 2 3 # 拆包