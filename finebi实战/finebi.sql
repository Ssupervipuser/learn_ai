create database if not exists  ecommerce_db;
# drop database ecommerce_db;
use ecommerce_db;

create table if not exists categories(
    category_id int primary key  not null  unique ,
    category_name varchar(50) not null unique
);

create table if not exists products(
    product_id int primary key ,
    product_name varchar(100) not null unique ,
    price decimal(10,2) not null ,
    category_id int not null ,
    foreign key (category_id) references categories(category_id)
);

create table if not exists customers(
    customer_id int primary key ,
    customer_name varchar(50) not null,
    city varchar(50) not null
);


create table if not exists orders(
    order_id int primary key ,
    customer_id int not null ,
    order_date date not null ,
    total_amount decimal(10,2) default 0.00,
    foreign key (customer_id) references customers(customer_id)
);


create table if not exists order_items(
    item_id int primary key ,
    order_id int not null ,
    product_id int not null ,
    quantity int not null ,
    item_price decimal(10,2) not null ,
    foreign key (order_id) references orders(order_id),
    foreign key (product_id) references products(product_id)
);


insert into categories
values
    (1,'电⼦产品'),
    (2,'服装'),
    (3,'美妆'),
    (4,'⻝品'),
    (5,'⽇⽤');

# select * from categories;

insert into products values
(1, '联想笔记本', 5000.00, 1),
(2, '海尔冰箱', 3000.00, 1 ),
(3, '雷神游戏本', 6000.00, 1),
(4, '杰克琼斯夹克', 800.00, 2),
(5, '真维斯牛仔裤', 200.00, 2),
(6, '花花公子衬衫', 440.00, 2),
(7, '劲霸西装', 2000.00, 2),
(8, '香奈儿口红', 800.00, 3),
(9, '相宜本草面霜', 200.00, 3),
(10, '迪奥粉底', 500.00, 3),
(11, '一叶子面膜', 100.00, 3),
(12, '好想你红枣', 50.00, 4),
(13, '香飘飘奶茶', 20.00, 4),
(14, '旺旺雪饼', 15.00, 4),
(15, '海澜之家T恤', 150.00, 2),
(16, '苹果手机', 8000.00, 1),
(17, '兰蔻精华', 1200.00, 3),
(18, '雀巢咖啡', 80.00, 4),
(19, '汰渍洗衣液', 50.00, 5),
(20, '舒肤佳香皂', 10.00, 5)
;

insert into customers values
(1, '张三', '北京'),
(2, '李四', '上海'),
(3, '王五', '广州'),
(4, '赵六', '深圳'),
(5, '孙七', '成都'),
(6, '周八', '杭州'),
(7, '吴九', '重庆'),
(8, '郑十', '南京'),
(9, '刘十一', '武汉'),
(10, '陈十二', '西安'),
(11, '杨十三', '天津'),
(12, '黄十四', '苏州'),
(13, '马十五', '青岛'),
(14, '冯十六', '大连'),
(15, '朱十七', '厦门')

;
# select * from orders;
insert into orders values
(1, 9, '2023-09-07', 1545.00),
(2, 5, '2024-01-03', 27265.00),
(3, 3, '2024-06-17', 600.00),
(4, 6, '2024-08-02', 8430.00),
(5, 4, '2023-04-14', 1600.00),
(6, 3, '2024-03-07', 1165.00),
(7, 1, '2023-07-11', 4050.00),
(8, 2, '2024-06-01', 48060.00),
(9, 13, '2023-09-15', 3280.00),
(10, 1, '2023-04-21', 1000.00),
(11, 15, '2023-04-06', 770.00),
(12, 15, '2024-06-09', 4845.00),
(13, 1, '2024-04-06', 3615.00),
(14, 10, '2023-07-09', 5300.00),
(15, 8, '2023-11-26', 250.00),
(16, 12, '2023-05-03', 1720.00),
(17, 11, '2023-04-04', 50.00),
(18, 2, '2023-03-21', 2100.00),
(19, 11, '2023-08-12', 33800.00),
(20, 5, '2023-02-02', 44000.00),
(21, 12, '2023-12-23', 2595.00),
(22, 7, '2023-01-23', 11320.00),
(23, 4, '2023-09-25', 200.00),
(24, 2, '2023-04-05', 2610.00),
(25, 14, '2023-06-19', 2010.00)
;

insert into  order_items values
                             (1, 1, 10, 3, 500.00),
(2, 1, 14, 3, 15.00),
(3, 2, 3, 4, 6000.00),
(4, 2, 12, 1, 50.00),
(5, 2, 14, 1, 15.00),
(6, 2, 4, 4, 800.00),
(7, 3, 15, 4, 150.00),
(8, 4, 4, 3, 800.00),
(9, 4, 14, 2, 15.00),
(10, 4, 3, 1, 6000.00),
(11, 5, 8, 2, 800.00),
(12, 6, 11, 3, 100.00),
(13, 6, 14, 1, 15.00),
(14, 6, 12, 2, 50.00),
(15, 6, 15, 5, 150.00),
(16, 7, 12, 3, 50.00),
(17, 7, 18, 5, 80.00),
(18, 7, 11, 3, 100.00),
(19, 7, 4, 4, 800.00),
(20, 8, 1, 1, 5000.00),
(21, 8, 2, 1, 3000.00),
(22, 8, 13, 3, 20.00),
(23, 8, 16, 5, 8000.00),
(24, 9, 6, 2, 440.00),
(25, 9, 5, 1, 200.00),
(26, 9, 6, 5, 440.00),
(27, 10, 11, 4, 100.00),
(28, 10, 5, 3, 200.00),
(29, 11, 13, 1, 20.00),
(30, 11, 11, 4, 100.00),
(31, 11, 11, 1, 100.00),
(32, 11, 19, 5, 50.00),
(33, 12, 9, 4, 200.00),
(34, 12, 14, 3, 15.00),
(35, 12, 7, 2, 2000.00),
(36, 13, 10, 4, 500.00),
(37, 13, 11, 1, 100.00),
(38, 13, 10, 3, 500.00),
(39, 13, 14, 1, 15.00),
(40, 14, 9, 2, 200.00),
(41, 14, 8, 3, 800.00),
(42, 14, 9, 5, 200.00),
(43, 14, 10, 3, 500.00),
(44, 15, 12, 3, 50.00),
(45, 15, 19, 2, 50.00),
(46, 16, 18, 4, 80.00),
(47, 16, 8, 1, 800.00),
(48, 16, 5, 3, 200.00),
(49, 17, 12, 1, 50.00),
(50, 18, 11, 1, 100.00),
(51, 18, 7, 1, 2000.00),
(52, 19, 3, 3, 6000.00),
(53, 19, 2, 5, 3000.00),
(54, 19, 5, 4, 200.00),
(55, 20, 16, 5, 8000.00),
(56, 20, 7, 2, 2000.00),
(57, 21, 11, 5, 100.00),
(58, 21, 14, 3, 15.00),
(59, 21, 7, 1, 2000.00),
(60, 21, 19, 1, 50.00),
(61, 22, 6, 3, 440.00),
(62, 22, 1, 2, 5000.00),
(63, 23, 9, 1, 200.00),
(64, 24, 13, 3, 20.00),
(65, 24, 6, 5, 440.00),
(66, 24, 11, 2, 100.00),
(67, 24, 15, 1, 150.00),
(68, 25, 6, 3, 440.00),
(69, 25, 19, 1, 50.00),
(70, 25, 5, 1, 200.00),
(71, 25, 6, 1, 440.00)
;
# select * from order_items;

select distinct city
from customers
;

#2
select price,
       product_name
from
    products
order by price desc
limit 5
;
#3.
select
    c.category_id,
    c.category_name,
    avg(p.price)
from products p
join categories c on p.category_id = c.category_id
group by category_id

;
#4.
select
    c.category_name,
    products.product_name
from products
join categories c on products.category_id = c.category_id

;
#5
SELECT
    c.city,
sum(oi.quantity*oi.item_price)
from orders as os
JOIN order_items as oi
on os.order_id = oi.order_id
join customers c
on os.customer_id = c.customer_id
group by c.city
;


#6
select
    order_id,
    order_date,
    orders.total_amount

from
    orders
where orders.total_amount> (select avg(orders.total_amount) from orders)
;


#7
select
    order_date ,
    sum(quantity)

from orders os
join order_items oi on os.order_id = oi.order_id

group by order_date
order by order_date
;
select * from orders;


#8
select
    os.order_id,
    c.customer_name,
    os.order_date,
    os.total_amount
from orders os
join customers c on os.customer_id = c.customer_id
;
#9
select
    count(c.category_id),category_name
from products p
join categories c on c.category_id = p.category_id
group by p.category_id
;

#10
select

    product_name,
    sum(quantity*oi.product_id)

from order_items oi
join products on oi.product_id = products.product_id
group by product_name
;




