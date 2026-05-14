create database if not exists test04_constraint;
use test04_constraint;

create table if not exists person1(
    id int primary key ,
        last_name varchar(20),
    first_name varchar(20),
    address varchar(20),
    city varchar(20)
);
show tables ;

create table if not exists person2(

    last_name varchar(20),
    first_name varchar(20),
    address varchar(20),
    city varchar(20),
    primary key (last_name,first_name)

);

desc person1;

alter table person1 drop primary key ;

alter table person2 add primary key (last_name,first_name);


insert into test04_constraint.person1 values
(1,'三','张','南京市雨花台区','南京市');


insert into test04_constraint.person2 values
('五','李','南京市雨花台区','南京市');


#not null
create table test04_constraint.persons5(
  id int not null ,
  last_name varchar(20) not null,
  first_name varchar(20),
  address varchar(20),
  city varchar(20)

);

desc persons5;

alter table persons5 change id id int;
#unique

create table  if not exists user(
    id int primary key auto_increment,
    phone varchar(11) unique,
    email varchar(50) unique ,
    username varchar(20),
    id_card int,
    unique (username,phone)
);

desc user;

alter table user add unique (id_card);


INSERT INTO test04_constraint.user
(phone) VALUES ('13800138000');

