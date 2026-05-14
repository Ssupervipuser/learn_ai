import time # python内置包
import traceback
from student import Student

class Cms:

    # 学生管理系统类
    # 增删改查学生信息
    # 从文件中保存、读取学生信息
    # 显示界面、退出系统
    def __init__(self):
        self.start_sleep_time = 1 # 假的启动等待时间
        # 确定保存文件的路径
        self.filepath = './students.data'
        # 初始化所有学生的信息
        self.students_list = []
        # todo 这个函数一执行，就会有self.students_list列表
        #  该列表的元素是 Student() 对象
        self.load_student() # 加载文件中的数据 到 self.students_list列表中


    def add_demo_stu(self):
        # 添加用于测试系统的学生数据
        s1 = Student('张三丰', 19, '男', '12121', '备注')
        self.students_list.append(s1)
        s2 = Student('张四丰', 19, '男', '12121', '备注')
        self.students_list.append(s2)
        s3 = Student('张五丰', 19, '男', '12121', '备注')
        self.students_list.append(s3)

    @staticmethod
    def show_operate_view():
        """Cms.show_operate_view()
        展示管理系统的界面，提示信息
        :return: None
        """
        print('*' * 20)
        view_str = """学生管理系统V2.0
        1. 添加学生
        2. 修改学生
        3. 删除学生
        4. 查询一个学生
        5. 查询所有学生
        6. 保存信息到文件
        7. 退出系统
        """
        print(view_str)
        print('*' * 20)

    def start(self):
        # 程序入口函数、管理系统的主干逻辑
        # todo 添加测试数据
        # self.add_demo_stu()
        # 模拟系统启动用户等待
        print('启动中，请等待...')

        while 1:
            time.sleep(self.start_sleep_time) # 程序在这里停住self.start_sleep_times
            # 显示菜单、提示信息
            Cms.show_operate_view()
            # 接收用户的键盘输入
            number_str = input('请输入要操作功能的编号：')
            # 根据输入进行判断，不同的输入执行相应的功能函数方法
            if number_str == '1':
                print('执行功能1，添加学生')
                self.add_student()
            elif number_str == '2':
                print('执行功能2，修改学生')
                self.update_student()
            elif number_str == '3':
                print('执行功能3，删除学生')
                self.del_student()
            elif number_str == '4':
                print('执行功能4，查询特定学生')
                self.get_1_student()
            elif number_str == '5':
                print('执行功能5，查询所有学生')
                self.get_all_students()
            elif number_str == '6':
                print('执行功能6，保存信息到文件')
                self.save_student()
            elif number_str == '7':
                # 选择退出时，让用户再次确认
                while 1:
                    flag = input('确认退出系统吗？（Y/N）')
                    if flag == 'Y':
                        print('感谢使用，谢谢再见！')
                        return # 直接结束整个start()函数
                    elif flag == 'N':
                        print('不退出继续执行')
                        break # 退出内层循环
                    else:
                        print('输入有误重新输入：')
            else:
                print('输入有误，请重新输入')

    def add_student(self):
        # 添加一个学生
        # 1. 接受输入
        name = input('输入学生姓名：')
        age = int(input('输入学生年龄：'))
        gender = input('输入学生性别：')
        mobile = input('输入学生手机号：')
        description = input('输入学生备注信息：')
        # 2. 创建学生对象
        student = Student(
            name, age, gender, mobile, description
        )
        # 3. 添加学生信息到列表中
        self.students_list.append(student) # 添加的是学生对象
        print('已添加：', student)


    def del_student(self):
        # 删除一个学生：根据姓名删除
        # 1. 获取用户输入的要删除的学生姓名
        del_name = input('输入要删除的学生姓名：')
        # 2. 遍历学生列表，存在就删除、退出遍历，不存在就提示不存在
        for stu in self.students_list:
            if del_name == stu.name:
                self.students_list.remove(stu)
                print(f'成功删除{stu.name}的信息')
                break # for循环一旦break就不执行后边的else
        else: # for循环正常结束，就执行这里
            print('要删除的学生不存在')


    def update_student(self):
        # 修改一个学生：根据姓名
        # 1. 输入要修改信息的学生姓名
        update_name = input('输入要修改信息的学生姓名：')
        # 2. 遍历学生，找到要修改的，进行修改
        for stu in self.students_list:
            if update_name == stu.name:
                stu.age = int(input('年龄：'))
                stu.gender = input('性别：')
                stu.mobile = input('手机号：')
                stu.description = input('备注信息：')
                print('修改完的学生信息：', stu)
                break
        else: # break时，这里就不执行
            print('要修改信息的学生不存在')

    def get_1_student(self):
        # 查询一个学生：根据姓名
        # 1. 输入查询的学生姓名
        stu_name = input('输入要修改信息的学生姓名：')
        # 2. 遍历学生，找到查询的学生，进行展示
        for stu in self.students_list:
            if stu_name == stu.name:
                print('查询到信息为：', stu)
                break
        else:
            print('要查询信息的学生不存在')


    def get_all_students(self):
        # 查询全部学生
        print('\t姓名\t年龄\t性别\t手机号\t备注')
        for stu in self.students_list:
            # print(stu)
            print(f'\t{stu.name}\t{stu.age}\t{stu.gender}\t{stu.mobile}\t{stu.description}')

    def save_student   (self):
        # 学生信息保存到文件
        # 2. 打开文件并写入数据
        new_list = []
        with open(self.filepath, 'w', encoding='utf8') as fw:
            # 3. 遍历每一个学生对象，构造成列表，添加到新列表中
            for stu in self.students_list:
                # 把对象所有属性变成由名字和值构成的字典
                # 每个学生信息字典添加到列表中
                new_list.append(stu.__dict__)
            # 新列表转成字符串之后，写入文件中
            fw.write(str(new_list))
            print(f'信息已经保存到路径【{self.filepath}】中')

    def load_student(self):
        # 从文件中读取字符串，转成列表（列表中元素转成字典）
        # 覆盖到 self.students_list 中
        try: # 文件不存在的时候没法打开读，会报错，所以try
            with open(self.filepath, 'r', encoding='utf8') as fr:
                students_list_str = fr.read() # 读取所有
                students_lst = eval(students_list_str) # 转换类型
                for stu_dict in students_lst: # 遍历出每一个学生信息字典
                    # todo 这里可以尝试修改Student类，使用**kwargs字典不定长参数
                    # 字典-->学生对象
                    stu = Student(stu_dict['name'], stu_dict['age'], stu_dict['gender'], stu_dict['mobile'], stu_dict['description'])
                    stu = Student(**stu_dict)
                    self.students_list.append(stu) # 学生对象添加到列表中
        except: # 如果r读文件报错，说明文件不存在，说明是第一次启动，于是创建文件
            # print(traceback.format_exc())
            with open(self.filepath, 'w', encoding='utf8') as fw:
                self.students_list = [] # 初始化 学生列表


if __name__ == '__main__':
    # Cms.show_operate_view()

    # 测试CMS()的start()
    # Cms().start()
    cms = Cms()
    cms.start()
    # cms.add_student() # 添加
    cms.get_all_students() # 查所有
    # cms.del_student() # 删
    # cms.get_all_students() # 查所有