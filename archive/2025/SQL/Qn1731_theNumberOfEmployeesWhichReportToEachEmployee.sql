SELECT b.employee_id, b.name, COUNT(*) as reports_count, ROUND(AVG(a.age)) as average_age
FROM Employees a
LEFT JOIN Employees b on a.reports_to = b.employee_id
WHERE a.reports_to is not NULL
GROUP BY b.employee_id, b.name
ORDER BY b.employee_id