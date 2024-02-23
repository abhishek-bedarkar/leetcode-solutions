# Write your MySQL query statement below
select unique_id, name 
from Employees as emp left join EmployeeUNI as emp_uq 
on emp.id = emp_uq.id