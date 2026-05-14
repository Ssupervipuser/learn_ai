
# while没有break，循环结束就执行else

i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('这里是while循环的else')

print('-'*5)

# while被break终止了，就不会执行else

i = 1
while i <= 10:
    if i == 11:
        i += 1
        break
    print(i)
    i += 1
else:
    print('这里是while循环的else')

print('-'*5)