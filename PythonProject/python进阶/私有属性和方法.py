class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'
        # 定义私有属性
        self.__money = 2000000

    # 定义私有方法
    def __info_print(self):
        print(self.kongfu)
        print(self.__money)

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 徒孙类
class Tusun(Prentice):
    pass


daqiu = Prentice()
# 对象不能访问私有属性和私有方法
# print(daqiu.__money)
# daqiu.__info_print()

xiaoqiu = Tusun()
# 子类无法继承父类的私有属性和私有方法
# print(xiaoqiu.__money)  # 无法访问实例属性__money
# xiaoqiu.__info_print()
