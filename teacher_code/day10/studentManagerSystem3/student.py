# 定义学生类


class Student:
    def __init__(
        self,
        name, # 学生姓名
        age,
        gender,
        mobile,
        description
    ):
        # 定义每个学生的属性
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile
        self.description = description
        # todo 定义成一个学生信息字典？

    def __str__(self):
        # todo print(Student())时，输出的是这个函数的返回的字符串
        stu_str = f"""学生信息是：
        {self.name}, 
        {self.age}, 
        {self.gender}, 
        {self.mobile}, 
        {self.description}
        """
        return stu_str

    # def return_dict(self):
    #     return self.__dict__
    #
    # def return_self(self):
    #     return self

if __name__ == '__main__':
    # s = Student(sasasa)
    # s.__dict__ ==> 学生信息字典

    pass


