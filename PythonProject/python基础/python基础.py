#1.定义变量：苹果价格

price_str=input('please input your price of apple: ')


#2.定义变量  斤
num_str=input('please input your number of apple: ')

#todo： 将苹果价格、数量两个变量的值从str转为int或float
price=float(price_str)
num_int=int(num_str)
#4.定义变量：支付的总金额=苹果单价*斤数
amount=price*num_int

#5打印输出所有变量
print(f'number of apple: {num_int} yuan/jin, has buy{num_int} yuan/jin,you need pay {amount} yuan')

