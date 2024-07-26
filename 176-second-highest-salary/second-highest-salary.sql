# Write your MySQL query statement below

select max(salary) as SecondHighestSalary 
from Employee 
where salary < (select max(salary) from Employee) ;

# But invalid for just one row
-- select salary as SecondHighestSalary
-- from Employee order by salary desc
-- limit 1 offset 1;

-- with ranked_salaries as (
--     select salary, row_number() over( order by salary desc) as rn
--     from Employee
-- )
-- select salary as SecondHighestSalary 
-- from ranked_salaries
-- where rn = 2;
