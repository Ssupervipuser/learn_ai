from studentsinfo import students_info # 导入存储学生信息的列表

def add_info():
    """ todo 1. 添加学生信息
    通过遍历每一个学生字典，判断id是否重复，如果重复提前终止函数
    如果不重复，就组装学生信息字典，并添加到学生列表中
    :return: None
    """
    # 接收学生的id
    new_id = input('请录入您要添加的学生的编号: ')
    # 识别输入的学生id是否重复，如果重复，提前结束函数
    # 遍历学生列表，每一次获得一个学生的字典
    for student in students_info:
        # 基于key是id，获得学生的id
        # 判断是否和录入的一致
        if student['id'] == new_id:
            # 如果一致
            print('您录入的学生编号已存在, 请重新操作')
            return # 函数提前结束
    # 如果没有重复 就继续输入学生姓名和电话
    new_name = input('请录入您要添加的学生的姓名: ')
    new_tel = input('请录入您要添加的学生的手机号: ')
    # 组装一个学生的信息字典
    dict_info = {'id': new_id, 'name': new_name, 'tel': new_tel}
    # 向学生列表中添加学生信息字典
    students_info.append(dict_info)
    print(students_info)

if __name__ == '__main__':
    add_info()