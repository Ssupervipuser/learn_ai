from studentsinfo import students_info

def get_studentinfo():
    """todo 4. 查询单个学生信息
    通过比较 输入的学生姓名 和 学生字典['name'] ，再打印输出遍历出来的那一个符合条件的学生字典
    :return:
    """
    name = input('请录入要查询信息的学生姓名: ')
    for student in students_info:
        # 遍历出来的学生字典[姓名] 是否和 输出的姓名 相等
        if student['name'] == name:
            # 如果相等、说明找到了、就打印输出
            print('学生的信息是 {}'.format(student))
            return # 找到了之后提前终止函数
    # 遍历结束都没有找到，就提示不存在
    print('您要查询信息的学生不存在，请重新操作')