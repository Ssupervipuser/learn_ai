# class SweetPotato:
#     def __init__(self):
#         self.kaodigua_time=0
#         self.digua_status='shengde'
#         self.tiaoliao=[]
#     def kaodigua(self,time_int):
#         self.kaodigua_time=self.kaodigua_time+time_int
#
#         if self.kaodigua_time<=30:
#             self.digua_status='shneg'
#         elif 3<self.kaodigua_time<=7:
#             self.digua_satus='jiasheng'
#         elif 7<self.kaodigua_time<=12:
#             self.digua_status='shule'
#         else:
#             self.digua_status='HULE'
#         print(self.kaodigua_time,self.digua_status)
#
#
#     def addtiaoliao(self,tiaoliao):
#         self.tiaoliao.append(tiaoliao)
#         print(self.tiaoliao)
#
#     # def __str__(self):
#     #     return f'烧烤总时间{self.kaodigua_time},状态：{self.tiaoliao},调料类型{self.digua_status}'
#
# sp1=SweetPotato()
# sp2=SweetPotato()
#
# sp1.kaodigua(4)
# sp1.kaodigua(9)
# sp1.kaodigua(8)
# sp1.kaodigua(20)
# sp2.addtiaoliao('tianmianjiang')
# sp1.addtiaoliao('mashala')
# sp1.addtiaoliao('gali')
#
# print(sp1)
# print(sp2)



# class Master(object):
#     def __init__(self):
#         self.kongfu='gufajianbing'
#
#     def make_cake(self):
#         print(f'use  {self.kongfu}make cake')
#
# class School(object):
#     pass
    # def __init__(self):
    #     self.kongfu='heimajianbing'
    #
    # def make_cake(self):
    #     print(f'use  {self.kongfu}make cake')


# class Prentice(School,Master):
#     def __init__(self):
#         self.kongfu='duchuangjianbing'
#
#     def make_cake(self):
#         print(f'use  {self.kongfu}make cake')
#
# xiaoming=Prentice()
# print(xiaoming.kongfu)
# xiaoming.make_cake()


#
# class Prentice(School,Master):
#     def __init__(self):
#         self.kongfu='duchuangjianbing'
#
#     def make_cake(self):
#         print(f'use  {self.kongfu}make cake')
#
#     # def make_master_cake(self):
#     #     Master.__init__(self)
#     #     Master.make_cake(self)
#
#     def make_master_cake(self):
#         super().__init__()
#         super().make_cake()

#
# xiaoming=Prentice()
# xiaoming.make_master_cake()






# class Master(object):
#     def __init__(self):
#         self.kongfu='gufajianbing'
#
#     def make_cake(self):
#         print(f'use  {self.kongfu}make cake')
#
# class School(object):
#
#     def __init__(self):
#         self.kongfu='heimajianbing'
#
#     def make_cake(self):
#         print(f'use  {self.kongfu}make cake')
#
#
# class Prentice(School,Master):
#     def __init__(self):
#         self.kongfu='duchuangjianbing'
#         self.__money=20000
#
#     def make_cake(self):
#         print(f'use  {self.kongfu}make cake')
#
#
#
# class Tusun(Prentice):
#     pass
#
# xiaoming=Prentice()
#
# xiaoli=Tusun()
# xiaoli.make_cake()

#
# xiaoming=Prentice()
# print(xiaoming.kongfu)
# xiaoming.make_cake()

# class A(object):
#     def __init__(self):
#         self.a = 1
#
#     def show(self):
#         print(self.a)

# class B(A):
#     def __init__(self):
#         # super().__init__()
#         self.a=2
#
#     # def change(self):
#     #     print(self.a)
#
#     def show(self):
#         print(self.a)
#
#     def show2(self):
#         super().__init__()
#         super().show()
#
# bbb=B()
# bbb.show2()



class HeroFighter(object):
    def power(self):
        return 60

class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80

class EnemyFighter(object):
    def attack(self):
        return 70

def object_play(hero: HeroFighter, enemy:EnemyFighter):

    if hero.power() > enemy.attack():
        print('vectory')
    elif hero.power() == enemy.attack():
        print('same')
    else:
        print('defeat')

hero1=HeroFighter()
hero2=AdvHeroFighter()
enemy=EnemyFighter()

#
object_play(hero1,enemy)
object_play(hero2,enemy)


class Student(object):
    school='heima'  #类属性

    def __init__(self, name='wangzong',age=19):
        self.name=name  #对象属性
        self.age=age

    def show1(self):    #对象方法用来操作对象属性
        print(self.name)
        print(self.age)

    @classmethod
    def show1(cls):     #类方法用来操作类属性
        print(f'cls:{cls}')
        print(cls.school)
        print('我是类方法')

    @staticmethod
    def show2():
        print(Student.school)
        print('我是静态方法')

    def show3(self):
        print('我是普通的对象方法')


if __name__ == '__main__':
    print(Student.school)   #类名。类属性调用类属性
    s1=Student()
    print(s1.name,s1.age)   #对象名。对象属性，操作对象属性
    # print(s1.school)    #对象名。类属性，不推荐容易混淆，
    print('=' * 20)

    Student.show1()#操作类方法
    s1.show1()

    print('-'*20)
    s1.show2()  #操作静态方法
    Student.show2()

    print('3' * 20)
    s1.show3()  # 操作对象方法
    Student.show3()  #类名操作不了对象方法，会报错