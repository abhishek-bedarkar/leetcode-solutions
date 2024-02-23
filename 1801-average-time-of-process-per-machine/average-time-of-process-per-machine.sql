# Write your MySQL query statement below

select machine_id, round(avg(processing_time),3) as processing_time 
    from 
        (
            select l.machine_id, l.process_id, r.timestamp - l.timestamp  AS processing_time  
            from 
                Activity l 
                left join Activity r on l.machine_id = r.machine_id and l.process_id =r.process_id 
            where  l.activity_type  = 'start' and r.activity_type='end') as subquery 
    group by 
    machine_id