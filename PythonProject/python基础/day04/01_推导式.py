
# 把字典中的所有值，构造成一个列表

d = {'a':1, 'b':2, 'c':3}

lst = []
for v in d.values():
    lst.append(v)
print(lst)

# todo 列表推导式，也是一种构造列表的方法
lst2 = [v for v in d.values()]
print(lst2)

# todo 元组不能直接推导，需要通过列表转换为元组
d = {'a':1, 'b':2, 'c':3}
tpl = (k for k in d.keys()) # 不直接返回元组，给的是迭代对象
print(tpl)
tpl = tuple([k for k in d.keys()])
print(tpl)

# todo 集合推导式
d = {'a':1, 'b':2, 'c':3}
st = {k for k in d.keys()}
print(st)
st = set([k for k in d.keys()])
print(st)

# lst3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst3 = [i for i in range(10)]
print(lst3)
# 对lst3这个列表 进行转换：用推导式的方式 转换成 元组、集合！
# 转元组
tpl = tuple([v for v in lst3])
print(tpl, type(tpl))
# 转集合
st = {v for v in lst3}
print(st, type(st))