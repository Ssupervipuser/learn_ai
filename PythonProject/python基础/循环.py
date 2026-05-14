# todo 跑步5圈 ，每跑一圈，做十个俯卧撑
# i=1
# while i<=5:
#     print('跑步%d圈'%i)
#
#     j=1
#     while j<=10:
#         print(f'俯卧撑{j}个')
#         j+=1
#     i+=1
#


# i=0
# while i<=5:
#     j=0
#     while j<=i:
#         print('*',end='')
#         j+=1
#     print('\n')
#     i=i+1


#遍历字符串，跳过6，不打印，使用continue

my_str='123456789'


for i in my_str:
    if i=='6':
        continue
    print(i)

#打印到6就不打印了

for i in my_str:
    if i == '6':
        break
    print(i)



















