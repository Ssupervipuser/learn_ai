# def confirm(account,pwd):
#     i=0
#     while i<=3:
#         if pwd=='admin888' and account=='admin':
#             print('登录成功')
#         else:
#             print("账号或密码错误请再次输入")
#         i+=1
#     print("账号已被封禁，请联系管理员")
#
#
#
# account=input("请输入账号：")
# pwd=input("请输入密码，若三次错误账号将被封禁，请小心输入：")
#
# confirm(account,pwd)



i=0
while i<3:
    account=input("请输入账号：")
    pwd=input("请输入密码，若三次错误账号将被封禁，请小心输入：")
    if pwd == 'admin888' and account == 'admin':
        print('登录成功')
        break
    else:
        print("账号或密码错误请再次输入")
    i+=1
    print("账号已被封禁，请联系管理员")