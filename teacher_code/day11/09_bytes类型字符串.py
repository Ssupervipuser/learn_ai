
strs = '黑马程序员'
# 把字符串转换成二进制（编码方式声明是utf8）
bs = strs.encode(encoding='utf8')
print(bs) # bytes类型的字符串
# b'\xe9\xbb\x91\xe9\xa9\xac\xe7\xa8\x8b\xe5\xba\x8f\xe5\x91\x98'
# b'\xba\xda\xc2\xed\xb3\xcc\xd0\xf2\xd4\xb1'
print(type(bs)) # <class 'bytes'>

# 把bytes类型的字符串按utf8编码方式转换回去
ret = bs.decode(encoding='utf8')
print(ret)