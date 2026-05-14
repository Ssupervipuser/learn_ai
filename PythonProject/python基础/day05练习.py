#元组不定长参数，用一个* 来表明，纯如是是一个元组
def fun(*args):
    print(type(args),args)
    return 111
ret=fun(1,2,3,4)


# 字典不定长参数，用** 表名，传入是是一个字典
def func1(**kwargs):
    print(type(kwargs),kwargs)

func1(
    name='aaa',
    age=18,
    gender='af'
)

#函数不同形式参数有顺序要求，普通参数，元组不定长参数，缺省参数，字典不定长参数
def func2(int,*args,name='dehua',**kwargs):
    print(int,args,name,kwargs)

func2(1,2,3,5,name='zhangsan',age=16,gender='nv')
def func3(**kwargs):
    print(type(kwargs),kwargs)


#组包，变量赋值时，等号右边有多个数据时，会自动包装为元组赋值给等号左边的变量
a=1,2,4
print(type(a), a)


#拆包，多个变量=容器数据    当变量数值等于容器长度时，容器中的每个元素会依次赋值给等号左边的变量

a,b,c=(1,2,3)
print(a,b,c)

#先组包后拆包
a,b,c=1,2,3
print(a,b,c)

a,b=10,20
print(f'a={a},b={b}')



#函数多个返回值
def func4():
    return 1,2,4
a,b,c=func4()
print(a,b,c)

a=10
b=a
c=a
print(id(a),id(b),id(c))

a=20
print(id(a),id(b),id(c))


my_list=[1,2,3,4,5,6,7,8,9]
my_list=[4,12,3,[3,4]]

your_list=my_list
print(id(my_list),id(your_list))

my_list[0]='haha'
print(id(my_list),my_list)
print(id(your_list),your_list)
print('*'*19)


list1 = [1, 2, [3, 4]]
list2 = list1.copy()

print("list1:", list1, id(list1))
print("list2:", list2, id(list2))

list1[2][0] = 5
print('修改了list1中的嵌套值')


print("list1:", list1, id(list1))
print("list2:", list2, id(list2))

list1[0] = 5
print('修改了list1中的值')


print("list1:", list1, id(list1))
print("list2:", list2, id(list2))

print('*'*19)
from copy import deepcopy # 导包使用 deepcopy深拷贝函数

list1 = [1, 2, [3, 4]]
list2 = deepcopy(list1)

print("list1:", list1, id(list1))
print("list2:", list2, id(list2))

list1[2][0] = 5
print('修改了list1中的某个值')

print("list1:", list1, id(list1))
print("list2:", list2, id(list2))