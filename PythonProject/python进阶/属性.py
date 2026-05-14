class Person:
    def __init__(self):
        self.__age=100

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,new_age):
        self.__age=new_age



class Person2:
    def __init__(self):
        self.__age=102

    def get_age(self):
        return self.__age

    def set_age(self,new_age):
        self.__age=new_age


    age=property(get_age,set_age)



if __name__ == '__main__':
    p=Person()
    print(p.age)
    p.age=200
    print(p.age)


    p2=Person2()
    print(Person2.age)

    print(p2.age)

    Person2.age=202
    print(Person2.age)
    print(p2.age)
