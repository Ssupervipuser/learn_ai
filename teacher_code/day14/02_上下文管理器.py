
class Myfile:
    def __init__(self, file_path_name, file_model='w'):
        self.file_path_name = file_path_name # 文件的完整路径包括名字
        self.file_model = file_model # 文件的打开模式，默认是w覆盖写
        self.f = None # 预设对象属性：文件操作对象
    # todo 上下文管理器需要定义下边两个魔法方法
    def __enter__(self):
        print('这是里上文')
        self.f = open(self.file_path_name, self.file_model)
        return self.f # 返回文件操作对象
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('这是下文')
        try:
            a = 1 / 0 # 就非要可能出错！
        except:
            pass
        finally:
            self.f.close() # 关闭文件对象
        print('下文exit函数结束了')


if __name__ == '__main__':
    file_path_name = '1.txt'
    # todo 1. Myfile(file_path_name, 'w') 创建对象
    # todo 2. __enter__() 执行完毕！fw就是该函数的返回对象
    with Myfile(file_path_name, 'w') as fw:
        print('创建文件，看后续报错的效果')
    # todo 3. __exit__() 执行完毕！
    print(222222)
    # todo 4. Myfile(file_path_name, 'r') 创建对象
    # todo 5. __enter__() 执行完毕！fr就是该函数的返回对象
    with Myfile(file_path_name, 'r') as fr:
        a = 1 / 0 # 这里报错了！程序后边两行代码都不执行了！
        fr.read()
        print(111111)
        # todo 6. __exit__() 执行完毕！
    # todo : 即使报错，下文管理exit函数也会执行！
