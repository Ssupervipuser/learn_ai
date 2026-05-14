
class Dog:
    @classmethod
    def eat(cls):
        # 类方法：固定第一个参数是cls，头上要加@classmethod装饰器
        # 1. 用来定义这个类中的工具函数
        # 2. 操作类属性、【不操作对象属性】！
        print('狗都喜欢吃骨头')

    def run(self):
        self.name = 'xxxx'
        # 对象方法
        Dog.eat()


Dog.eat() # 类方法函数的调用执行方式
Dog().run()