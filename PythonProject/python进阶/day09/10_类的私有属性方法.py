
class Master:
    def __init__(self):
        self.kongfu = '师父配方'
    def makeCake(self):
        print(f'{self.kongfu}做蛋糕')

class School:
    def __init__(self):
        self.kongfu = '学校配方'
    def makeCake(self):
        print(f'{self.kongfu}做蛋糕')

class Tudi(School, Master):
    def __init__(self):
        # 两个下划线开头的变量，是该类的私有属性，继承不了、实例化对象也不能用！
        # todo 私有属性只能在类的定义的内部使用
        self.__money = 2000

    def getMoney(self):
        # todo 想让实例化的对象、继承的子类对象使用私有属性的话，需要专门定义方法
        print(self.__money)

    def __setMoney(self):
        # todo 私有方法，只能自己这个类内部使用
        self.__money += 1000

    def showSetMoney(self):
        self.__setMoney()  # 私有方法，只能自己这个类内部使用

    def makeCake(self):
        super().__init__()
        super().makeCake()

class Tusun(Tudi):
    pass


tusun = Tusun()
tusun.showSetMoney()
tusun.getMoney()

tudi = Tudi()
tudi.showSetMoney()
tudi.getMoney()
