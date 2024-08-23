# Write your MySQL query statement below


-- with reporting as (
--     select e.name, m.name as manager_name, m.id as m_id
--     from Employee e 
--     left join employee m on e.managerId  = m.id  
--     where e.managerId is not null and m.id is not null
-- )
-- select manager_name as name 
-- from reporting 
-- group by m_id having count(1) >=5;


select name from Employee where id in (select managerId from Employee group by managerId having count(managerId)>=5)