


nums = [i for i in range(21)]
nums = list(range(21))
print(nums)

# 求 列表中既是奇数、又能被3整除余数为0，这些符合条件的元素求和

sum = 0
for i in nums:
    # 奇数 i % 2 == 1
    # 被3除余0 i % 3 == 0
    if i % 2 == 1 and i % 3 == 0:
       sum += i # sum = sum + i
print(sum)


def describe_inputs(*args, **kwargs):
    print(f"位置参数个数: {len(args)}")
    print(f"关键字参数个数: {len(kwargs)}")
    print(f"关键字参数的键: {', '.join(kwargs.keys())}")


    print('位置参数个数: ', len(args))
    print('关键字参数个数: ', len(kwargs))
    print('关键字参数的键: ', end=' ')
    for i, k in enumerate(kwargs.keys()):
        if i == len(kwargs)-1 : # len(kwargs)-1 就是最后一个遍历出来的元素的‘下标’
            print(k)
        else:
            print(k, end=', ')

describe_inputs(1, 'hello', 3.14, name='Alice', age=25, city='Beijing')
# 示例输出：
# 位置参数个数: 3
# 关键字参数个数: 3
# 关键字参数的键: name, age, city


"""
接收用户输入的账号和密码，
如果账号为'admin'，密码为'admin888'，则提示用户登录成功，
其他情况则提示用户名或密码输入错误，只有3次输入机会。
"""

i = 3
while i > 0 :

    username = input('账号：')
    password = input('密码：')

    if username == 'admin' and password == 'admin888':
        print('登陆成功')
        break
    else:
        i -= 1
        if i == 0:
            print('登录失败没有机会了！')
        else:
            print('用户名或密码输入错误，还有{}次机会'.format(i))

