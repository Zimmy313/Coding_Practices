with first as(
    select player_id, min(event_date) as first_date
    from Activity
    group by player_id
), seconds as(
    select a.player_id
    from Activity a
    left join first b on a.player_id = b.player_id
    where DATEDIFF(a.event_date, b.first_date) = 1
)

select ROUND(
    COUNT(seconds.player_id) / (SELECT COUNT(*) from first), 2
) as fraction
from seconds;

SELECT 
    ROUND(
        COUNT(DISTINCT CASE WHEN DATEDIFF(event_date, first_date) = 1 THEN player_id END) /
        COUNT(DISTINCT player_id),
        2
    ) AS fraction
FROM (
    SELECT 
        player_id,
        event_date,
        MIN(event_date) OVER (PARTITION BY player_id) AS first_date
    FROM Activity
) t;

--AGG_FUNCTION(...) OVER (PARTITION BY ...)