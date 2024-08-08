# Write your MySQL query statement below

select team_id,
    team_name,
    sum(coalesce(case when (team_id = host_team) and (host_goals > guest_goals) then 3 
        when (team_id = guest_team) and (guest_goals > host_goals) then 3
        when host_goals = guest_goals then 1 end, 0)) as num_points
from teams t
left join Matches m
on t.team_id = m.host_team or t.team_id = m.guest_team
group by team_id
order by num_points desc, team_id asc