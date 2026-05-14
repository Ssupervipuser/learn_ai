import re

my_str = 'abc123def456ghi789'
p = r'\d+[a-z]'
# todo findall 查询所有结果都返回list
ret = re.findall(p, my_str)
print(ret) # ['123d', '456g']

my_str = 'abc123def456ghi789'
p = r'(\d+)[a-z]'
# todo findall 查询所有结果都返回list
# todo  如果re规则里出现小括号，那么只返回小括号中匹配的结果！
ret = re.findall(p, my_str)
print(ret) # ['123', '456']

#  r'(\d+)[a-z]' 表示 只要1个或多个数字，但是数字后边得是一个小写字母 且 只要 1个或多个数字
#  只要括号里边的，但必须符合整个规则！

my_str = '<html>豆包</html>豆包，豆包比较好用，大家都爱用豆包'
#  \1 表示第1个()组
p2 = r"<([a-zA-Z1-6]{4})>豆包</\1>"
print(re.findall(p2, my_str)) # ['html']

my_str = '<html>豆包</html>豆包，豆包比较好用，大家都爱用豆包'
#  \1 表示第1个()组
p2 = r"<([a-zA-Z1-6]{4})>(豆包)</\1>\2"
print(re.findall(p2, my_str)) # [('html', '豆包')]


# new_str = re.compile(r'').sub('新的', '被替换的完整的大字符串')
# todo 替换、删除
new_str = re.sub(
    r'\d+', # re规则
    '*', # 新字符串
    '手机号：13812345678，验证码：666' # 要被替换的原字符串
)
print(new_str)

# todo 分割: 按规则去切割原字符串，返回新字符串构成的list
#   分割规则匹配的字符串就不要了
result = re.split(r'\s+', 'hello   world\tpython\njava')
print(result) # ['hello', 'world', 'python', 'java']
# 对比原来学的字符串的split方法
print('hello\tworld\tpython\tjava'.split('\t'))


# todo p = re.compile() 返回的是re正则规则
# new_str = re.compile(r'').sub('新的', '被替换的完整的大字符串')
phone_p = re.compile(r'^1[3-9]\d{9}')
print(phone_p)
ret = phone_p.findall('13112345678')
print(ret)
ret = phone_p.findall('13187654321asasasa')
print(ret)
# todo 先p = re.compile()的好处：超级大的字符串多次匹配的时候能够有效提升性能

# todo python re方法函数的两种用法：
"""
re.findall(r're规则', '原字符串')
re.compile(r're规则').findall('原字符串')
re.sub(r're规则', '新字符串', '原字符串')
re.compile(r're规则').sub('新字符串', '原字符串')
"""