from studentsinfo import students_info

def get_allinfo():
    """todo 5. 查询所有的学生信息
    如果是空列表、就提示没信息
    遍历学生列表，格式化使出每一个学生的信息
    :return:
    """
    print('当前所有学生信息如下：')
    if students_info == []: # 学生信息列表中没数据，就直接提示没信息
        print('无')
    for student in students_info:
        print('学生id：{}，姓名：{}，电话：{}'.format(student['id'], student['name'], student['tel']))
