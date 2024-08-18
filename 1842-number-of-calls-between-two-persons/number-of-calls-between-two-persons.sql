# Write your MySQL query statement below

with Calls_enriched as (
    select duration,
        case when from_id < to_id then concat(from_id ,"_" , to_id) else concat(to_id ,"_",from_id) end as id
    from Calls
)
select convert(substring_index(id,'_',1), unsigned) as person1,
    convert(substring_index(id,'_',-1), unsigned) as person2,
    count(*) as call_count,
    sum(duration) as total_duration
from Calls_enriched 
group by id