
my_list = ['职业法师刘海柱', '基尼太美蔡徐坤', '声具泪下周淑怡']

# 遍历列表中 元素下标 和 元素的值
for i in enumerate(my_list):
    print(i)
for i, v in enumerate(my_list):
    print(i)
    print(v)

# todo 切片：返回的东西是列表
print(my_list[::-1]) # 反转
# 左包右闭、左闭右开、左包右不包、左边要右边不要
print(my_list[0:1]) # ['职业法师刘海柱']
# print(my_list[0:1:1]) # ['职业法师刘海柱']
print(my_list[0:2]) # ['职业法师刘海柱', '基尼太美蔡徐坤']

# todo [x:y:-n]
# x:y 表示从哪到哪：左包右闭、左闭右开、左包右不包、左边要右边不要
# 如果xy都不写，只有一个冒号，表示从头到尾都要！
# todo -n的- 表示从右往左数
# todo -n的n 表示步长，比如2，倒数第1个要，倒数第2个不要，倒数第3个要，倒数第4个就不要了
print(my_list[::-2]) # ['声具泪下周淑怡', '职业法师刘海柱']

my_list.append('杨过')
my_list.append('小龙女')
my_list.append('古龙')
print(my_list)


print(my_list[2:4])
# x:y:n 表示从哪到哪
# x不写，从头开始都要
print(my_list[-1:-4:-1])

# todo  x:y:n x、y 是下标，从哪到哪
# 如果 n前边有减号，表示从右往左找
print(my_list[-1:2:-1])
# 和上边是相同的 2和-4都是下标，两个下标指向的是同一个元素！
print(my_list[-1:-4:-1])

# todo x:y 是下标！ 他俩的范围如果为空 就输出 []空列表
print(my_list[-1:20:-1])
print(my_list[-1:20])

print(my_list[1:2:-1])
print(my_list[0:20:-1])