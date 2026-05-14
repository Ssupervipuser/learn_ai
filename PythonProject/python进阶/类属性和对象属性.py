#定义一个 student类
from os import name


class Student(object):
    #定义类属性
    teacher_name='水镜先生'

    #定义对象属性，即写到init方法中的属性
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #定义str魔法方法，输出对象信息
    def __str__(self):
        return f'姓名：{self.name} 年龄：{self.age}'


if __name__ == '__main__':
    #1.对象属性
    s1=Student('曹操',38)
    s2=Student('曹操',38)

    #修改s1的属性值
    s1.name='许褚'
    s1.age=40

    print(f's1:{s1}')
    print(f's2:{s2}')
    print('-'*23)

    #2.类属性
    #类属性可以通过类名. 和 对象名. 的方式调用
    print(Student.teacher_name)
    print(s1.teacher_name)
    print(s2.teacher_name)
    #尝试用对象名.的方式来修改类属性
    s1.teacher_name='nb'
    print(s1.teacher_name)     # nb
    print(s2.teacher_name)     #水镜先生
    print('-'*23)
    '''
    我们发现使用对象名.的方式修改类属性是行不通的s1.teacher_name='nb'只是再s1的内存中添加了
    一个新的属性nb
    '''

    #3尝试使用类名.修改类属性
    Student.teacher_name = 'nb'
    print(s1.teacher_name)  # nb
    print(s2.teacher_name)  # nb
