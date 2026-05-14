# 作业

class SweetPotato(object):
# class SweetPotato():
# class SweetPotato:
    def __init__(self):
        # 初始化函数定义属性
        self.kaodigua_time = 0 # 烤地瓜的总时长
        self.digua_status = '生的' # 地瓜的生熟状态
        self.tiaoliao_list = [] # 调料列表

    def kaodigua(self, time_int):
        # 根据烧烤时间，改变总烧烤时长，改变地瓜的生熟状态
        # 改变总烧烤时长
        self.kaodigua_time = self.kaodigua_time + time_int
        # 改变地瓜的生熟状态
        if self.kaodigua_time <= 3:
            self.digua_status = '生的'
        elif 3 < self.kaodigua_time <= 7:
            self.digua_status = '夹生'
        elif 7 < self.kaodigua_time <= 12:
            self.digua_status = '熟了'
        else:
            self.digua_status = '糊了'
        print(self.digua_status, self.kaodigua_time)

    def addtiaoliao(self, tiaoliao):
        # 添加调料到 地瓜的配料列表中
        self.tiaoliao_list.append(tiaoliao)
        print(self.tiaoliao_list)

    def __str__(self):
        # print(obj_name) 会输出 烧烤时间、生熟状态、调料列表
        return f'烧烤总时长：{self.kaodigua_time}，状态：{self.digua_status}，调料都有：{self.tiaoliao_list}'


sp1 = SweetPotato() # 实例化烤地瓜
sp2 = SweetPotato()
sp1.kaodigua(4)
sp2.kaodigua(9)
sp1.kaodigua(8)
sp1.kaodigua(20)
sp2.addtiaoliao('甜面酱')
sp1.addtiaoliao('玛莎拉')
sp1.addtiaoliao('咖喱')

print(sp1)
print(sp2)

import asyncio