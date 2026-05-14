# 1 需求：在列表中["apple", "banana", "orange", "pear"]，匹配apple和pear
import re

fruit = ["apple", "banana", "orange", "pear"]

for fruit_str in fruit:
    # todo [] 不管里边写啥，只能匹配一个字符！
    p = r'[apple|pear]' # 表示[]中出现的任意的一个字符、一个字符！
    ret = re.search(p, fruit_str)
    if ret: print(ret.group())
    else: print(ret)
for fruit_str in fruit:
    # todo (a|b) 表示 a或b
    p = r'(apple|pear)'
    ret = re.search(p, fruit_str)
    if ret: print(ret.group())
    else: print(ret)

# 2 需求：匹配出163、126、qq等邮箱
"""
xxxxxx@163.com
xxxxxx@126.com
xxxxxx@qq.com
"""
my_str = 'dsdsds232232@163.com'
# todo (163|126|qq) 表示 163或126或qq
p = r'.+@(163|126|qq)\.com'
print(re.search(p, my_str).group())

# 3 需求：匹配qq:10567这样的数据，提取出来qq文字和qq号码
my_str = '职业法师刘海柱的qq:10561他擅长给人买瓜子'
p = r'qq:\d+'
p = r'(qq):(\d+)'
p = r'(qq):([1-9]\d{4,11})' # qq:5-12位数字
print(re.search(p, my_str).group())
# todo (xxxx) 表示 一个整体

# 4 需求：匹配出 <html>hh</html>
my_str = '<html>hh</html>'
my_str = '<html>豆包_百度搜索</html>'
p = r'<[a-z]+>.+</[a-z]+>'
print(re.search(p, my_str).group())

my_str = '<html>豆包_百度搜索</html>'
p2 = r"<([a-zA-Z1-6]{4})>.*</([a-zA-Z1-6]{4})>"
print(re.search(p2, my_str).group())


# todo 测试打印,比较不同
print('\1')
print('\\1') # 在字符串中，\有特殊含义，想输出\本身，就必须\\

# todo \num 表示上一个()组
text = "aa bb cc ab ba 11 22"
# (\w) 是第1分组，\1 表示再匹配一次同样的内容
# todo 只要(\w)一个字符，\1表示和前边字符相同的字符 ：两个相同字符，但只返回第一个字符
result = re.findall(r'(\w)\1', text)
print(result)

my_str = '<html>豆包_百度搜索</html>'
#  \1 表示第1个()组
p2 = r"<([a-zA-Z1-6]{4})>.*</\1>"
print(re.search(p2, my_str).group())

my_str = '<html>豆包</html>豆包，豆包比较好用，大家都爱用豆包'
#  \1 表示第1个()组
p2 = r"<([a-zA-Z1-6]{4})>(豆包)</\1>\2"
print(re.findall(p2, my_str)) # [('html', '豆包')]

