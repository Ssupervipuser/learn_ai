

my_list = [1,2,3,4]

# 列表的遍历：把每一个元素从左到右依次，读取！
for i in my_list:
    print(i)

print(my_list)

# num是否在my_list中
num = 5
a = '不在里边'
for i in my_list:
    if num == i:
        a = '在里边'
print(a)

if num in my_list:
    print('在里边')