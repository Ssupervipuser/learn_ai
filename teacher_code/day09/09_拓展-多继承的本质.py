
class Master:
    def __init__(self):
        self.kongfu = '师父配方'
    def makeCake(self):
        print(f'{self.kongfu}做蛋糕')

class School:
    def __init__(self):
        self.kongfu = '学校配方'
        self.__money = 200
    # def makeCake(self):
    #     print(f'{self.kongfu}做蛋糕')

class Tudi(School, Master):
    def makeCake(self):
        super().__init__()
        super().makeCake()
        # todo 1. 此时，小明使用的是学校makeCake函数
        #  但学校自己没有这个函数，按照继承顺序，学校从师父继承了做蛋糕
        #  学校不能自己直接做蛋糕
        # todo 2. 此时，小明使用的是师父makeCake函数
        #  用师父makeCake函数时，self.kongfu这个变量使用的是小明的变量
        #  小明的self.kongfu来源于学校
        #  小明使用makeCake函数时，函数来源于师父、变量来源于学校
        # 获得父类的所有属性、包括私有的，返回字典
        print(super().__dict__) # {'kongfu': '学校配方'}


xiaoming = Tudi()
xiaoming.makeCake() # 学校配方做蛋糕


s = School()
print(s.__dict__)
print('*'*10)

# 定义父类.
class Master:
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用 {self.kongfu} 制作煎饼果子')

class School:
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'
    def make_cake(self):
        print(f'运用 {self.kongfu} 制作煎饼果子')

# 定义子类
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'
        self.__money = 5000
    def __make_cake(self):
        # 私有方法
        self.__init__() # 在类定义的内部重置属性
        print(f'运用{self.kongfu}制作煎饼果子')
    # 通过公有方法来调用私有方法，或操作私有属性
    def make(self):
        print('执行子类的私有__make_cake方法')
        self.__make_cake()
    def set_money(self, money):
        self.__money = money
    def get_money(self):
        return self.__money

# 定义子类的子类
class Tusun(Prentice):
    pass

# 5.测试.
xiaohei = Tusun()
xiaohei.make()
print(xiaohei.get_money())
xiaohei.set_money(100)
print(xiaohei.get_money())

xiaohei.make()
print(xiaohei.get_money())