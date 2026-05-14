import re
#
# #re.match 从大字符串中第一个字符开始，返回第一个符合条件的子串
# my_str='aitcastitk'
# #todo re.match(r'正则表达式规则',被查找的字符串)
# #   从被查找的字符串首个字母开始匹配，陪陪到就返回第一个
# #   ret=re.match()   ret就是返回的查询结果对象
# #   如果没有匹配到就返回None
#
# ret=re.match('.it.',my_str)
# print(ret)
# print(ret.group())
#
# # my_str='city:1beijing2.shanghai'
# #todo re.search()查询整个字符串，根据规则返回抵押
#
# ret=re.search('.it.',my_str)
# print(ret)
# print(ret.group())
#
#
# print('*'*10)
# """删除或替换
# ret = re.compile(r'正则规则').sub('新子串', '字符串')
# """
#
# import re
# sentence = "车主说:你的刹车片应该更换了啊,嘿嘿"
#
# # 删除 去掉语气词
#
# p = r"呢|吧|哈|啊|啦|嘿|嘿嘿"
# mystr = re.compile(pattern=p).sub('', sentence)
# print('mystr-->', mystr)
#
# # 替换 除了汉字数字字母和，！？。.- 以外的字符，都换成x
# # \u4e00-\u9fa5 是用来判断是不是中文的条件
# p = r"[^，！？。\.\-\u4e00-\u9fa5_a-zA-Z0-9]"
# r = re.compile(pattern=p)
# mystr = r.sub('x', sentence)
# print('mystr-->', mystr)

result=re.match(r'itcast','itcast222222')
if result:
    info=result.group()
    print(info)
else:
    print('没有匹配到')

# 2. [ ] 匹配[ ]中列举的字符
# [a-z]  [A-Z] [0-9]   [a-zA-Z0-9]
# 匹配数据
result = re.match(r"itcast[123abc]", "itcast376")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
    
# 3. \d  匹配一个数字,即0-9 => [0123456789] => [0-9]
# 匹配数据
result = re.match(r"itcast\d", "itcast5666")
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

with open()



