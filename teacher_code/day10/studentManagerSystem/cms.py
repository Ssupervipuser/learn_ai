import time # python内置包

class Cms:
    # 学生管理系统类
    # 增删改查学生信息
    # 从文件中保存、读取学生信息
    # 显示界面、退出系统
    def __init__(self):
        self.start_sleep_time = 1 # 假的启动等待时间
        # 初始化所有学生的信息
        self.students_list = []

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
        # 模拟系统启动用户等待
        print('启动中，请等待...')
        time.sleep(self.start_sleep_time) # 程序在这里停住1.5s

        while 1:
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
        pass

    def del_student(self):
        # 删除一个学生
        pass

    def update_student(self):
        # 修改一个学生
        pass

    def get_1_student(self):
        # 查询一个学生
        pass

    def get_all_students(self):
        # 查询全部学生
        pass

    def save_student(self):
        # 学生信息保存到文件
        pass



if __name__ == '__main__':
    # Cms.show_operate_view()

    # 测试CMS()的start()
    Cms().start()