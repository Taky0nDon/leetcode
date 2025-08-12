-- Write your PostgreSQL query statement below
-- check employee salary (s1)
-- get salary of employee where id = managerId (s2)
-- get name where  s1 > s2
SELECT name as "Employee" FROM Employee e
    WHERE e.salary > (SELECT salary FROM Employee f WHERE f.id = e.managerId);
    
-- Selfjoin approach
-- SELECT e.name as "Employee" from Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.sudo slary;
