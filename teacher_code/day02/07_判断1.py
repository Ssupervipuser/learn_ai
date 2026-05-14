
# 能否进网吧
# 1. 定义变量，获取用户的年龄
age_str = input('少年，请输入你的年龄：')
# 2. 转换类型 年龄字符串 转成 int数字
age_int = int(age_str)

# 3. 判断：年龄大于等于18,
# if 条件表达式:
# age_int >= 18
if age_int >= 18:
    # todo 条件表达式为False的时候，if的区域代码不执行！
    # 4. 如果大于等于18成立，就请进
    print('请进')
    print('请进')
    print('请进')
    print('请进')
    print('请进')

# todo 不管前边的判断是怎么样子的，这里都会执行
print('最终都得出去')

# todo 如果想双分支判断
# if age_int < 18:
#     print('出去')


