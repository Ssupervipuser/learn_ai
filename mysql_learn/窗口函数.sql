/*
  窗口函数解释
    概念: 它是mysql8.0的新特征, 主要是给[表新增1列],新增的内容,取决于你使用了什么窗口函数
    格式:
        窗口函数 over(  [ partition by 分组字段 order by 排序字段 desc|asc ])
    常用窗口函数:
        row_number(): 做行标记
        rank()      :做稀疏排名
        dense_rank():做密集排名
    大白话解释
        假设数据集 100 90 90 60 则这三个函数的排序为:
            row_number():  1 2 3 4
            rank()      :  1 2 2 4
            dense_rank():  1 2 2 3
    小结:
        1: 窗口函数 = 给表新增1列 ,
        2: 如果不写partition by , 则统计是全表的数据 ,如果写了 统计组内的数据
        3: 如果不写orderby ,则统计的是组内所有的数据 ,如果写了 ,统计组内从第一个行数据
 */
show databases ;
use day01;

create table employee (empid int,ename varchar(20) ,deptid int ,salary decimal(10,2));

insert into employee values(1,'刘备',10,5500.00);
insert into employee values(2,'赵云',10,4500.00);
insert into employee values(2,'张飞',10,3500.00);
insert into employee values(2,'关羽',10,4500.00);

insert into employee values(3,'曹操',20,1900.00);
insert into employee values(4,'许褚',20,4800.00);
insert into employee values(5,'张辽',20,6500.00);
insert into employee values(6,'徐晃',20,14500.00);

insert into employee values(7,'孙权',30,44500.00);
insert into employee values(8,'周瑜',30,6500.00);
insert into employee values(9,'陆逊',30,7500.00);

SELECT * from employee;



-- 引入开窗函数
SELECT
        *,
        sum(salary) over () as total_sum ,  #验证:开窗函数会给原表增加1个列  求和所有人的薪资
        deptid,
        sum(salary) OVER (PARTITION BY  deptid) as total_sum , # 写了PARTITION BY   对组内薪资进行求和
        deptid,
        salary,
        sum(salary) over(PARTITION BY  deptid order by salary desc) as total_sum  #

FROM  employee;


-- 按照部门id(deptid)分组, 按照工资(salary)降序   [排名].
SELECT
    *,
    row_number() OVER (PARTITION BY deptid ORDER BY  salary desc) as rn,
    rank() OVER (PARTITION BY deptid ORDER BY  salary desc) as rk,
    dense_rank() OVER (PARTITION BY deptid ORDER BY  salary desc) as dk
FROM  employee;


# 有啥用 ????????   分组求topN

# 需求 找出 每组工资最高2个人的信息 (考虑并列)
# SELECT *,
#        rank()over(PARTITION BY deptid order by salary desc) rk
# from employee
# where rk<=2;

-- 解决方案: 子查询
SELECT * from (SELECT *,
                      RANK() OVER (PARTITION BY deptid ORDER BY salary DESC) rk
               FROM employee) t1 WHERE  rk<=2;












