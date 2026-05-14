drop database if exists school_db;
create database school_db;
use school_db;

create table  student_scores(
    id int primary key  auto_increment,
    name varchar(50) not null ,
    gender enum('man','woman') default 'man',
    class varchar(20) not null,
    subject varchar(30) not null,
    score decimal(5,2) not null
);
alter table student_scores change gender gender enum('男','女') default '男';

insert into student_scores(name, gender, class, subject, score)
values
('张三', '男', '高三(1)班', '数学', 92.5), 
('李四', '男', '高三(2)班', '数学', 88.0), 
('王芳', '女', '高三(1)班', '数学', 95.5), 
('赵敏', '女', '高三(3)班', '数学', 76.0), 
('刘伟', '男', '高三(2)班', '英语', 82.5), 
('陈静', '女', '高三(1)班', '英语', 91.0), 
('杨洋', '男', '高三(3)班', '英语', 68.5), 
('周杰', '男', '高三(1)班', '物理', 87.0), 
('林琳', '女', '高三(2)班', '物理', 93.5), 
('郭强', '男', '高三(3)班', '物理', 79.0), 
('马超', '男', '高三(2)班', '数学', 85.5), 
('黄蓉', '女', '高三(1)班', '英语', 89.0), 
('诸葛亮', '男', '高三(3)班', '物理', 98.5);

select *  from student_scores
          where student_scores.subject='数学'
          order by score desc ;

select
    avg(student_scores.score),
    min(student_scores.score),
    max(student_scores.score)
from student_scores where subject='物理';

select count(student_scores.id),
       class
from student_scores
group by class
;

select
   cast(avg(student_scores.score)as decimal (10,1)) as avg,
    subject
from student_scores
group by subject
;

select
    max(student_scores.score),
    class,subject
from student_scores
group by class,subject
;

select
    student_scores.subject,
    avg(score)
from student_scores
where student_scores.gender='女'
group by subject
having avg(score)>90
;