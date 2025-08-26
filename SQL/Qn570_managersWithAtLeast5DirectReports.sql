with manager as (
    select managerId 
    from Employee
    group by managerId
    having count(managerId) >= 5
)
select name
from Employee
join manager on employee.id = manager.managerId
