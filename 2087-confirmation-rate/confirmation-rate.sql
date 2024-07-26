WITH ConfirmationCounts AS (
    SELECT
        user_id,
        COUNT(*) AS total_requests,
        SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed_requests
    FROM Confirmations
    GROUP BY user_id
),
ConfirmationRates AS (
    SELECT
        user_id,
        COALESCE(ROUND(confirmed_requests / total_requests, 2), 0) AS confirmation_rate
    FROM ConfirmationCounts
)
SELECT
    s.user_id,
    COALESCE(c.confirmation_rate, 0) AS confirmation_rate
FROM Signups s
LEFT JOIN ConfirmationRates c ON s.user_id = c.user_id;