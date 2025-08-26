SELECT b.id
FROM Weather a
JOIN Weather b ON DATEDIFF(b.recordDate, a.recordDate) = 1 -- b is one day after a. if you swap, it means a is one day after b
WHERE b.temperature > a.temperature;

-- questions tested you on self join as well as DATEDIFF function(can be solved using DATEADD too) (for MYsql)
-- got other ways to solve for other languages. e.g. Postgres b.recordDate = a.recordDate + INTERVAL '1 day'