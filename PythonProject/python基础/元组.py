'''
元组只能读，不能增删改，不能改变顺序
tuple is read only ,can't change order
'''

# define tuple

names_tuple=()
names_tuple=('aaa',)
names_tuple=('aaa','bbb','ccc','ddd')


for index ,name in enumerate(names_tuple):
    print(index,name)

int_tuple=(1,2,3,4)
print(int_tuple[::-1])
new=int_tuple[::-1]
print(type(new))

generator=(i for i in int_tuple)
print(generator)
