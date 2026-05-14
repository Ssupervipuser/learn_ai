import sys
# todo 在程序入口的所在文件中，把需要搜索包模块的路径添加到sys.path
# 代码最开始就添加
sys.path.append('D:/BaiduNetdiskDownload/1.python基础/code/day08/student_tools')
# print(sys.path)
# todo 之后就按pycharm能够运行的方式去导包即可

from student_tools.addinfo import add_info
from student_tools.deleteinfo import delete_info
from student_tools.updateinfo import update_info
from student_tools.getstudentinfo import get_studentinfo
from student_tools.getallinfo import get_allinfo

# 0. 定义函数 print_info()  , 打印提示信息
def print_info():
    # 打印提示信息
    print('='*20)
    print('学生管理系统功能如下，稍后请输入编号')
    print('1. 添加学生')
    print('2. 删除学生')
    print('3. 修改学生信息')
    print('4. 查询单个学生信息')
    print('5. 查询所有的学生信息')
    print('6. 退出系统')


def main():
    """todo 程序运行的主干逻辑
    判断输入1-6哪一个数字（str），执行相应的功能函数
    :return:
    """
    while True:
        print_info() # 打印提示各种功能信息：1-6
        num = input('请输出要操作的编号：')

        if num == '1':
            add_info() # 添加学生
        elif num == '2':
            delete_info() # 删除学生
        elif num == '3':
            update_info() # 修改学生信息
        elif num == '4':
            get_studentinfo() # 获取一个学生的信息
        elif num == '5':
            get_allinfo() # 输出所有学生的信息
        elif num == '6':
            return # 退出系统，return直接终止函数、while循环也跟着函数一起终止了
        else: # 输出其他的情况
            print('输入不正确请核对后再输入')


if __name__ == '__main__':

    # 执行主逻辑！
    # 程序入口
    main()