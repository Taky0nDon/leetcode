-- Write your PostgreSQL query statement below
-- check employee salary (s1)
-- get salary of employee where id = managerId (s2)
-- get name where  s1 > s2
SELECT name as "Employee" FROM Employee e
    WHERE e.salary > (SELECT salary FROM Employee f WHERE f.id = e.managerId);
