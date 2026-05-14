
a = {1,2,3,9,5}
for i in a:
    print(i)
for i in enumerate(a):
    print(i)


lst = [1,2,3]
ret = lst.append(4)
print(ret) # None
print(lst)

sr = '12345'
new_sr = sr.replace('1', 'a')
print(new_sr)
print(sr)

ret = sr.find('1')
print(ret)

ret_list = sr.split('3')
print(ret_list)

d = {1:'a', 2:'b'}
print(max(d), min(d), sum(d))
for k in d:
    print(k)
for k in d.keys():
    print(k)