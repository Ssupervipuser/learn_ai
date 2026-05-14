import re  # 补充必要的模块导入，保证代码可运行

# 1. .表示匹配任意1个字符，除了\n换行符
# 匹配数据: 从左向右匹配，一个字符接着一个字符的匹配
result = re.match(r"itcast.", "itcast22222")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")

# 2. [ ] 匹配[ ]中列举的字符
# [a-z]  [A-Z] [0-9]   [a-zA-Z0-9]
# [a-z]. 和[a-z]一样 表示a-z字母一个字符
# [a-z]* 表示任意个a-z字母，有可能0个，返回空字符串
# 匹配数据
result = re.match(r"[a-z][a-z]", "itcast376")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")

# 3. \d  匹配一个数字,即0-9 => [0123456789] => [0-9]
# 匹配数据
result = re.match(r"itcast\d.\d", "itcast5666")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")

# 4. \D  匹配非数字, 即不是数字
# 匹配数据
result = re.match(r"itcast\D", "itcast-66")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")

# 5. \s  匹配空白,即空格,tab键
# 匹配数据
result = re.match(r"itcast\s111", "itcast\t111")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")

# 6. \S  匹配非空白
# 匹配数据
result = re.match(r"itcast\S", "itcast\t")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")

# 7. \w  匹配非特殊字符，即a-z, A-Z, 0-9, _, 汉字
# 匹配数据
result = re.match(r"itcast\w", "itcasta")
# result = re.match("itcast\w", "itcast!")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")

# 8. \W  匹配特殊字符,即非字母, 非数字, 非_, 非汉字
# 匹配数据
result = re.match(r"itcast\W.", "itcast\t2aa")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")

