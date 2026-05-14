import traceback

my_list = [i for i in range(5)]
print(my_list, type(my_list)) # [0, 1, 2, 3, 4] <class 'list'>

# todo 生成器！用推导式的方式构造生成器！下边不叫元组
my_generator = (i for i in range(5)) # 保存的是生成元素的规则
# <generator object <genexpr> at 0x00000192611CEA40>
print(my_generator, type(my_generator)) # <class 'generator'>
for i in my_generator:
    print(i)
# todo 取空了之后就不能再next()了，不然报StopIteration这个错误！
# todo 对于生成器来说，除了遍历以外，还可以用next(g)按顺序获取元素
for i in range(5):
    try:
        v = next(my_generator)
        print(v)
    except:
        pass
        # print(traceback.format_exc())


# todo 生成器函数
def myGenerator(n):
    for i in range(n):
        print('myGenerator：开始生成...')
        # todo 能够让函数变成生成器
        #  i 就是每次调用next()或遍历1次时返回的对象
        yield i
        print('myGenerator：生成1次') # 不出现了

# todo 生成器函数的返回值是生成器
g = myGenerator(6) # g就是生成器
# <generator object myGenerator at 0x000001F0FEFC1CB0> <class 'generator'>
print(g, type(g))
print(next(g)) # 0
print(next(g)) # 1
for i in g:
    print(i) # 这里依次返回 2、3、4、5
# print(next(g)) # 报错：StopIteration