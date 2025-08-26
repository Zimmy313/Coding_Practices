select a.student_id, a.student_name, b.subject_name, count(c.student_id) as attended_exams
from Students a
cross join Subjects b -- cross join dont support 'on' clause
left join Examinations c on a.student_id = c.student_id and b.subject_name = c.subject_name
group by a.student_id, b.subject_name -- by right, should also group by a.student_name since  
-- it is selected in the select clause. Good practice to add it in. Some sql languages will
-- raise errors.
order by a.student_id, b.subject_name