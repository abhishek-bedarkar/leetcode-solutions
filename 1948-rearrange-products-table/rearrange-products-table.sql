# Write your MySQL query statement below
with Product_ids as (
    select product_id from Products
),
result1 as(
    select product_id,
        "store1" as store,
        store1 as price
    from Products
    where store1 is not Null
),
result2 as(
    select product_id,
    "store2" as store,
    store2 as price
    from Products
    where store2 is not Null
),
result3 as (
    select product_id,
    "store3"as store,
    store3 as price
    from Products
    where store3 is not Null
)
select * from result1
Union
select * from result2
Union
select * from result3