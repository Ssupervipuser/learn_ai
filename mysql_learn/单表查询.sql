-- 复制并运行下边的代码，用于本章节的DQL查询数据的学习 
# 创建数据库 
drop database if exists test05_dql; 
create database test05_dql; 
use test05_dql; 
#创建商品表： 
create table test05_dql.product( 
 pid int primary key, 
 pname varchar(20), 
 price decimal(10,2), 
 category_id varchar(32) 
); 
# 多行书写: alt + 鼠标左键选择 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(1,'联想',5000,'c001'); 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(2,'海尔',3000,'c001'); 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(3,'雷神',5000,'c001'); 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(4,'杰克琼斯',800,'c002'); 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(5,'真维斯',200,'c002'); 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(6,'花花公子',440,'c002'); 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(7,'劲霸',2000,'c002'); 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(8,'香奈儿',800,'c003'); 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(9,'相宜本草',200,'c003'); 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(10,'面霸',50,'c003'); 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(11,'好想你枣',56,'c004'); 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(12,'香飘飘奶茶',12,'c005'); 
INSERT INTO test05_dql.product(pid,pname,price,category_id) VALUES(13,'海澜之家',128,'c002'); 

-- 校验: 
select * from test05_dql.product;

# 查询所以商品
select * from test05_dql.product;

# 查询商品命和商品价格
select product.pname,product.price from product;
# 别名查询
# 为表名
select
    product.pid as '商品ID',
    product.pname as '商品名',
    product.price as '商品价格',
    product.category_id as '商品分类编号'
from product;


select
distinct
    product.category_id as '商品分类编号'
from product;

desc product;



#综合实力
-- 查询商品名称为“花花公子”的商品所有信息
    select * from product where pname='花花公子';
-- 查询价格为800商品
    select * from product where price=800;
-- 查询价格不是800的所有商品
    select * from product where price<>800;
    select * from product where price!=800;
-- 查询商品价格大于60元的所有商品信息
    select * from product where price>60;
-- 查询商品价格在200到800之间所有商品
    select * from product where price between 200 and 800;
    select * from product where price >=200 and price<=800;
-- 查询商品价格是200或800的所有商品
    select * from product where price=200 or price=800;
-- 查询含有'霸'字的所有商品
    select * from product where pname like'%霸%';
-- 查询以'香'开头的所有商品
    select * from product where pname like'香%';

-- 查询第二个字为'想'的所有商品
    select * from product where pname like'_想';

-- 商品没有分类的商品
    select * from product where category_id is null;
-- 查询有分类的商品

 select * from product where category_id is not null;