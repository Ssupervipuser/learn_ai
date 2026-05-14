my_dict={'name':'666','age':18,'city':'aaa'}
# my_dict=dict()
# print(my_dict)


my_dict['name']='8888'
print(my_dict)
print(my_dict.get('name'))
print(my_dict.get('citys'))
print(my_dict.get('citys','没这个东西'))


my_dict2={
    'a':0,
    'b':1,
    'c':2,
    'd':3}

print(len(my_dict))

# for key,value in my_dict.items():
#     print(key,value)

for v in my_dict.values():
    print(v)
print('='*20)
for k,v in my_dict.items():
    print(k,v)
    print(type(k),type(v))

print('-'*20)
for k in my_dict.keys():
    print(k)

print('-'*20)
for i ,(k,v) in enumerate(my_dict.items()):
    print(i,k,v)