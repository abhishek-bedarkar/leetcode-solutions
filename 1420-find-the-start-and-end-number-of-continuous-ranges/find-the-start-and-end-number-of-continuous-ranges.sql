with ranked_log as (
    SELECT 
        log_id,
        log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS grp
    FROM 
        Logs
)
select min(log_id) as start_id,
    max(log_id) as end_id
from ranked_log
group by grp
order by start_id