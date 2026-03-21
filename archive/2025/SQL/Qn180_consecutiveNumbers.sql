SELECT DISTINCT num as ConsecutiveNums
FROM (
    SELECT num,
           LAG(num, 1) over (ORDER BY id) as pre1,
           LAG(num, 2) over (ORDER BY id) as pre2
    FROM Logs
) AS sub 
WHERE num = pre1 and num = pre2;
-- need alias for subquery under FROM. not needed under WHERE AND SELECT
