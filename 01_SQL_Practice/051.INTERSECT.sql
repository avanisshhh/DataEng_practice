SELECT * FROM tblEmps
UNION
SELECT * FROM tblEmps2

SELECT * FROM tblEmps
INTERSECT
SELECT * FROM tblEmps2
--INTERSECT returns only the rows that are present in both result sets. In this case, it will return the rows that are common to both tblEmps and tblEmps2 tables. If there are any duplicate rows in either table, they will be treated as a single row in the result set.

DELETE FROM tblEmps2 WHERE EMPLOYEEID = 10


SELECT A.* FROM tblEmps A JOIN tblEmps B
ON A.EmployeeId = B.EmployeeId AND A.ParentEmployeeId = B.ParentEmployeeId