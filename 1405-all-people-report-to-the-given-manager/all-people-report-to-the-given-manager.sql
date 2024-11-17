# Write your MySQL query statement below
-- with level_1 as (
--     select employee_id
--     from Employees
--     where manager_id = 1 and employee_id != 1
-- ),
-- level_2 as (
--     select employee_id
--     from Employees
--     where manager_id in (select employee_id from level_1)
-- ),
-- level_3 as (
--     select employee_id
--     from Employees
--     where manager_id in (select employee_id from level_2)
-- )
-- select employee_id from level_1
-- union 
-- select employee_id from level_2
-- union
-- select employee_id from level_3


with recursive employee_hir_3 as (

    # base case
    select employee_id,
        1 as depth
    from Employees
    where manager_id = 1 and employee_id != 1

    union 

    # recursive case
    select e.employee_id,
        eh.depth + 1 as depth
    from Employees e 
    inner join employee_hir_3 eh on e.manager_id = eh.employee_id 
    where eh.depth < 3
)
select employee_id
from employee_hir_3;