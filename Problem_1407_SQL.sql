--Top Travellers, solved Jan 7 2025

with x as (with r as (select user_id, sum(distance) as travelled_distance from Rides group by user_id) select user_id, name, coalesce(travelled_distance, 0) as travelled_distance from users left join r on users.id = r.user_id order by travelled_distance desc, name asc) select name, travelled_distance from x;

-- SELECT r.user_id, r.travelled_distance, u.id, u.name FROM Users u LEFT JOIN Rides r ON u.id = r.user_id;

-- select * from Users u left join (select user_id, sum(distance) as travelled_distance from Rides) group by user_id) as p on u.id = p.user_id
