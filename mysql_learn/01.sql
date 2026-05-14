show databases;



create database if not exists test02_db;
use test02_db;

create table  if not exists category(
    id int primary key ,
    cname varchar(20)
);

desc category;

desc test02_db.category;

#在test02库中创建表product
create table if not exists product(
    pid int primary key ,   #主键
    pname varchar(20),      #产品名
    price decimal(10,1),    #价格
    categroy_id varchar(10) #分类id

);

show tables ;

drop table if exists category;


alter table test02_db.category add `describe` varchar(20);

desc test02_db.category;

alter table test02_db.category add des2 varchar(20);

alter table test02_db.category change des2 desnew varchar(20);

alter table test02_db.category change des2 desnew varchar(20);

alter table test02_db.category drop desnew;



# 创建数据库
create database if not exists shop_db;
use shop_db;

#创建用户表
create table if not exists  user(
    user_id int primary key ,
    useername varchar(20),
    password varchar(20),
    email varchar(50),
    phone varchar (20)

);

desc shop_db.user;

# 3.创建商品分类表
create table if not exists categroy(
    category_id int primary key ,
    cname varchar(20),
    description varchar(100)

);

show tables ;

# 4. 创建商品表
create table if not exists product(
    product_id int primary key ,
    product_name varchar(20),
    price decimal(10,2),
    categroy_id int
);

#5.创建订单表
create table  if not exists shop_db.order(
    order_id int primary key ,
    user_id int,
    total_amout decimal(10,2),
    status varchar(20)
);

desc shop_db.product;

alter table user add real_name varchar(20);

desc shop_db.user;

alter table shop_db.categroy drop description;

desc shop_db.categroy;

rename table shop_db.order to shop_db.order_info;

desc shop_db.order_info;

alter table shop_db.user change useername username varchar(20);

desc shop_db.user;