

print('作业')
""" 
1. 03_列表、字典综合练习.py
2. 串讲笔记课件 在线文档 
    https://my.feishu.cn/wiki/Er0zwNVwAiD1C6k7QwEc8Ob3n46
    代码全来一遍：【4.容器数据类型】
3. 串讲笔记课件 在线文档
    代码抄一遍、写注释、能看懂：【5.1 函数示例】
"""

product=[
    {'name':'diannao','price':7000},
    {'name':'shubiao','price':30},
    {'name':'fengshan','price':20},
    {'name':'san','price':50},
]

qianbao=8000

total_money=0
for item in product:
    total_money+=item['price']

if total_money<qianbao:
    print('拿下')
print('买不起，跑路')

