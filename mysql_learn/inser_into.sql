create database if not exists test03_db;

use test03_db;
show databases ;

create table if not exists category(
    id varchar(10) primary key ,
    cname varchar(20)

);

desc test03_db.category;

create table if not exists test03_db.product(
    pid int primary key ,
    panme varchar(50),
    price decimal(10,1),
    categroy_id varchar(10)
);

show tables ;

insert into category(id, cname) VALUES ('01','手机');

insert into category values ('c02','家用电器');

insert into category values ('c03','电脑');

insert into category
values ('c04','数码相机'),
       ('c05','铠甲勇士');


insert into category(id) values ('06');

insert into category values ('07',null);


insert into product values
                        (1,'iphone16 pm',12999,'co1'),
                        (2,'三星w25',15999,'co1'),
                        (3,'冰箱',4999,'co2'),
                        (4,'电脑',4399.9,'co3'),
                        (5,'微波炉',99,'co2');


update category set id='c01' where id='01';
update category set id='c06' where id='06';


alter table product add active int;
update product set product.active=1;

alter table product change panme pname varchar(50);

update product set pname='huawei',price=5999 where pid=1;

delete from product where price>5000;

delete from product;
truncate  category;

alter table product change panme ppanme varchar(900);
alter table product add status varchar(1);

desc category;
update category set cname='ss' where cname='ssss'