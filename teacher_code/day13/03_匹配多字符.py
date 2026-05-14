import re
"""匹配字符的数量：前一个字符的数量
* 前一个字符出现0次、1次或多次
+ 前一个字符出现1次或多次
? 前一个字符出现0次、1次 【注意往下边看、还有非贪婪模式】
{n} 前一个字符出现n次
{n,m} 前一个字符出现n到m次 
"""

# * 表示前一个字符出现任意次、包括0次
ret = re.match(r'itcast1*', 'itcast1111222333')
print(ret.group())
ret = re.match(r'itcast1*.*', 'itcast1')
print(ret.group())
ret = re.match(r'itcast\d*', 'itcast1111222333aaa')
print(ret.group())

# + 表示前一个字符出现1次或多次、不是0次！
ret = re.match(r'itcast\d+', 'itcast')
if ret is None: print(ret)
else: print(ret.group())

# ? 表示前一个字符出现0次或1次
ret = re.match(r'itcast\d?', 'itcast12345')
if ret is None: print(ret)
else: print(ret.group())

# {m} 表示 前一个字符重复连续出现m次
# {m,n} 表示 前一个字符重复连续出现m-n次
ret = re.match(r'[a-z]{1,2}', 'itcast12345')
if ret is None: print(ret)
else: print(ret.group())
ret = re.match(r'[a-z]{2}', 'itcast12345')
if ret is None: print(ret)
else: print(ret.group())
ret = re.search(r'[a-z]{2}', '33b333itcast12345')
if ret is None: print(ret)
else: print(ret.group())


"""贪婪与非贪婪：
+ * ? 表示数量，当?出现在它们后边的时候，取最短！【非贪婪】
.* 0个字符、1个字符、多个字符，会尽可能的长！【贪婪模式】
.*? 0个字符、1个字符、多个字符，但是会尽可能的短！【非贪婪模式】
+? 前一个字符出现1次
"""
my_str = '0123456'
print(re.search(r'.*', my_str).group())
print(re.search(r'.*?', my_str).group()) # 返回''空字符串

# \d+? ==> \d
# todo + * ? 表示数量，当?出现在它们后边的时候，取最短！【非贪婪】
print(re.search(r'\d+?', my_str).group()) # 返回 0 【一个字符】
print(re.search(r'\d?', my_str).group()) # 返回 0 【一个字符】
print(re.search(r'\d??', my_str).group()) # 返回 '' 【空字符】
my_str = '0123456'
print(re.search(r'\d{2,5}', my_str).group()) # 返回 01234
print(re.search(r'\d{2,5}?', my_str).group()) # 返回 01