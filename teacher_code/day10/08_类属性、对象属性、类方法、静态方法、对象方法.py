""" todo
对象.对象属性
类名.类属性

对象.对象方法函数()
类名.类方法函数()

类名.静态方法函数()
"""

class Student(object):
    # 类属性
    school = '黑马程序员'
    # todo 类属性，所有对象都共有，对象属性由对象独有
    def __init__(self, name, age): # 有self参数的就是对象方法
        # 对象属性
        self.name = name
        self.age = age
        print(self) # 实例对象

    @classmethod
    def show1(cls): # 类方法：有classmethod装饰器、有cls参数
        # 操作类属性：类属性的修改和查看
        Student.school = '白马会'
        print(Student.school)
        print(cls) # 类本身

    @staticmethod
    def show2(): # 静态方法：和类、对象都没有关联！
        # 完全是写手觉得这个函数放这里逻辑上看着顺眼
        print('不操作类属性、不操作对象属性')

    def show3(self):
        print('对象方法函数')


# todo 对象方法、对象属性
s = Student(name='张三', age=18)
s.show3() # 实例对象.对象方法函数()
s.name = '张三丰'
print(s.name)

# todo 类属性、类方法
Student.show1() # 类名.类方法函数()
Student.school = '河马会' # 类属性共有！永久改变
print(Student.school)

# todo 静态方法
Student.show2() # 类名.静态方法函数()

print(Student.__dict__)
print(Student('1', 1).__dict__)
