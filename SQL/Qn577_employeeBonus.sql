
select name, bonus 
from Employee a
left join Bonus b on a.empId = b.empId
where bonus < 1000 or bonus is null