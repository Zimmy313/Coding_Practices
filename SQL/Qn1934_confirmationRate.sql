with cfm as(
    select user_id, count(*) as confirm_count
    from Confirmations
    where action = 'confirmed'
    group by user_id
), all_count as(
    select user_id, count(*) as all_count
    from Confirmations
    group by user_id
)

select a.user_id, ROUND(IFNULL(b.confirm_count/c.all_count, 0),2) as confirmation_rate
from Signups a
left join cfm b on a.user_id = b.user_id
left join all_count c on a.user_id = c.user_id
group by user_id

