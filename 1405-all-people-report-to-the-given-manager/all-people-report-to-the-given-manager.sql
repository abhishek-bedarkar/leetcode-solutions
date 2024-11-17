# Write your MySQL query statement below
with level_1 as (
    select employee_id
    from Employees
    where manager_id = 1 and employee_id != 1
),
level_2 as (
    select employee_id
    from Employees
    where manager_id in (select employee_id from level_1)
),
level_3 as (
    select employee_id
    from Employees
    where manager_id in (select employee_id from level_2)
)
select employee_id from level_1
union 
select employee_id from level_2
union
select employee_id from level_3