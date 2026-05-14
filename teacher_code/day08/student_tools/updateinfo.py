from studentsinfo import students_info

def update_info():
    """ todo 3. 修改学生信息
    根据输入的id，遍历学生列表，直到找到要修改的学生字典，再修改
    :return:
    """
    id = input('请录入您要修改信息的学生的编号: ')

    # student==> 学生字典 ；students_info==>所有学生字典构成的列表
    for student in students_info:
        #  判断 按key取出id的值 == 输入的要更新修改的学生的id
        if student['id'] == id:
            print('学生信息为 {}'.format(student))
            # 接收输入的学生姓名、电话
            new_name = input('请录入学生修改后的姓名: ')
            new_tel = input('请录入学生修改后的手机号: ')
            # 组装数据并更新信息：字典按key重新赋值（修改值）
            student['name'] = new_name
            student['tel'] = new_tel

            print('此时学生信息为 {}'.format(students_info))
            return # 修改完了、提前终止函数

    # 如果遍历一遍找不到，就提示不存在
    print('您要修改信息的学生不存在，请重新操作')