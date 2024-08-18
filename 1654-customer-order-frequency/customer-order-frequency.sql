# Write your MySQL query statement below

select o.customer_id,
    c.name    
from Orders o
left join Customers c 
on o.customer_id = c.customer_id
left join Product p
on o.product_id = p.product_id
where year(o.order_date) = 2020
group by o.customer_id
having sum(case when month(o.order_date) = 6 then p.price*o.quantity else 0 end) >= 100 and sum(case when  month(o.order_date) = 7 then p.price*o.quantity else 0 end) >= 100


-- SELECT o.customer_id,
--        c.name    
-- FROM Orders o
-- LEFT JOIN Customers c 
-- ON o.customer_id = c.customer_id
-- LEFT JOIN Product p
-- ON o.product_id = p.product_id
-- WHERE YEAR(o.order_date) = 2020
-- GROUP BY o.customer_id, c.name
-- HAVING SUM(CASE WHEN MONTH(o.order_date) = 6 THEN p.price * o.quantity ELSE 0 END) >= 100
--    AND SUM(CASE WHEN MONTH(o.order_date) = 7 THEN p.price * o.quantity ELSE 0 END) >= 100;