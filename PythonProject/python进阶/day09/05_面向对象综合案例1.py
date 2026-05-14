# 当前100kg
# 跑步：减少 0.5
# 吃喝：增加 2

class Xiaoming:

    def __init__(self):
        # 当前100kg
        self.tizhong = 100

    def paobu(self):
        # 跑步：减少 0.5
        self.tizhong = self.tizhong - 0.5
        # self.tizhong -= 0.5
        print(self.tizhong)

    def chihe(self):
        # 吃喝：增加 2
        self.tizhong = self.tizhong + 2
        print(self.tizhong)

    def __str__(self):
        return str(self.tizhong)


xiaoming = Xiaoming() # 实例化对象
xiaoming.chihe()
xiaoming.paobu()
print(xiaoming)