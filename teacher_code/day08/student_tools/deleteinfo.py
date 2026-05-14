from studentsinfo import students_info

def delete_info():
    """ todo 2. 删除学生
    遍历每一个学生字典，根据学生字典的key中的id，判断是否为要删除的学生字典
    如果是就删除，提前终止函数；全部遍历完毕都不是，提示不存、结束函数
    :return:
    """
    # 获取要删除的学生id
    id = input('请录入您要删除的学生的编号: ')
    # 遍历每一个学生字典，根据学生字典的key中的id，判断是否为要删除的学生字典
    # 如果是就删除，提前终止函数；全部遍历完毕都不是，提示不存、结束函数
    for student in students_info:
        # 判断要删除的id是否在学生信息中
        if student['id'] == id:
            # 从学生列表中，删除指定的学生字典
            students_info.remove(student)
            print('根据您录入的学生编号, 已删除该学生信息')
            return # 提前终止函数
    print('您要删除的学生不存在，请重新操作')