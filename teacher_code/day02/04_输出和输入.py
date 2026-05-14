

a = 1
b = 2
c = 3
d = 4
print(a, b, c)
print(d, '你好！')

# end 是 print函数方法的特殊的参数
# end的值 表示一行最后的符号是什么
# ''两个引号中间啥也没有 ，是字符串、特殊的空字符串
# end=XX 该行以XX结尾
# end='' 表示以空字符串结尾，所以不换行了
# 本来默认结尾是换行符号是 \n
print(a, end='')
print('*')
# print(a) ==> print(a, end='\n')

print(a, end='@@@@') # 1@@@@
# \n 就是换行符
print('\n你\n好\n！')
# \t 是 tab键输出的一个类似4个空格位置的大空格
print('\t中国！')

# todo ''  \n  \t

# todo 格式化输出
num = 9527
name = '刘海柱'
age = 18
high = 1.78
# 需求：我的学号是 XXXX，我叫XXX，年龄XX，身高XX
print(
    '我的学号是%d，我叫%s，年龄%d，身高%f' % (num, name, age, high)
)

""" print('%d %f %s %s' % (int, float, str1, str2))
%d 表示 整数int；和int()函数一样 能够做类型转换
%f 表示 小数float；和float()函数一样 能够做类型转换
%s 表示 字符串str；和str()函数一样 能够做类型转换
"""

a = '我的学号是%d，我叫%s，年龄%d，身高%f'
print(a)

b = '我的学号是%d，我叫%s，年龄%d，身高%f' % (num, name, age, high)
print(b)

print(
    a % (num, name, age, high)
)

# todo 格式化输出的第二种方式
# format函数： '{}'.format(x) # x可以是任意类型
c = '我叫{}'
print(c.format('刘海柱'))
d = '我叫{}'.format('刘海柱2')
print(d)
print('这是字符串还是数字啊？{}'.format(555))

# todo 格式化输出的第3种方式
# f'{变量名1}, {变量名2}'
name = '刘海柱3'
age = 19
print(f'我叫{name}，我的年龄是{age}')


# todo input输入
# 1. 能够在终端接收键盘的输入，以回车结束
# 2. 暂停程序、暂停在input()函数这里
# 3. 接收的键盘输入类型一定是字符串！
# 模拟输入密码
password = input('请输入你的密码，以回车结束：')
print(password, type(password))