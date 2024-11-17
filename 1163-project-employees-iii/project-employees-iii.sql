# Write your MySQL query statement below


with ranked_exp_per_dept as (
    select p.project_id, 
        p.employee_id,
        rank() over(partition by p.project_id order by e.experience_years desc) as rnk
    from Project p
    inner join Employee e on p.employee_id = e.employee_id
)
select project_id,
    employee_id
from ranked_exp_per_dept
where rnk = 1;