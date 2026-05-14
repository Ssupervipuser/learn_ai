# 打印1-10，但跳过6
i = 1
while True:
    # 判断是否到6
    if i == 6:
        print('跳过6')
        i += 1 # 在本次循环结束之前 i 要自增 1
        continue # 提前结束本次循环，继续下一次循环
    print(i) # 10
    i += 1 # 11
    # 判断 i 超过10
    if i > 10:
        break # 结束全部循环
print('while循环之后的代码')