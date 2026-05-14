class Phone:
    # color='白色'
    #开机
    def open_phone(self):
        print('手机开机')

    #关机
    def close_phone(self):
        print('关机')

    #拍照
    def get_photo(self):
        print('拍照')

    def show_photo(self):
        self.color='白色'
        print(self.color)
#实例化对象
phone1 = Phone()
#调用类对象方法
phone1.open_phone()
phone1.close_phone()
phone1.get_photo()
phone1.show_photo()