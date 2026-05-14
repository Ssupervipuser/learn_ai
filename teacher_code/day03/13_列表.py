
# todo list列表，下标从0开始（下标就是顺序，从0开始）
# 下标也可以倒着数：从 -1 开始 （右边第一个下标是 -1， 第二个是-2）
a_list = ['刘海柱', '张三', '李四', 18, True, None]

# 按照下标去获取list列表中的值
ret = a_list[0]
print(ret)
print(a_list[-1])
print(a_list[5])

# 空列表
b_list = []
print(type(b_list)) # <class 'list'>


# 列表嵌套
school_list = [
    ['郑州大学', '清华大学'],
    ['北京大学', '河南大学'],
    ['洛阳师范', '河南工程大学']
]
# ['郑州大学', '清华大学'], <class 'list'>
# print(school_list[0], type(school_list[0]))
# school_0_list = school_list[0]
# print(school_0_list[0])

# 列表嵌套列表的时候，可以一直用下标去最里边的元素
print(school_list[0][0])
