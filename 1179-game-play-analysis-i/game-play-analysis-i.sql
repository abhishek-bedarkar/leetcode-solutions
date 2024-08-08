# Write your MySQL query statement below
-- with ranked_activity as (
--     select *,
--          rank() over (partition by player_id order by event_date) as rnk
--     from Activity
-- )
-- select player_id,
--     ranked_activity.event_date as first_login 
--     from ranked_activity 
--     where ranked_activity.rnk = 1



select player_id,
    min(event_date) as first_login
from Activity 
group by player_id