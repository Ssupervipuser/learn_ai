import re

my_str = 'abc123def456ghi789'

p=r'\d+[a-z]'   #['123d', '456g']

#todo findall查询所有结果都返回list
ret=re.findall(p,my_str)
print(ret)

p=r'(\d+)[a-z]'
#todo 如果re规则里出现小括号，那么只返回小括号中匹配的结果
ret=re.findall(p,my_str)
print(ret)

my_str = '<html>豆包</html>豆包，豆包比较好用，大家都爱用豆包'
#\1表示第1个()组
# p2=r'<([a-zA-Z1-6]{4})>豆包</\1>'
p2=r'<([a-zA-Z1-6]{4})>豆包</\1>\2'
ret=re.findall(p2,my_str)
print(ret)  #['html']

# new_str=re.compile(r"").sub('新的','被替换的完整的大字符串')