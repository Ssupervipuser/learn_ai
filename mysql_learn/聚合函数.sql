use test05_dql;

show tables ;
desc test05_dql.product;

select * from product;

select count(pid) from product;

select count(1) from product;

select count(product.price) from product where price>200;

select sum(product.price) from product where category_id='c001';

select cast(avg(product.price) as decimal(9, 1)) as '均价'
from product
where category_id = 'c002';

select max(product.price),min(product.price) from product;


select
    category_id,
    count(category_id)

from product
group by category_id
;

select product.category_id,
       count(category_id) as c
from product
group by category_id
having c > 1
;
show create table product;
# CREATE TABLE `product` (
#   `pid` int NOT NULL,
#   `pname` varchar(20) DEFAULT NULL,
#   `price` decimal(10,2) DEFAULT NULL,
#   `category_id` varchar(32) DEFAULT NULL,
#   PRIMARY KEY (`pid`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

create table product2(
    pid int primary key ,
    pname varchar(20),
    price decimal(10,2)

);
truncate table product2;


insert into test05_dql.product2
select product.pid, product.pname, product.price
from product where category_id='c001';

select * from product2;

# create table product3();
create table product3
as
    select
        pid,
        pname,
        price
from product where category_id='c001';