

# 定义一个类
class Car:

    def run(self):
        # todo self是指代实例化后的具体的那个对象
        # self是：<__main__.Car object at 0x000001FCEFD087D0>
        print(f'self是：{self}')
        # Car 车这一类 都具有的函数方法：跑
        print('车跑起来了')

    def work(self):
        # todo self即然是实例化后的具体对象，那就可以在定义类的时候，调用类里边的属性和方法
        # 实例化对象.run函数执行
        self.run() # 跑起来了


# print(type(Car()))
# __main__.Car 表示 当前.py文件中的Car类的对象
# <class '__main__.Car'>

# 实例化一个具体的车对象
# car 是对象名
car1 = Car()
# 实例对象调用自己本身所在类的方法函数
# car1.run() # 这个车跑起来了
# print(car1)
car1.work()

# 实例化一个具体的车对象
# car 是对象名
# car2 = Car()
# # 实例对象调用自己本身所在类的方法函数
# car2.run() # 这个车跑起来了
# print(car2)
