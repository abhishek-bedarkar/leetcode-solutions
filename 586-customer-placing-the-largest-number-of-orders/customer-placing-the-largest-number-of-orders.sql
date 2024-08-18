# Write your MySQL query statement below

with customer_order_count as (
    select customer_number,
     count(*) as ord_count 
    from Orders
    group by customer_number 
)
select customer_number 
from customer_order_count where ord_count = (select max(ord_count) from customer_order_count )




