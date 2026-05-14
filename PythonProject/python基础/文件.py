#1.指定文件、获取文件的完整路径
filepath='./test2.txt'

#2.根据要备份的文件，定义新文件的名字

#2.1 找最后一个的下标
xiabiao=-(filepath[::-1].find('.')+1)

#2.2. 切片，拼接
new_fp=filepath[:-4]+'[备份]'+filepath[-4:]
print(new_fp)

# 根据新备份文件的完整路径创建新文件

with open(new_fp,'w',encoding='utf-8') as f:
    #5.读取要备份的就文件中的文本内容
    with open(filepath,'r',encoding='utf-8') as fr:
        content_str=fr.read()

    f.write(content_str)

