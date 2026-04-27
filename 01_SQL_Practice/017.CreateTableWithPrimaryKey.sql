CREATE TABLE EMPLOYEES_New(
	EmployeeId int primary key,
	EmployeeName varchar(100),
	DOJ datetime,
	Salary float
)
--EmployeeId is the primary key of the table. It uniquely identifies each record in the table and cannot contain NULL values.
--Diff bw PK and without PK: A table with a primary key enforces uniqueness and integrity, while a table without a primary key may allow duplicate records and does not guarantee data integrity.
--fast retrieval of data based on the primary key, as it creates an index on the primary key column(s). This can significantly improve query performance when searching for specific records.
SELECT * FROM EMPLOYEES_New

INSERT INTO EMPLOYEES_New VALUES(1,'JOHN','2023-01-14',40000)

INSERT INTO EMPLOYEES_New(EmployeeId,EmployeeName,DOJ,Salary) 
VALUES(2,'JACK','2022-11-24',30000)

INSERT INTO EMPLOYEES_New(EmployeeId,EmployeeName,DOJ,Salary) 
VALUES(NULL,'AMAN','2021-11-24',30400)
--and cannot contain NULL values.