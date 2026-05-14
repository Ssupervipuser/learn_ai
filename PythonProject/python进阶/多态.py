class Animal(object):
    pass

class Dog(Animal):
    def speak(self):
        print('wwww')

class Cat(Animal):
    def speak(self):
        print('喵喵')

def make_noise(animal):
    animal.speak()


if __name__ == '__main__':
    #实例化对象
    dog = Dog()
    cat = Cat()

    make_noise(dog)
    make_noise(cat)