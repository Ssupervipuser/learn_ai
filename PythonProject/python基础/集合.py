my_set={1,2,3,4,5,6,7,8,9}
print(my_set)
myset2=set([1,2,3,4,5,6,7,8,9])
print(myset2)

#
my_set.add(10)
my_set.add(10)
my_set.add('aaaaa')
print(my_set)
my_set.remove('aaaaa')
print(len(my_set))
print(max(my_set))
print(min(my_set))

#遍历每个元素
for s in my_set:
    print(s)

for i ,v in enumerate(my_set):
    print(i,v)