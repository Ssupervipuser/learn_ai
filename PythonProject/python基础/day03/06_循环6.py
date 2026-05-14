
# 外层循环到第 i 次，内层就循环 i 次

i = 1
while i <= 5:
    # i是几，内层循环就循环几次
    j = 1
    while j <= i:
        print(1, end='')
        j += 1
    print() # 内层循环全部执行完毕，就换行
    i += 1