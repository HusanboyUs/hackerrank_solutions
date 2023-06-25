
SELECT E.name as Employee FROM Employee E
INNER JOIN Employee M on E.managerId = M.id
WHERE E.salary > M.salary
