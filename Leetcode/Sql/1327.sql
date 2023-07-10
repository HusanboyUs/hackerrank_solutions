# Write your MySQL query statement below
SELECT P.product_name, SUM(O.unit) as unit FROM Products P
INNER JOIN Orders O on P.product_id = O.product_id
WHERE O.order_date < '2020-03-00' and O.order_date > '2020-02-00'
GROUP BY P.product_name
HAVING SUM(O.unit) >= 100