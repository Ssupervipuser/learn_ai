class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(object):
    # 学校类
    def __init__(self):
        self.kongfu = '黑马煎饼果子配方'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class Prentice(School, Master):
    # todo 多继承，多个父类如果有同名属性、方法
    # todo 子类使用的是左边的父类的同名属性和方法
    def __init__(self):
        self.kongfu = '独门配方'
    def make_cake(self):
        # 子类重写了父类的同名函数
        # 继承时子类父类有同名属性或方法时，子类对象默认使用的是子类的
        print(f'运用{self.kongfu}制作煎饼果子')

    # todo 子类中还想用父类的同名方法的实现方式
    def make_master_cake(self):
        Master.__init__(self) # 固定写法：父类名.init(self)
        Master.make_cake(self) # 固定写法：父类名.函数(self)

    def make_school_cake(self):
        School.__init__(self) # 固定写法：父类名.init(self)
        School.make_cake(self) # 固定写法：父类名.函数(self)

    def make_old_cake(self):
        # todo super().init() 初始化最左边的父类
        # todo super().make_cake() 执行最左边父类的函数方法
        # todo 此时 super() 就是 School 这个类
        super().__init__()
        super().make_cake() # 调用父类的函数方法


# 查看继承的顺序：类名.mro
print(Prentice.__mro__)
print(Prentice.mro())

xiaoming = Prentice() # 实例化对象，具体的人：小明
xiaoming.make_cake() # 小明自己的摊煎饼的方法
print(xiaoming.kongfu) # 小明自己的属性

xiaoming.make_master_cake() # 小明按师父的方法做煎饼果子
xiaoming.make_school_cake() # 小明按学校的方法做煎饼果子

xiaoming.make_old_cake() #


