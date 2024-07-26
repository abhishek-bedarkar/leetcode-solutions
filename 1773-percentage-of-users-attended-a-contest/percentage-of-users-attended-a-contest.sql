# Write your MySQL query statement below

with total_user as (

    select count(1) as total_cnt from Users
)
select contest_id, round((count(2)/t.total_cnt) * 100,2) as percentage 
from users u
inner join Register R on u.user_id = r.user_id
cross join total_user t 
group by contest_id 
order by percentage desc, contest_id asc;