# Write your MySQL query statement below
SELECT * 
FROM Cinema
WHERE description != 'boring' AND mod(id,2) != 0
ORDER BY rating DESC