
# 循环打印 5次 1-10，跳过6，每次数字作为1行
j = 1
while j <= 5:
    i = 1
    while i <= 10:
        # 出现6之后就不再打印了
        if i == 6:
            # 在 continue 终止本次、进入下次循环之前 先让 i + 1
            i += 1
            # 注意continue的时机！
            continue # 跳过当前循环的这一次、后边的代码都不执行了！
        print(i, end='')
        i += 1

    print()
    j += 1