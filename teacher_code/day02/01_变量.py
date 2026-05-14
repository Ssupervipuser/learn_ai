# 定义名叫 num 的变量 存储的数值是 1
# 变量的值 又叫做 字面量
num = 1
# 查看变量的值
print(num) # 输出的是 1
# 加上引号就不是变量num了 而是字符串！
print('num') # 输出的是 num

# 变量的值是可以随时改变的！
num = 192 # 重新给 num 这个变量赋值
print(num) # 输出 192

# 再定义一个变量，要求值是200，且输出
num2 = 200
print(num2)

print('*'*10) # 字符串被重复10遍，再输出
# 变量的类型
# 需求：定义变量，存储姓名、年龄、性别、身高

# 字符串，定义姓名
name = '西门吹雪'
name2 = "叶孤城"
# 打印多个变量，用逗号分开
print(name, name2) # 西门吹雪 叶孤城

# type(变量名或变量的值) ==> 查看该变量的类型！
# str 表示 字符串类型
print(type(name)) # 输出 <class 'str'>

# 输出 <class 'str'> <class 'str'>
print(type(name), type(name2))
print(
    type(name),
    type(name2)
)

print(
    type(1111)
) # 输出 <class 'int'>
print('*'*10)
# 整数，定义年龄
age = 18
# 浮点数、小数，身高1.78
high = 1.78

# 真假值bool，性别要么男、要么女，男就是True
gender = True # 真、这里指代男的
gender2 = False # 假、表示不是男的

# 查看小数和真假布尔值的数据类型
print(type(high)) # <class 'float'>

print(type(gender)) # <class 'bool'>
print(type(gender2)) # <class 'bool'>


# todo 变量命名规则！
"""
1. 字母、下划线、数字组成，数字不能开头
a = 
a1 = 
a_1 = 
a_b_1 = 
_a = 
2. 玩家自定义的一切都不能和python的关键字重名！
包括文件夹和文件、变量、函数、类，都不能是python关键字！
python关键字 == python自带的

3. python中严格区分大小写！
A 不等于 a ！

4. 尽量让你自定义的一切名字 都能见名知意
xingming = '张三'
"""
# 给print这个名字重新定义，定义为一个整数！
# 此时print就不再具有输出、打印的功能了！
# print = 111
# 这里就报错了！
# print(print)

# todo 命名的三种方式！

# 1. 小驼峰：首字母小写
myName = '李四'
myname = '张三' # 常见

# 2. 大驼峰：首字母大写
MyName = '刘海柱'
Myname = '刘海柱2'

# 3. 蛇形：用了下划线
my_name = '王力猛' # 常见
My_name = '王力猛'

# 一般蛇形命名的时候 字母都小写
# 大驼峰：定义类的时候
# 蛇形 or 小驼峰：函数方法、变量、文件

# 变量1 = 5
# print(变量1)

