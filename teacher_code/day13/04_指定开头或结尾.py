# r'[^\d]' 除了数字以外的一个字符
# todo ^ $ 分别表示 被查找匹配的（旧的）字符串开头结尾
#   ^ 表示从文本字符串的最开头第一个字符开始严格匹配；从第一个字符开始查找
#   $ 表示从文本字符串的最后一个字符严格匹配；从最后一个字符开始查找
#   [^ ....] 表示 取反集

import re
# todo r'^\d' 表示被匹配的字符串的首字母是数字，返回这个数字
#  r'^[\d]{5}' 表示数字开头（从被匹配的首字符）就是个数字，返回5个数字
#  ^ 能把 re.search 等同于 re.match
print(re.match(r'^\dit', '2itcast').group())
print(re.search(r'^\dit', 'sasasasa2itcast')) # None
print(re.match(r'^\d.*', '22itcast').group()) # 22itcast


# todo 当指定一个字符结尾时，前边是非贪婪模式且可能匹配到空串，那最终返回的就是空字符串
#   .*?\d$ 本来.*?是表示非贪婪 应该匹配''空字符串，但是$规定以\d为结尾，所以?非贪婪就不起作用了
#   $ 表示被匹配的字符串的结尾必须是前一个字符串
#   \d$ 只能匹配 整个大字符串最后一个字符是数字结尾
print(re.match(r'.*?\d$', 'itcast666777').group()) # 返回 itcast666
# print(re.match(r'.*\d$', 'itcast666a').group()) # 返回 itcast666
# 匹配数字开头、数字结尾
p = r'^\d.*$'  # r'^\d*$'
print(re.match(p, '1abc456').group())
# 匹配11位的手机号
p = r'1\d{10}'
print(re.search(p, '张三13112345678男').group())

# todo [^指定字符]  匹配除了指定字符以外的所有字符
# 查询不以4结尾、返回3位数字
my_str = '42121212121214'
p = r'[^4$]{3}'
print(re.search(p, my_str).group())
p = r'^[4]\d*$' # todo $必须放在规则的最后 # ，当^不在[]中必须放在规则的前边
print(re.search(p, my_str).group())