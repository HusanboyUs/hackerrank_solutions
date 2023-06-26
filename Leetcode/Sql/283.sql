# Write your MySQL query statement below
SELECT C.name as Customers FROM Customers C
LEFT JOIN Orders O on C.id = O.customerId
WHERE O.customerId is Null