# 定义变量
# 是否有车票
has_ticket_str = input('输入是否有票，是 或 否：')
if has_ticket_str == '是':
    has_ticket = True
    # 这里安检、检查小刀长度
    knife_length = int(input('输入小刀长度：'))
else: # 其他情况 全False
    has_ticket = False

# 要求：先检票、再安检；没票就不安检
# 是否有车票
if has_ticket == True: # 1 真
    # 如果有票，就安检
    print('检查小刀长度') # 1.1
    # 小刀长度是否大于20厘米
    if knife_length > 20: # 1.2 真
        # 大于20，禁止上车
        print('禁止上车') # 1.2 真 1
    # 小于等于20，可以上车
    else: # 1.2 假
        print('可以上车') # 1.2 假 1
# 如果没有票，就不安检、买票
else: # 1 假
    print('不安检、去买票')


