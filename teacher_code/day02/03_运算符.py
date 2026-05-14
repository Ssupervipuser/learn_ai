# 数值类型可以直接相加
print(1+2)

# 字符串相加 ==> 拼接字符串
print('1'+'2') # 输出 12

# 注意：除法 / 出现小数的时候 有精度问题
a = 10 # int 整数
b = 3 # int 整数
ret = a / b # float 浮点数、小数
print(ret) # 输出 3.3333333333333335

# // 除法取整
print(a // b) # 只保留整数 3

# % 除法取余数
print(a % b) # 余数是1

# 指数
print(2**3) # 表示 2的3次方


# todo 符合赋值预算
a = 1
b = 2
ret = a + b
print(ret) # 此时ret是 3

ret = ret + 1 # 此时等号右边ret是 3
# 结果是4 此时 ret是4
print(ret) # 输出、打印

# 等价于ret = ret + 1
ret += 1 # 让 ret再+1
print(ret) # ret 是 5

""" 对于 = 两边，先计算 = 右边，再计算 =和左边
ret -= 1 ==> ret = ret-1
ret %= 3 ==> ret = ret % 3
"""

a += b
# ==> a = a + b
# ==> a = 1 + 2
print(a) # 此时 a 就变成了 3

