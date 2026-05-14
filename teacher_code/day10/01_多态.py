
class Animal:
    # def speak(self):
    #     pass
    pass

class Dog(Animal):
    def speak(self):
        print('汪汪汪')

class Cat(Animal):
    def speak(self):
        print('喵喵喵')

# todo 会发生多态的函数
# animal: Animal 表示 animal这个传入的参数的类型是 Animal类
# animal即是Animal类型的，也是自己具体的一个子类型（Dog、Cat）
def make_noise(animal: Animal): # 同一函数、传入不同的参数、结果不同
    # todo 不能的对象、执行相同的speak函数，结果不同
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


# todo 类型检查、类型规定
def bar(a:int, b:int):
    """
    :param a: int类型
    :param b: int类型
    :return: ab的和
    """
    return a+b


ret = bar('1', '2')
print(ret)