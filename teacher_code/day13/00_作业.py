import re
# 1. 07_re练习.py
#   要求：把re常用6个函数都写一遍
#todo re.match:从字符串开头匹配
#   作用：直接打字符串开头是否符合正则模式，成功返回Match对象，失败返回None
#   语法：re.match(pattern,string,flags=0)

#匹配开头的数字
ret=re.match(r'\d+','123abc456')
print(ret.group())

#todo re.search(pattern,string,flags=0)在字符串任意位置匹配第一个符合的结果
#   作用：扫描整个字符串，找到第一个符合正则模式的子串，返回Match对象，失败返回None

ret=re.search(r'\d+','123abc456')
print(ret.group())

#todo re.findall(pattern,string,flags=0) 找到所有符合的结果，返回列表
#   作用扫描整个字符串，返回所有匹配的子串组成的列表，无匹配返回空列表

result = re.findall(r'\d+', 'abc123def456ghi789')
print(result)

#todo sub(pattern,repl,string,count=0,flags=0)将字符串中匹配正则的部分替换成指定内容，返回替换后的新字符串
#   count：默认0（替换所有），指定数字则只替换前N个

result = re.sub(r'\d+', '*', '手机号：13812345678，验证码：666')

print(result)

#todo re.split(pattern,string,maxsplit=0,flags=0)将字符串按正则分割，返回分割后的列表
#   maxsplit：默认0（全部分割），指定数字则只分割前N次


# 示例1：按任意空白符（空格/制表符/换行）分割
result = re.split(r'\s+', 'hello   world\tpython\njava')
print(result)  # 输出：['hello', 'world', 'python', 'java']# 示例2：按逗号或分号分割
result2 = re.split(r'[,;]', '苹果,香蕉;橙子,葡萄')
print(result2)  # 输出：['苹果', '香蕉', '橙子', '葡萄']

#todo re.compile(pattern,flags=0)将正则模式编译为pattern对象，可重复使用（多次匹配是推荐，减少重复编译开销）

# 2. 08_上下文管理器-手写open文件.py

class MyFile(object):
    def __init__(self,file_path_name,file_model):
        self.file_path_name = file_path_name
        self.file_model = file_model
        self.fp=None

    def __enter__(self):
        print('这是上文')
        self.fp=open(self.file_path_name,self.file_model)

    def __exit__(self,exc_type,exc_value,traceback):
        print('这是下文')
        self.fp.close()

if __name__ == '__main__':
    with MyFile('./1.txt', 'w') as f:
        print('创建1.txt文件，为后续测试做准备')
    with MyFile('./1.txt', 'r') as f:
        a = 1 / 0 # 这里报错，不影响关闭文件
        filedata = f.read()
        print('filedata-->', filedata)      