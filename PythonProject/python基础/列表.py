# my_list=[1,2,4,5,66,5,4,3,9]
#
# #增
# # my_list=my_list+[7,8,9]
# my_list.append(888)
# print(my_list)
# # 删
# my_list.remove(4)
# print(my_list)
# # 改
# my_list[2]=999
# print(my_list)
#
# # 查
# print(my_list[3])
#
# #for循环查
# for i in my_list:
#     print(i)
#
# #排序
# print('-'*34)
# my_list.sort(reverse=True)
# print(my_list)
#

#define list
names_list=[]
names_list=['aaa','bbb','ccc']

#add element
names_list.append('fff')
print(names_list)

# delete the specified element
names_list.remove('bbb')
print(names_list)

#get element base on their index
print(names_list[0])

# change element base on their index
names_list[0]='bbbbb'
print(names_list)

#delete element base on their index

del names_list[0]
print(names_list)

intlist=[1,2,3,4,5]

#
print(len(intlist))

print(max(intlist))
print(min(intlist))
print(sum(intlist))


intlist2=[3,2,5,4,6]
# the element of list are reordered
intlist2.sort()
print(intlist2)

intlist2.sort(reverse=True)
intlist2[::-1]
print(intlist2)

print('ccc' in intlist)
print('ccc' not in intlist)

for index,name in enumerate(names_list):
    print(index,name)

print([index for index, value in enumerate(names_list)])
print([index for index, _ in enumerate(names_list)])
# _ 是python解释器的约定表示我不需要这个值