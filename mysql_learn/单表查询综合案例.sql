-- 创建数据库

CREATE DATABASE company_db;
USE company_db;

-- 创建员工表
drop table if exists employee ;
CREATE TABLE employee (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL DEFAULT '男',
    age INT,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2),
    join_date DATE
);

-- 插入模拟数据
INSERT INTO employee
(name, gender, age, department, salary, join_date)
VALUES
('张三', '男', 28, '技术部', 15000.00, '2020-03-15'),
('李四', '男', 32, '技术部', 18000.00, '2019-06-20'),
('王芳', '女', 25, '市场部', 8000.00, '2021-08-10'),
('赵敏', '女', 30, '市场部', 12000.00, '2020-11-05'),
('刘伟', '男', 35, '销售部', 10000.00, '2018-05-12'),
('陈静', '女', 27, '销售部', 9000.00, '2021-02-18'),
('杨洋', '男', 40, '管理层', 30000.00, '2015-12-01'),
('周杰', '男', 33, '技术部', 20000.00, '2017-09-22'),
('林琳', '女', 29, '市场部', 11000.00, '2019-04-30'),
('郭强', '男', 45, '管理层', 35000.00, '2014-10-15'),
('马超', '男', 31, '销售部', 9500.00, '2020-07-23'),
('黄蓉', '女', 26, '技术部', 13000.00, '2022-01-10'),
('孙悟饭', '男', 28, '销售部', 8500.00, '2021-09-05'),
('白素贞', '女', 38, '管理层', 28000.00, '2016-11-20'),
('诸葛亮', '男', 42, '管理层', 32000.00, '2013-08-08');


select * from employee;


-- 简单查询需求:       
# 查询员工姓名和所属部门       
# 使用别名：显示"员工姓名"和"月薪"列       
select name as '员工姓名' ,department as '月薪'from employee ;
-- 去重查询       
# 查询所有不重复的部门名称       
select distinct department from employee ;
-- 运算查询       
# todo 针对查询的结果, 修改对应列的字段类型的方法是：       
# cast(字段 as 数据类型) as 新字段名       
# 显示所有员工涨薪10%后的薪水（保留两位小数）       
select cast(salary*1.1 as decimal(10,2)) as salary2  from employee;
-- 条件查询       
# 查询薪水大于等于10000元的员工
select * from employee where salary>10000;
# 查询年龄在30岁以下的员工
select * from employee where age<30;

# 查询市场部所有员工
select * from employee where department='市场部';
# 查询薪水在8000到15000之间的员工
select * from employee where salary>=8000 and salary<=15000;

# 查询部门为"技术部"或"销售部"的员工
select * from employee where department='市场部' or department='销售部';

# 查询名字中包含"杰"字的员工
select * from employee where name like '%杰%';
# 查询姓"黄"的员工
select * from employee where name like '黄%';
# 查询2020年之前入职的员工       
select * from employee where join_date <'2020-01-01';
-- 组合查询       
# 查询女性且年龄小于30岁的员工
select * from employee where gender='女' and age<30;
# 查询管理层中薪水高于30000元的员工
select * from employee where department='管理层' and salary>30000;
# 查询不是技术部也不是市场部的员工
select * from employee where department not in ('技术部','市场部');