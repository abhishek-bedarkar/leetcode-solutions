# Write your MySQL query statement below
WITH RECURSIVE all_subtasks AS (
    # base
    SELECT 1 AS num

    UNION

    # recursive 
    SELECT 1 + num
    FROM all_subtasks
    WHERE num <= 20 
),
generated_subtasks as (
    SELECT t.task_id,
        at.num as subtask_id
    FROM Tasks t
    JOIN all_subtasks at on t.subtasks_count >= at.num
    ORDER BY t.task_id
)
SELECT GS.task_id,
    GS.subtask_id
FROM generated_subtasks GS
LEFT JOIN Executed  E ON GS.task_id = E.task_id and GS.subtask_id = E.subtask_id
WHERE E.task_id IS NULL AND E.subtask_id IS NULL; 
