
# todo 1. 比较运算符 != 、 == 、 > ....a = True # bool
a = 1
b = 1

#  a==b a和b进行比较，看两者是否相等，返回的是真True或假False
print(a==b) # True
print(type(a==b)) # <class 'bool'>
# a==b 是个bool布尔类型

c = 1
d = 1
print(c==d)
print(1==1)

# False和0进行比较，如果二者相等就返回True，不等就返回False
e = False
f = 0
print(e==0) # True

# 变量1 != 变量2
# 表示 变量1和变量2是否相等，如果不等返回True，如果相等返回False
g = 1
h = 2
print(g!=h) # True
# 因为55不等于66，所以返回True
print(55!=66)
# != 不等于

print(4>6) # False

print('*'*10)

# todo 2. 逻辑运算符 and or not
print(True and False) # False
print(5>3 and 5>6) # False

print(5>3 or 5>6) # True

print(not 5>3) # False
print(not(5>3)) # False
print(not (5>3)) # False
print(False and (True or False)) # False
print(False or False) # False

# todo 3. 逻辑运算符 or 比较运算符 连接的变量、整体叫做条件表达式
# todo 条件表达式 ，打印它，一定输出 True 或 False
# todo 条件表达式作用：作为判断和循环的条件
# todo 条件表达式，先比较、后逻辑
# todo 先not 再and 最后or

print(
    5==5 or 5>=6 and 5!=6
)
a = 5==5 # 定义a这个变量 是 5==5, 5==5是条件表达式、返回True
print(a, '这一行在这里')
#  True or False and True
print(True or False and True) # True

print(
    (
        (5 == 5) or (5 >= 6)
    ) and (5 != 6)
)

# todo 作业2：设计一个代码，证明 not and or 的先后执行顺序
ret = False or True and not False
# 提示：可以两两判断得到先后顺序