
class Father(object):
    def __init__(self):
        self.gender = '男'
    def walk(self):
        print('溜达')

class Son(Father): # 声明集成于Father父类
    def playgame(self):
        print('打游戏')


s = Son()
s.walk()
print(s.gender)
s.playgame()