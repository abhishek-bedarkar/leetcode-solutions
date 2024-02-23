# Write your MySQL query statement below
SELECT 
    id
FROM (
    SELECT 
        id,
        recordDate,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate) AS prevTemperature,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prevDate
    FROM Weather
) AS subquery
WHERE temperature > prevTemperature and prevTemperature IS not NULL and DATEDIFF(recordDate, prevDate) = 1;
