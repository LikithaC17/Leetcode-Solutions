# Write your MySQL query statement below
# Write your MySQL query statement below
(select u.name as results 
from Users u
join MovieRating m
on u.user_id= m.user_id
group by m.user_id
order by count(m.user_id) desc ,results asc
limit 1)
union all
(select m1.title as results
from Movies m1 join MovieRating m
on m1.movie_id=m.movie_id
where created_at between '2020-02-01' and '2020-02-29'
group by m.movie_id
order by avg(rating) desc, results asc
limit 1)