# class Check(object):
#     # def __init__(self, fn):
#     #     # 初始化操作在此完成
#     #     self.__fn = fn
#
#
#     # 实现__call__方法，表示对象是一个可调用对象，可以像调用函数一样进行调用。
#     def __call__(self, *args, **kwargs):
#         # 添加装饰功能
#         print("请先登陆...")
#         self.__fn()
#
#
# # @Check
# def comment():
#     print("发表评论")
#
#
# # comment()
#
#
# class Check(object):
#
#     # 实现__call__方法，表示对象是一个可调用对象，可以像调用函数一样进行调用。
#     def __call__(self, *args, **kwargs):
#         # 添加装饰功能
#         print("请先登陆...")
#         self.__fn()
#
#
# def comment():
#     print("发表评论")
#
# cmm=Check()
# cmm()





def input_user(fn):
    print('input_user1')
    def inner():
        print('模拟输入用户名密码')
        fn()  # 调用被装饰的函数
    print('input_user2')
    return inner


def check_user(fn):
    print('check_user1')
    def inner():        #a=10
        print('模拟验证用户名密码')
        fn()
    print('check_user2')
    return inner


@input_user  # 输入账号密码
@check_user  # 验证账号密码
def comment():
    print('发表评论')

comment()


# def check_user(fn):
#     print('check_user1')
#     def inner():
#         print('模拟验证用户名密码')
#         fn()
#     print('check_user2')
#     return inner
#
# @check_user  # 验证账号密码
# def comment():
#     print('发表评论')
#
# comment()