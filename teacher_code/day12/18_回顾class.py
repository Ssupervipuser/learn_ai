class Person:
    # --------------- 类属性 ---------------
    species = "人类"
    total_count = 0

    # --------------- 构造方法 ---------------
    def __init__(self, name, age):
        self.name = name          # 实例属性（公有）
        self.__age = age          # 私有属性：双下划线开头

        Person.total_count += 1

    # --------------- __str__ ---------------
    def __str__(self): # 打印对象名的时候 print(Person()) 输出该函数return后边的字符串
        return f"姓名：{self.name}，年龄：{self.__age}"

    # --------------- __del__  ---------------
    def __del__(self): # 当删除对象时，就会执行这个函数
        Person.total_count -= 1

    # --------------- 普通方法 ---------------
    def work(self): # 对象方法
        print(f"{self.name} 在生活")

    # --------------- 私有方法 ---------------
    def __private_method(self):
        print(f"【私有方法】{self.name} 的秘密年龄是 {self.__age}")

    # 公开方法调用私有方法（对象只能这样访问）
    def show_private(self):
        self.__private_method()

    # --------------- 静态方法 ---------------
    @staticmethod
    def is_adult(age):
        return age >= 18

    # --------------- 类方法 ---------------
    @classmethod
    def get_total(cls):
        return f"总人数：{cls.total_count}"


# =============== 子类：多态 ===============
class Student(Person):
    def work(self):
        print(f"{self.name} 在学习")


class Teacher(Person):
    def work(self):
        print(f"{self.name} 在上课")

    def father_func(self):
        # 调用父类方法的方式
        Person.work(self)
        super().work()


# =============== 测试 ===============
if __name__ == "__main__":
    p = Person("张三", 20)
    print(p)

    # 访问私有属性、方法会报错
    # print(p.__age)    # 报错
    # p.__private_method()  # 报错

    # 正确方式：通过公开方法访问
    p.show_private()

    print("-" * 40)

    # 多态演示
    people = [Student("小明", 18), Teacher("李老师", 40)]
    for person in people:
        person.work()

    print("-" * 40)
    print(Person.get_total())