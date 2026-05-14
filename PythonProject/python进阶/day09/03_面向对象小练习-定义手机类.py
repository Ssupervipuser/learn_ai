
# 手机类
class Phone:
    # 定义手机颜色
    color = '白色'
    # 开机
    def open_phone(self):
        print('手机开机')
    # 关机
    def close_phone(self):
        print('关机')
    # 拍照
    def get_photo(self):
        print('手机拍照')
    def show_photo(self):
        print(f'手机的出厂颜色是{self.color}')
        self.color = '金色' # 修改 color
        print(f'手机的新颜色是{self.color}')

# 实例化对象
phone1 = Phone()
# 调用类对象的方法
phone1.open_phone()
phone1.get_photo()
phone1.close_phone()
phone1.show_photo()