SELECT d.name AS Department, sub.name AS Employee, salary AS Salary
FROM (
    SELECT name, departmentId, salary,
        RANK() over (PARTITION BY departmentId 
                        ORDER BY salary DESC) AS rank_salary
    FROM Employee
) as sub
INNER JOIN Department d on sub.departmentId = d.id
WHERE sub.rank_salary = 1
