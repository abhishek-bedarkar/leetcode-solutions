# Write your MySQL query statement below

select
    name,
    bonus
from
    (
        select
            name,
            bonus
        from
            Employee e
        left join Bonus b on e.empID = b.empId
    ) as subquery
where bonus is null or bonus <1000