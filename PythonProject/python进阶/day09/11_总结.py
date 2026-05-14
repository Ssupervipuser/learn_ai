
"""类 ==> 面向对象：python中，一切皆对象
方法就是函数、属性就是变量！
"""

class Animal(object):
    # 动物类
    def __init__(self):
        # 初始化方法：经常用来定义属性
        self.animal_name = '动物的名字'
        self.animal_weight = 0 # 动物体重质量

    def eat(self):
        print(f'{self.animal_name}吃东西')

class Dog(Animal):
    # Dog继承于Animal类，默认就会有父类的属性和方法
    def run(self):
        print(f'{self.animal_name}奔跑')
    def __bar(self):
        print('私有方法不能被继承、也不能被对象调用')

class TeshuDog(Animal):
    def run(self):
        print(f'{self.animal_name}特殊的奔跑姿势')

class Hasiky(TeshuDog, Dog):
    def run(self):
        print('重新从父类继承过来的同名函数')
        print(f'{self.animal_name} 奔跑')

    def fuleiRun(self):
        TeshuDog.run(self) # 具体父类名.函数()
        Dog.run(self)
        # todo 第一个父类的run函数执行，如果第一个父类没有，就执行第二个父类的run函数
        super().run()

    def fuleiShuxingInit(self):
        self.animal_weight = 30
        print(self.animal_weight) # 30
        super().__init__() # todo 执行父类的初始化函数，导致animal_weight重置为0
        print(self.animal_weight) # 0


    # def getFuleiShuxing(self): # 强行获取父类属性值
    #     print(TeshuDog().animal_weight) # 获取父类具体属性值的方法

    def __init__(self, name):
        self.__age = 0 # 私有属性
        self.animal_name = name # 重写集成于父类的属性
        self.animal_weight = 30

    def __str__(self):
        # print(具体对象) 输出return返回的字符串
        return '这个哈士奇名字叫{}'.format(self.animal_name)

    def __del__(self):
        print('删除对象时，一定会执行这里')

    def brokeHome(self):
        print(f'{self.animal_name}拆家')

    def __skill(self):
        # todo 私有方法
        print('后空翻')

    def showSkill(self):
        # 在这个公有方法中，调用了私有方法
        self.__skill()

    def setAge(self):
        # todo 设置、修改私有属性 __age
        self.__age += 1

    def getAge(self):
        # todo 获取私有属性
        print(self.__age)

# 实例化对象 erha就是一个对象
erha = Hasiky(name='哈哈')
erha.run() # 子类父类同名函数，执行子类的！
erha.eat() # 对象直接调用父类的方法
erha.showSkill() # 调用共用方法、该共用方法中调用了私有方法
erha.setAge() # 调用共用方法、该共用方法中修改了私有属性
erha.getAge() # 调用共用方法、该共用方法中获取了私有属性
print(erha.__dict__) # 对象.__dict__ 获取所有属性、包括私有属性
erha.animal_weight = 40 # 对象.属性 = xxx # 设置、修改属性
print(erha.animal_weight) # 对象.属性 # 获取属性
print(erha)

erha.fuleiRun()
erha.fuleiShuxingInit()

# todo 关于父类执行 init 初始化函数的时机
class A:
    def __init__(self):
        self.a = 'a'
    def printselfa(self):
        print(self.a)

class B(A):
    def __init__(self):
        self.a = 'b'

    def printselfa(self):
        # todo xxx.__init__() 看这里
        print(self.a)
        # 此时，父类的这个函数输出的变量a的值被子类覆盖了
        super().printselfa()
        # 如果想执行父类这个函数，同时该函数里还使用父类的变量
        super().__init__()
        super().printselfa()
        # 此时self.a变量的值 被父类覆盖了
        # 这里要再切换成子类的a这个变量
        self.__init__()
        super().printselfa()

b = B()
b.printselfa()