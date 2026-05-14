
class Person():
    count = 1 # 类属性：在class类中，在函数外：所有对象共有
    def __init__(self):
        self.name = None # 对象属性：对象独有
    def get_count(self):
        print(Person.count)


print(Person.count) # 类属性的获取方式
Person().get_count()

Person.count = 2 # 永久改变类属性
print(Person.count)
Person().get_count()

p1 = Person()
p2 = Person()
p1.name = '张三'
print(p1.name)
print(p2.name)
p2.name = '李四'
p1.get_count()

p1.gender = 1

Person.abcd = 555
print(Person.abcd) # 类里没定义，类外也可以添加、修改

p1.count = 3 # 对象名.属性 ==> 对象属性
print(Person.count) # 虽然同名，但不能修改类属性
# todo 类名.类属性
#  对象名.对象属性； self.对象属性
