# Write your MySQL query statement below

select c.name as name, sum(t.amount) as balance
from Transactions t 
left join Users c
on t.account = c.account
group by t.account
having balance> 10000