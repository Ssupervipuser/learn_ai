

a = 10
b, c = a, a
print(a, b, c)

# 通过id函数，可以知道 abc都等于同一个10
print(id(a))
print(id(b))
print(id(c))
# todo =等号的本质 是 【引用】
# 那个10本来存在，a只是引用、指向了它
a, b = 20, 10
print(id(a), id(b))

# 函数中参数的引用
# todo 函数传参传递的是：引用
abc = 100
def func(num1):
    print('func num1的id是：', id(num1))
print('函数调用执行之前，abc的id是：', id(abc))
func(num1=abc)
print('函数调用执行之后，abc的id是：', id(abc))

# todo 容器中元素可变的 是可变类型
# 在不改变id的情况下，能否改变其中的数据，若能就是可变，反之则不可变
# 可变：列表、字典、集合；不可变：数值类型、字符串、元组

# todo 如何证明list列表是可变类型？
# 定义一个列表，打印它的id
lst = []
print(id(lst)) # 2554154701120
# 添加元素之后再打印它的id
lst.append(0)
print(lst) # [0]
print(id(lst)) # 2554154701120
# 最后发现id没变化，内容变了，所以是可变类型

# todo 证明不可变类型的方法：
# 内容发生改变了、容器也变了==> 生成了新的容器
sr = 'abc'
print(id(sr))
print(id(sr+'d')) # 新字符串
print(id(sr))


# todo 集合 可变
st = set()
print(id(st))
st.add(1)
print(id(st))

# todo 元组 不可变
# 因为不能增删改元组中的元素，所以元组天然就是不可变类型
tpl = ()
print(id(tpl), type(tpl))
print(id((1,)))



# 元组A中嵌套的其他容器B，这个B内容咋变跟A没关系
tuple1 = (1, 2, 3, [3,4])
print(id(tuple1)) # 2856170787344
print(tuple1) # (1, 2, 3, [3, 4])
tuple1[3][0]= 33 # (1, 2, 3, [33, 4])
print(id(tuple1)) # 2856170787344
print(tuple1)

# lst2 = [3, 4]
# print(id(lst2))
# tuple2=(1, 2, 3, lst2)
# lst2[0] = 33
# print(lst2, id(lst2))
# # tuple2=(1, 2, 3, lst2的指向、引用，id)



set_1 = {1,2,3}
print(id(set_1)) # 1707673729312
set_1.add(5)
print(id(set_1)) # 1707673729312
print(id(set_1.add(4))) # 140715312826320

# set_1 # 是 集合
# set_1.add(4) # 是 集合的函数调用执行