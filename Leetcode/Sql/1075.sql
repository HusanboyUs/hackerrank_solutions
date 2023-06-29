# Write your MySQL query statement below
SELECT P.project_id, ROUND(AVG(E.experience_years),2) as average_years
FROM Project P
INNER JOIN Employee E on P.employee_id = E.employee_id
GROUP BY (project_id)