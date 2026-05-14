import re


# 找出指定的.py文件中的所有函数方法，输出函数方法的名字
# 1. 读取文件
# filepath = './07_demo示例代码cms.py'
# with open(filepath, 'r', encoding='utf8') as fr:
#     content_str = fr.read()
# print(content_str)
# 2. re规则
# """
# def  函数名 (a = '没参数或有参数') :
#     pass
# def==>def
# \s==>空格、\n、\t等等
# (\S+)==>非空白字符
# .*==>任意字符任意数量，这里主要为了匹配函数名后边、括号前边的空白字符
# \(==>左半边小括号
# \)==>右半边小括号
# """

# p = r'def\s+(\S+).*\(.*\):' # 匹配所有函数名
# p = r'def\s+([a-zA-Z_]\w*)\s*\('
# # 3. 匹配所有并输出
# ret_list = re.findall(p, content_str)
# print(ret_list)

"""
1. 匹配并查找所有
ret_list = re.findall(r're规则', content_str)
2. 匹配一个，匹配不到就报错（None.group()【X】）
ret_str = re.search(r're规则', content_str).group()
3. 匹配一个，从content_str的第一个字符开始严格匹配
匹配不到就报错（None.group()【X】）
ret_str = re.match(r're规则', content_str).group()

4. 切割: 符合规则的字符串抛弃、返回切割后的字符串构成的列表
ret_list = re.split(r're规则', content_str)

5. 替换
new_str = re.sub(r're规则', '新字符串', '旧的原字符串')

6. 提前创建re规则: 一个规则编译之后，匹配多次（大字符串），能明显提升效率
re_p = re.compile(r're规则') 

re_p.findall(content_str)
re_p.search(content_str)
re_p.match(content_str)
re_p.split(content_str)
re_p.sub('新字符串', '旧的原字符串')
print(type(re.compile(r're规则'))) # <class 're.Pattern'>
<class 're.Pattern'>
"""

"""re语法规则：请善用各种大模型查询re的规则
一、一个字符
. 任意一个字符，除了\n
[你好吗] 三个字符任意一个
[0-9] 一个数字字符
[a-zA-Z0-9] 一个字符，英文字母或数字
\d 一个数字0-9；\D 取反集
\s 一个空白符号，比如\t空格\n...；\S 取反集
\w 一个字符：[a-zA-Z0-9_]；\W 取反集
二、数量
.* 任意0个或多个字符
.+ 任意1个或多个字符
.? 任意0个或1个字符
\d{5} 连续的5个数字
.{1,3} 任意的一个到三个字符 
三、贪婪非贪婪
\d+? 一个数字
a?? 本来a?表示0或1个a，但a??表示0个a
四、开头^结尾$: 被匹配的原字符串的 ^开头、结尾$
^a 被匹配的原字符串以a开头，返回a
[a-z]{6}z$ 被匹配的原字符串以z结尾，前边是6个小写英文字母
五、转义、转译 \
\. 匹配.本身
\\ 匹配\本身
\(\) 匹配小括号本身
六、小括号分组
a(bc)d 按照规则匹配abcd，findall时返回bc
a(bc)d\1 按照规则匹配abcdbc，\1表示第一个小括号里的规则复用
七、| 或者
(abc|bcd) 表示匹配abc或bcd
ab(c|b)cd 表示匹配c或b
"""


# with open('1111.png', 'rb') as f:
#     ret = f.read()
# print(ret)
#
# a = '1234567890zasasahjg1211itcastsasa1itcastsasa09'
# p = r'\d(itcast)(sa)'
# ret_list = re.findall(p, a)
# print(ret_list) # [('itcast', 'sa'), ('itcast', 'sa')]
# new_retlist = [i[0] for i in ret_list]
# print(new_retlist)

