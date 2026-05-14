
# 1. 输入用户年龄，类型转为int
age = input('输入年龄') # str
age_int = int(age) # int

# 2. 判断是否满18
# ge_int >= 18 是条件表达式
if age_int >= 18:
    # 2.1 如果满18，允许进网吧
    print('允许进网吧')
# 3. 如果不满18，回家写作业
else:
    print('回家写作业')