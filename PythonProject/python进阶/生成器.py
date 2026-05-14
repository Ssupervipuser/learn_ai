# import math
#
# def dataset_loader(bath_size:int):
#     file_path_name='../../teacher_code/day14/歌词.txt'
#     with open(file_path_name,'r',encoding='utf-8') as f:
#         lines_list=f.readlines()
#     lines_count=len(lines_list)
#     batch_number_float=lines_count/bath_size
#     batch_number_int=math.ceil(batch_number_float)
#     for idx in range(batch_number_int):
#         yield lines_list[idx*bath_size:idx*bath_size+bath_size]
#
#
# g=dataset_loader(5)
# for lst in g:
#     print(lst)
#
#
#
#

# for i in range(1,11):
#     print(i,type(i))
#
# myg=(i for i in range(1,11))
# print(myg)
#
# v=next(myg)
# print(v,type(v))
#
# for v in myg:
#     print(v,type(v))


class Person(object):
    def __init__(self):
        # 定义私有属性 __age，初始值为 0
        self.__age = 0

    # 装饰器 @property：将方法转为属性，用于获取私有属性值
    @property
    def age(self):
        return self.__age

    # 装饰器 @age.setter：为 age 属性设置修改器，用于修改私有属性值
    @age.setter
    def age(self, new_age):
        self.__age = new_age

if __name__ == '__main__':
    # 创建 Person 实例
    p1 = Person()
    # 获取 age 属性值（调用 @property 装饰的 age 方法）
    print(p1.age)  # 输出：0

    # 修改 age 属性值（调用 @age.setter 装饰的 age 方法）
    p1.age = 100
    # 再次获取 age 属性值
    print(p1.age)  # 输出：100