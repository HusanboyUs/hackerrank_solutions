# Write your MySQL query statement below
SELECT E.name as name, B.bonus FROM Employee E
LEFT JOIN Bonus B on B.empId = E.empId
WHERE B.bonus < 1000 or B.bonus is Null