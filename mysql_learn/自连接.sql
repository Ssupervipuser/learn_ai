show databases ;

use areas_db;

#查询河南省所有地市
#他的pid是null的话就说明是省 市

select
    city.title,
    province.title,
    city.pid

from
    areas as province
join areas as city on city.pid=province.id

where province.title='河南省';

# 查询郑州市下辖的所有区县市的信息

select
    city.title,
    county.title
from
    areas as city
join areas as county on county.pid=city.id

where city.title='郑州市';


select
    city.title,
    province.title,
    city.pid
from
    areas as province
join areas as city on city.pid=province.id
# join areas as county on county.pid=city.id

where province.title='郑州市';

#查询河南省下所有市、区县的信息

select
    province.title,
    city.title,
    county.title
from areas province
join areas city on city.pid=province.id
join areas county on county.pid=city.id
where province.title='河南省'
