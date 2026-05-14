#定义函数print_info()，打印提示信息

def print_info():
    print('='*20)
    print('学生管理系统功能如下，请稍后输入编号')
    print('1.添加学生')
    print('2.删除学生')
    print('3.修改学生信息')
    print('4.查询单个学生信息')
    print('5.查询所有的学生信息')
    print('6.退出系统')
    print('='*20)



#1.自定义函数 add_info()，实现添加学生（学生编号，学生姓名，手机号，）编号必须唯一
#数据格式[{'id':'heima001', 'name':'刘亦菲', 'tel': '111'}, {'id':'heima002', 'name':'高圆圆', 'tel': '222'}]

students_info=[]
#添加学生号，姓名，手机号，学生id必须唯一
def add_info():
    #提示用户录入学生id并接收
    new_id=input('请录入您要添加的学生编号')

    #遍历学生列表，获取到每个学生信息，根据id判断，如果已经存在，则不添加
    for student in students_info:
        if student['id'] == new_id:
            print('您录入的学生编号已经存在，请重新输入')
            return #结束函数

    #提示用户录入的学生姓名、手机号并接收
    new_name=input('请录入您要添加的学生的姓名：')
    new_tel=input('请录入您要添加的学生的手机号：')

    dict_info={'id':new_id,'name':new_name,'tel':new_tel}
    #字典类型的学生信息，添加到学生列表中
    students_info.append(dict_info)


#2.根据编号删除学生
def delete_info():
    id=input('请录入您要删除的学生编号')
    #遍历学生列表，获取到每个学生信息，根据id判断，如果已经存在，就删除该学生信息
    for student in students_info:
        if student['id'] == id:
            students_info.remove(student)
            print('根据您录入的学生编号，已删除该学生的信息')
            return  #删除成功结束函数
    #不存在就提示，同时函数结束
    print('您要删除的学生不存在，请重新操作')

#3.根据编号修改学生姓名，手机号
def update_info():
    id=input('请录入您要修改信息的学生编号：')
    #遍历学生列表，获取到每个学生信息，根据id判断，如果存在就删除该学生信息
    for student in students_info:
        if student['id'] == id:
            print()























