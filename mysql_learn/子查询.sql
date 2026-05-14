-- 准备工作
drop database if exists test09_mutiple_tab;
create database test09_mutiple_tab;
use test09_mutiple_tab;

drop table if exists table_category;
create table table_category(
    cid   varchar(20) primary key,
    cname varchar(40)    
);
create table table_product(
    pid         varchar(20) primary key,
    pname       varchar(40),
    price       double,
    flag        varchar(2), # 1表示上架、0表示下架
    category_id varchar(20),
    foreign key (category_id)
    references table_category(cid)
);

# 分类
insert into table_category(cid, cname) values('c001', '电器');
insert into table_category(cid, cname) values('c002', '服装');
insert into table_category(cid, cname) values('c003', '化妆品');

# 商品
insert into table_product(pid, pname, price, flag, category_id) values('p001', '联想', 5000, '1', 'c001');
insert into table_product(pid, pname, price, flag, category_id) values('p002', '海尔', 3000, '1', 'c001');
insert into table_product(pid, pname, price, flag, category_id) values('p003', '雷神', 5000, '1', 'c001');

insert into table_product (pid, pname, price, flag, category_id) values('p004', 'JACK JONES', 800, '1', 'c002');
insert into table_product (pid, pname, price, flag, category_id) values('p005', '真维斯', 200, '1', 'c002');
insert into table_product (pid, pname, price, flag, category_id) values('p006', '花花公子', 440, '1', 'c002');
insert into table_product (pid, pname, price, flag, category_id) values('p007', '劲霸', 2000, '1', 'c002');

insert into table_product (pid, pname, price, flag, category_id) values('p008', '香奈儿', 800, '1', 'c003');
insert into table_product (pid, pname, price, flag, category_id) values('p009', '相宜本草', 200, '1', 'c003');
insert into table_product (pid, pname, price, flag, category_id) values('p010', '迪奥', 1600, '1', 'c003');
insert into table_product (pid, pname, price, flag, category_id) values('p011', '一叶子', 799, '1', 'c003');


select * from table_product;

#子查询当条件
/*
select 字段 from table
where 字段[运算符、]
(select* from talbe)
*/
#todo 查询当前商品大于平均价格的商品
select avg(price) from table_product ;

select
    table_product.pname ,table_product.price
from table_product
  where price>(select avg(price)from table_product)
;

#todo 需求2：查询价格最高的商品（价格最高的可能不止一个）
select max(table_product.price) from table_product;

select
    pname,
    price
from table_product
where price=(select max(price) from table_product)
;


#子查询当来源
#select 字段 from (slect 字段 from table)

#todo 子查询的结果充当主查寻的数据源（临时表）
#需求查询价格再800~2000的商品，并显示对应分类名称
select * from table_category;
#1.查询价格
select table_product.pname,table_product.price,category_id
from table_product
where price between 200 and 800;

#将第一部的结果作为临时表和分类表关联，获取分类名称
select
*
from
    (select pname,price,category_id
     from table_product
     where price between 200 and 800) as p
join table_category as c
on p.category_id=c.cid
;


#子查询当字段
#select (select 字段 from table) from table

#todo计算每个商品的价格和商品整体的平均价格的差值
select avg(table_product.price) from table_product;
select*,
    price-
    (select avg(table_product.price) from table_product)
as '差值'


from table_product;


