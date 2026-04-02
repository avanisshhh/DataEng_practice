


SELECT * into tblEmps2 FROM tblEmps

SELECT * FROM tblEmps
UNION
SELECT * FROM tblEmps2

SELECT * FROM tblEmps
UNION ALL
SELECT * FROM tblEmps2


SELECT EmployeeId,EmployeeName,Title,Salary FROM tblEmps
UNION ALL
SELECT EmployeeId,EmployeeName,Title,Salary FROM tblEmps2


SELECT EmployeeId,EmployeeName,NULL Title,Salary FROM tblEmps
UNION ALL
SELECT EmployeeId,EmployeeName,Title,Salary FROM tblEmps2

--union vs union all: UNION removes duplicate rows from the result set, while UNION ALL includes all rows, including duplicates. UNION performs an implicit DISTINCT operation to eliminate duplicates, which can be more resource-intensive than UNION ALL, especially with large datasets. Therefore, if you do not need to remove duplicates and want better performance, it is recommended to use UNION ALL.