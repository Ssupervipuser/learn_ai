
# 循环打印 1-10，跳过6

i = 1
while i <= 10:
    i += 1
    # 出现6之后就不再打印了
    if i == 6:
        # 注意continue的时机！
        continue # 跳过当前循环的这一次、后边的代码都不执行了！

    print(i)