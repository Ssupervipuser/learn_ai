
# 手机类
class Phone:

    def __init__(self, pinpai, neicun=16):
        # todo 初始化方法函数：类一旦被实例化的时候、自动执行
        # todo 如果需要传参，类实例化的时候就要传参了！
        self.color = '白色' # 出厂颜色白色
        self.neicun = neicun # 出厂内存需要传参
        self.pinpai = pinpai

    def __str__(self):
        # todo 一旦定义本函数，print(实例对象)就输出这个函数的返回值
        # 返回的必须是字符串
        # 相当于重写了默认的__str__函数
        return '这是__str__函数'

    def __del__(self):
        # todo 代码结束时或手动删除对象时，自动执行del函数
        # 相当于在默认的__del__函数中额外增加了功能
        print('删除对象的时候自动执行__del__函数')

    def show_photo(self):
        # 查看手机当前状态、比如颜色
        print(f'手机的颜色是{self.color}')
        print(f'手机品牌是 {self.pinpai}')
        print(f'手机内存是 {self.neicun}')


# 实例化对象
# 此时，__init__初始化函数被执行了！
# 实例化的时候传参，参数传递给__init__函数
phone1 = Phone(pinpai='OPPO')
# 调用类对象的方法
phone1.show_photo()
# 因为定义了__str__函数，所以输出的是该函数自定义return的内容
print(phone1)
# 手动删除对象
del phone1
print(1111)

