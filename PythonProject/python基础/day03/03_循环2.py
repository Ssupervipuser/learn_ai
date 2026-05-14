
# 计算 1-100 累加和
sum_int = 0
i = 1
# 要循环100次，i从 1-100 依次出现
while i<=100:
    print(i)
    # 把每次出现的 i 加进去
    # 重新覆盖掉 sum_int 的值
    sum_int = sum_int + i
    # 为下一次循环做准备，让 i 的值 +1
    i += 1

# 5050
print(sum_int)
