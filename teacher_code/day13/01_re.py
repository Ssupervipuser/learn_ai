
import re # 正则导包

"""re.match
匹配字符: 从大字符串中第一个字符开始, 返回第一个符合条件的子串"""
my_str = 'aitcastitk'
# todo re.match(r'正则表达式规则', 被查找的字符串)
#   从被查找的字符串首个字母开始匹配，匹配到就返回第一个
#   r'.it.' 表示：  4个字符中间两个是it
#   r'xxxxx'表示：  正则规则字符串
#   ret = re.match(...) ret就是返回的查询结果对象
#   如果没有匹配（查询）到，ret就是None！
ret = re.match(r'.it.', my_str)
# todo 用查询结果对象.group() 获取查询到的结果字符串
print(ret.group()) # aitc
# print(re.match(r'.it.', 'itcastitk').group()) # 报错！ None 没有 group()方法
print(re.match(r'.it.', 'itcastitk')) # None


my_str = 'city:1beijing2.shanghai'
# todo re.search() 查询整个字符串，根据规则返回第一个匹配到的结果str
#  \d 表示一个数字
#  . 表示一个任意字符
#  * 表示任意数量的任意字符
#  匹配不到就返回None None不能grop()
ret = re.search(r'\d.*', my_str)
print(ret.group()) # 1beijing2.shanghai
ret = re.search(r'', my_str)
print(ret.group()) # 匹配到了！只不过匹配到的是空字符串！


"""删除或替换"""
my_str = '车主说：你的刹车片应该更换了啊，嘿嘿'
# 定义正则规则（正则表达式）
# todo | 表示 或者
p = r'呢|嘿|啊|嘿嘿'
# todo 按照pattern规则匹配，将oldstr中匹配到的子字符串替换为newstr
#  re.compile(pattern=p).sub('newstr', 'oldstr') 返回替换后的新字符串
ret = re.compile(pattern=p).sub('新字符串', my_str)
print(ret)
# todo 删除
ret = re.compile(pattern=p).sub('', my_str)
print(ret)
# todo  \. 表示匹配的是.本身；一个.表示任意1个字符
#  \\ 表示 \本身
p2 = r'[^，！？。\.\-\u4e00-\u9fa5_a-zA-Z0-9]' # [^……]表示取除了中括号规则的反集
r = re.compile(p2) # 传入正则规则，返回匹配对象
new_str = r.sub('x', my_str) # 替换
print(new_str)


# 练习：弹奏肖邦的夜曲，纪念你死去的爱情！
# 中文标点符号，全部替换成英文标点符号
r = r'[，。！？；：""''（）【】《》…—]'
my_str = '弹奏肖邦的夜曲，纪念你死去的爱情！'
ret = re.compile(r).sub(',', my_str)
print(ret)

# 1. .表示匹配任意1个字符，除了\n换行符
# 匹配数据: 从左向右匹配，一个字符接着一个字符的匹配
result = re.search(r"itcast.", "2itcast22222")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
