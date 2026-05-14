

product = [
    {'name': '电脑', 'price': 7000},
    {'name': '鼠标', 'price': 30},
    {'name': '风扇', 'price': 20},
    {'name': '伞', 'price': 50},
]

# 一共有8000 能把上边的商品都买下来吗？
qianbao = 8000

# 总金额
zongjine = 0 # 最开始的时候是0元
# 取出列表中每个字典中price的值、并相加求和
for i_dict in product:
    # price = i_dict['price']
    # print(price)
    # 遍历出来一个商品的价格，就累加到总金额上
    # i_dict['price'] 商品的价格
    # price = price + i_dict['price']
    zongjine += i_dict['price'] # 累加

print(zongjine)

# 判断 【钱包 - 所有商品价格的和】 是否大于0
if qianbao - zongjine >= 0:
    # 大于等于0 说明够花都能买
    print('钱够，买了！')
else: # 小于0 说明钱不够
    print('钱不够，不买了')




