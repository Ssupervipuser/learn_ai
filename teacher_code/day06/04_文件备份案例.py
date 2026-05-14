# 1. 指定文件、获取文件的完整路径
filepath = './code2/test2.txt' # 要备份的文件的路径
"""上边是个相对路径：相对于当前代码的位置，目标文件的完整路径
. 当前
./ 当前路径下
.. 上一级文件夹
../ 上一级文件夹下
../a.py 上一级文件夹下的a.py文件
../../b/c.txt 上一级的上一级文件夹下的b文件夹下的c.txt文件
绝对路径：从根目录（盘符C、D）开始一直到文件的扩展名
"""
# 2. 根据要备份的文件 定义新文件的名字： xxx[备份].xxx
# 2.1.找最后一个点的下标
# filepath[::-1] 把整个路径字符串倒排反转
# .find('.') 找最后一个点的下标，此时下标是反的
# - (反转的路径字符串.find('.') + 1)
# 求的是正常路径字符串倒着数的下标，比如 xxx.txt的点的下标就是 -4
xiabiao = - (filepath[::-1].find('.') + 1)
print(xiabiao)
# 2.2.切片、拼接： xxxx[备份].xxx
# ./code2/test2 + [备份] + .txt
new_fp = filepath[:-4] + '[备份]' + filepath[-4:]
# ./code2/test2[备份].txt
print(new_fp)
# new_fp = './code2/test2[备份].txt'
# 3. 根据新备份文件的完整路径创建新文件，w写方式
with open(new_fp, 'w', encoding='utf8') as fw:
    # 4. 读取要备份的旧文件中的文本内容
    with open(filepath, 'r', encoding='utf8') as fr:
        content_str = fr.read()
    # 5. 旧文件文本内容写入新备份文件
    fw.write(content_str)

# todo 相对路径的必要性：方便代码迁移、方便代码在其他环境部署
# todo 为啥需要操作文件进行读写：让程序和文件进行交互
