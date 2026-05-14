create database if not exists school_db;
show databases ;

use school_db;

create table if not exists student(
    sid int primary key auto_increment,
    sname varchar(20) not null unique ,
    gender varchar(2) not null default '男',
    age int,
    class varchar(20) not null

);
show tables ;

create table if not exists course(
    cid int primary key ,
    cname varchar(30) not null unique ,
    credit int not null default 1
);

create table if not exists sc(
    scid int primary key auto_increment,
    sid int not null ,
    cid int not null ,
    score int,
    sc_time datetime default current_timestamp


);

alter table sc add unique (sid,cid);


