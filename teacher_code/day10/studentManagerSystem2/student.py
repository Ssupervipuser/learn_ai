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
        stu_str = f"""学生信息是：
        {self.name}, 
        {self.age}, 
        {self.gender}, 
        {self.mobile}, 
        {self.description}
        """
        return stu_str