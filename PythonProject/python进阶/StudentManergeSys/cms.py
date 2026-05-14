from student import Student

class Cms:

    def __init__(self):
        self.student_list=[]
        self.load_student()


    @staticmethod
    def show_operate_view():
        view_str="""
        学生管理系统2.0
        1.添加学生
        2.修改学生
        3.删除学生
        4.查询学生
        5.查询所有学生
        6.保存信息到文件
        0.退出系统
        """
        print('*'*20)
        print(view_str)
        print('*'*20)

    def start(self):
        s1 = Student('小明', 18, '男', '10086', '算法工程师')
        self.student_list.append(s1)
        s2 = Student('小灰', 18, '男', '10010', '程序员')
        self.student_list.append(s2)
        s3 = Student('小红', 16, '女', '10000', '程序媛')
        self.student_list.append(s3)



        while True:
            Cms.show_operate_view()
            user_input=input('请输入操作功能编号：')
            if user_input=='1':
                print('执行功能1.添加学生')
                self.add_student()
            elif user_input=='2':
                print('执行功能2.修改学生')
                self.update_student()
            elif user_input=='3':
                print('执行功能3.删除学生')
                self.del_student()
            elif user_input == '4':
                print('执行功能4.查询指定学生')
                self.get_one_student()
            elif user_input == '5':
                print('执行功能5.查询所有学生')
                self.get_all_student()
            elif user_input == '6':
                print('执行功能6.保存学生信息到文件')
                self.save_student()
            elif user_input == '0':
                user_input=input('确定退出输入y，继续使用输入n：')
                if user_input=='y':
                    print('执行功能0.退出系统')
                    break
                else:
                    continue


    def add_student(self):
        name=input('请输入要添加的姓名')
        age=int(input('请输入要添加的年龄'))
        gender = input("请输入要添加的性别:")
        mobile = input("请输入要添加的联系方式:")
        description = input("请输入要添加的简介信息:")

        student=Student(name,age,gender,mobile,description)
        # print(student)

        self.student_list.append(student)
        print('学生信息添加成功')

    def del_student(self):
        del_stu=input('请输入要删除的学生姓名：')
        for stu in self.student_list:
            if stu.name==del_stu:
                self.student_list.remove(stu)
                print(f"学生信息删除成功{stu.name}")
                break
        else:
            print('删除学生信息不存在')

    def update_student(self):
        up_name=input("请输入需要修改的学生姓名：")
        for stu in self.student_list:
            if stu.name==up_name:
                stu.age = input("请输入需要修改的年龄：")
                stu.gender = input("请输入需要修改的性别：")
                stu.mobile = input("请输入需要修改的手机号：")
                stu.description = input("请输入需要修改的描述：")
                print('修改后的学生信息',stu)
                break
        else:
            print('修改学生不存在')


    def get_one_student(self):
        query_name = input("请输入要查询的学生姓名:")
        # 2.遍历学员数据列表，学员存在则输出信息否则提示不存在
        for stu in self.student_list:
            if query_name in stu.name:
                print(stu)
                break
        else:
            print("您要查找的学生不存在...")

    def get_all_student(self):
        print('\t姓名\t年龄\t性别\t手机\t备注')
        for student in self.student_list:
        # print("学生信息:", student)
            print(f'\t{student.name}\t{student.age}\t{student.gender}\t{student.mobile}\t{student.description}')

    def save_student(self):

        save_info=open('student.txt','w',encoding='utf-8')
        with open('student.txt','w',encoding='utf-8') as fw:
            for stu in self.student_list:
                fw.write(str(stu.__dict__))
                # fw.write('\n')


    def load_student(self):
        try:
            student_info = open('student.txt', 'r', encoding='utf-8')
        except:
            student_info = open('student.txt', 'w', encoding='utf-8')

        # contents = student_info.readlines()
        contents = student_info.read()

        # print(contents)
        if len(contents)==0:
            contents='[]'
        datas = eval(contents)
        self.student_list= [Student(i['name'], i['age'], i['gender'], i['mobile'], i['description']) for i in datas]
        print('结果',self.student_list)
        student_info.close()


if __name__ == '__main__':
    # Cms.show_operate_view()
    Cms().start()