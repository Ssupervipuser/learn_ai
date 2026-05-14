class AC:
    # todo 抽象类、规定接口的标准，比如：
    #  函数（函数名、参数和参数类型、返回值和返回值类型）
    def cool_wind(self):
        # 制冷
        pass

    def hot_wind(self):
        # 制热
        pass

    def swing(self):
        # 摆风
        pass

class MideaAC(AC):
    # 子类、具体实现接口功能的类
    def cool_wind(self):
        # 制冷
        print('midea制冷')

    def hot_wind(self):
        # 制热
        print('midea加热')

    def swing(self):
        # 摆风
        print('midea摆风')


def make_cool(ac: AC):
    # 管他是啥空调，这个函数就是要制冷
    ac.cool_wind()

def make_hot(ac: AC):
    # 管他是啥空调，这个函数就是要制热
    ac.hot_wind()


class XiaomiAC(AC):
    pass


if __name__ == '__main__':
    # 调用平台函数，利用多态+接口实现代码的解耦
    make_cool(MideaAC())
    make_cool(XiaomiAC())


