drop database if exists test06_mutiple_tab;  
create database test06_mutiple_tab;  
use test06_mutiple_tab;  
  
-- 创建 分类表 (主表)  
drop table if exists test06_mutiple_tab.category;  
create table test06_mutiple_tab.category(  
    id varchar(10) primary key ,  
    name varchar(20)  
) comment '分类表';  
  
-- 创建 商品表 (从表)
show tables ;

create table product(
    pid int primary key ,
    name varchar(20),
    price decimal(10,2),
    category_id varchar(10),
    foreign key (category_id) references category(id)
);


insert into category values
                         ('c01','手机');

insert into  product values
         (1,'华为',2999,'c01')
;
insert into product values
    (6,'美的冰箱',5999,null);
select * from product;


#多表之间的关系
#一对一
show databases ;
create database if not exists test07;
#主表
create table test07.emp(
    id int primary key ,
    name varchar(20),
    age int,
    gender varchar(10)
)comment '员工基本信息表';
#从表
create table test07.emp_info(
    id int primary key ,
    addr varchar(200),
    foreign key (id) references emp(id)
)comment '员工详细信息表';


#一对多
use test07;

show tables;

create table test07.category(
    id varchar(10) primary key ,
    name varchar(20)
)comment '分类表';

create table test07.product(
    pid int primary key ,   
    name varchar(20),   
    price decimal(10,2),   
    category_id varchar(10),   
    -- 外键约束   
    constraint category_id_fk   
        foreign key (category_id)   
        references test07.category(id)
)comment '商品表';

#多对多

-- 学生表   

create table test07.student(
    id varchar(10) primary key ,   
    name varchar(20)   
) comment '学生表';   
-- 课程表   
drop table if exists test07.course;
    create table test07.course(
    id varchar(10) primary key ,   
    name varchar(20)   
) comment '课程表';   
-- 选课表(中间表)   
# 中间表 需要通过二个外键字段 分别指向不同表的主键字段   
-- 创建二个外键字段 分别和学生表主键 以及 课程表主键关联   
drop table if exists test07.sc;
create table test07.sc(
    id int primary key auto_increment,   
    sid varchar(10),   
    cid varchar(10),   
    constraint sid_fk # 关联学生表的外键   
        foreign key (sid)   
        references test07.student(id),
    constraint cid_fk # 关联课程表的外键   
        foreign key (cid)   
        references test07.course(id)
) comment '选课表(中间表)';
