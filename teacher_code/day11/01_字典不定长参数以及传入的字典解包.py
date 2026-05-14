# 关于函数定义 **kwargs 以及传参时 * 的使用
d = {'a':1, 'b':2}
def bar(**kwargs): # 字典不定长参数
    print(*kwargs) # 打印出来的是key
    print(kwargs) # 打印出来是字典

bar(**d)  # 两个*表示 k和v
bar(a=1, b=2)

def bar(ak, bk):
    print(ak, bk)

# 一个*表示key，传入的是字典d的key
bar(*d) # *d 不用考虑字典中的key是否和函数形参是否严格一致！数量得一致
bar(ak='a', bk='b')
bar('a', 'b')

def bar(a, b):
    print(a, b) # 此时 a,b参数接收的是 字典中的v

# **d 传入的字典d中的key必须和函数形参严格一致！
bar(**d) # 传入字典、同时解包成 a=1, b=2 相当于 **dict
bar(a=d['a'], b=d['b'])
bar(d['a'], d['b'])
