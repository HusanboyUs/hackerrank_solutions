# Write your MySQL query statement below

SELECT P.product_name, S.year,S.price
FROM Product P
INNER JOIN Sales S on P.product_id = S.product_id
WHERE S.sale_id in (
  SELECT sale_id FROM Sales
)
GROUP BY S.sale_id
