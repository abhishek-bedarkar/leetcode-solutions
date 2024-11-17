# Write your MySQL query statement below
with sumed_cust_products as (
    select o.customer_id,
        o.product_id,
        count(order_id) as order_count
    from Orders o
    group by customer_id, product_id
),
ranked_cust_product as (
    select *,
        rank() over(partition by customer_id order by order_count desc) as rnk
    from sumed_cust_products
 )
 select r.customer_id,
    r.product_id,
    p.product_name
from ranked_cust_product r
inner join Products p on r.product_id = p.product_id
where rnk=1
order by r.customer_id
