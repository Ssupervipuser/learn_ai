"""
 [
     {'id':'heima001', 'name':'刘亦菲', 'tel': '111'},
     {'id':'heima002', 'name':'高圆圆', 'tel': '222'}
 ]
- 需求：
1. 先打印提示界面(1-6的数字), 让用户选择他/她要进行的操作.
2. 当用户选择1的时候, 实现操作: 添加学生号, 姓名, 手机号, 学生id必须唯一.
3. 当用户选择2的时候, 实现操作: 根据编号删除学生
4. 当用户选择3的时候, 实现操作: 根据编号修改学生姓名, 手机号.
5. 当用户选择4的时候, 实现操作: 根据姓名查询单个学生信息.
6. 当用户选择5的时候, 实现操作: 查询所有学生信息.
7. 当用户选择6的时候, 实现操作: 退出系统.
"""
# 定义列表、报错所有学生的信息
student_list =  [
     {'id':'heima001', 'name':'刘亦菲', 'tel': '111'},
     {'id':'heima002', 'name':'高圆圆', 'tel': '222'}
 ]

# 1. 先打印提示界面(1-6的数字), 让用户选择他/她要进行的操作.
def run():
    """
    程序主逻辑！
    :return: None
    """
    while 1:
        info_str = """请根据提示输出：
        1. 添加学生信息
        2. 根据学生id删除学生信息
        3. 根据学生id修改学生信息
        4. 根据学生姓名获取该学生的全部信息
        5. 展示所有学生信息
        6. 退出系统
        """
        while 1:
            print(info_str)
            try:
                num_str = int(input('请输入操作的编号：')) # str-->int
                print(num_str)
                break
            except:
                print('请规范输入！！')


        # 7. 当用户选择6的时候, 实现操作: 退出系统.
        if num_str == 6:
            break
        # 1. 添加学生信息
        elif num_str == 1:
            add_student()
        # 2. 根据学生id删除学生信息
        elif num_str == 2:
            del_student()
        # 3. 根据学生id修改学生信息
        elif num_str == 3:
            update_student()
        # 4. 根据学生姓名获取该学生的全部信息
        elif num_str == 4:
            get_student_info()
        # 5. 展示所有学生信息
        elif num_str == 5:
            print_students()
        else:
            print('请输入正确编号！')

# 2. 当用户选择1的时候, 实现操作: 添加学生号, 姓名, 手机号
# 学生id必须唯一.
def add_student():
    # 添加学生信息

    # 学生id必须唯一
    # 获得当前所有学生的id放列表中
    student_id_list = []
    for student_info_dict in student_list:
        student_id_list.append(student_info_dict['id'])
    print('上一个学生id是：{} \n'.format(student_id_list[-1]))
    while 1:
        student_id = input('输入学生的id：')
        # 判断输入的学生的id是否在学生id列表中
        if student_id in student_id_list: # 在里边、重复了！
            print('学生id重复了！请换一个！')
        else: # 不重复就终止循环
            break

    name = input('输入学生的姓名：') # 接收输入
    tel = input('输入学生的手机号：') # 接收输入

    # 组装学生信息字典
    student_info = {
        'id': student_id,
        'name': name,
        'tel': tel
    }
    # 将学生信息字典添加到所有学生列表中
    student_list.append(student_info)
    print(student_list)

# 3. 当用户选择2的时候, 实现操作: 根据编号删除学生
# def del_student():
#     # 删除学生信息
#     # 获得当前所有学生的id放列表中
#     student_id_list = []
#     for student_info_dict in student_list:
#         student_id_list.append(student_info_dict['id'])
#     print('所有学生的id是：{} \n'.format(student_id_list))
#     # 接收要删除的id
#     student_id_str = input('请输入要删除学生的id：')
#
#     # 把下标和元素成对的拿出来
#     for i, student_id in enumerate(student_id_list):
#         if student_id == student_id_str:
#             break # 此时 i 就是要删除学生的下标
#
#     # 利用下标i获得整个学生信息字典
#     for j, student_dict in enumerate(student_list):
#         if j == i:
#             student_info_dict = student_dict
#
#     # 删除学生信息
#     student_list.remove(student_info_dict)
#     # del student_list[i]
#
#     print(student_list)

# 3. 当用户选择2的时候, 实现操作: 根据编号删除学生
def del_student(student_id_str=False):
    print('请查看所有学生的信息:\n{}'.format(student_list))
    # todo 默认值参数的空置
    if student_id_str == False: # 直接删除学生信息时执行这里
        student_id_str = input('请输入要删除的学生id：')
    else: # 被update_student调用时执行这里
        student_id_str = student_id_str
    # 遍历学生列表，通过key获取学生id，和输入的id做比较
    for student_dict in student_list:
        if student_dict['id'] == student_id_str:
            # 相同就删除
            student_list.remove(student_dict)
            # 删除之后就终止遍历
            break
    print(student_list)


# 4. 当用户选择3的时候, 实现操作: 根据编号修改学生姓名, 手机号.
def update_student():
    print('请查看所有学生的信息:\n{}'.format(student_list))
    student_id_str = input('请输入要更改信息的学生id：')
    del_student(student_id_str) # todo 先删除、再添加
    add_student() # todo 直接调用添加学生信息的函数


# 5. 当用户选择4的时候, 实现操作: 根据姓名查询单个学生信息.
def get_student_info():
    student_name = input('请输入学生的姓名：')
    # 通过遍历学生列表，学生字典key和输入的姓名做比较，找到了就退出循环
    for student_dict in student_list:
        if student_dict['name'] == student_name:
            print(student_dict)
            break
    else: # break不执行的时候 else才执行
        print('查无此人')


# 6. 当用户选择5的时候, 实现操作: 查询所有学生信息.
def print_students():
    # print(student_list)
    for student_dict in student_list:
        print('学生id：{}，学生姓名：{}，手机号：{}'.format(
            student_dict['id'],
            student_dict['name'],
            student_dict['tel']
        ))


if __name__ == '__main__':
    # todo 下边为测试
    # add_student()
    # print(student_list)

    # del_student()
    # update_student()

    # get_student_info()
    # print_students()

    # todo 程序入口
    run()