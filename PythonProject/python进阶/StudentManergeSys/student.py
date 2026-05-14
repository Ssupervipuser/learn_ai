class Student:
    def __init__(self,name,age,gender,mobile,description):
        self.name=name
        self.age=age
        self.gender=gender
        self.mobile=mobile
        self.description=description

    def __str__(self):
        return f'{self.name} {self.age} {self.gender} {self.mobile} {self.description}'


if __name__ == '__main__':
    class A(object):
        a = 0

        def __init__(self):
            self.b = 1


    aa = A()
    # 返回类内部所有属性和方法对应的字典
    print(A.__dict__)
    # 返回实例属性和值组成的字典
    print(aa.__dict__)