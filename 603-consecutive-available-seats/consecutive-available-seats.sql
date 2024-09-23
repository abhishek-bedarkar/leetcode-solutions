with Cinema_seats as (
    select coalesce(lag(free) over(), 0) as prev_seat,
        coalesce(lead(free) over() , 0) as next_seat,
        free,
        seat_id
from Cinema
)
select seat_id
    from Cinema_seats
    where (prev_seat = 1 or next_seat=1) and (free=1)
