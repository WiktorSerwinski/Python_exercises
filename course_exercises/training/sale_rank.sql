select * from
(SELECT sale_id,amount,
dense_rank() OVER(order by amount desc) as ranking
from Sales) as sub
where ranking = x