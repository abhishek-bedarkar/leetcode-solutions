# Write your MySQL query statement below

with student_min_max_score as (
    select exam_id,
        student_id,
        case when (score < max(score) over(partition by exam_id)) and (score >  min(score) over(partition by exam_id)) 
            then 0 
        else 1 end as not_queit
    from Exam
)
select st_mnx.student_id,
    st.student_name
from student_min_max_score st_mnx
inner join Student st on st_mnx.student_id = st.student_id
group by st_mnx.student_id
having sum(st_mnx.not_queit) = 0;
