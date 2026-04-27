CREATE TABLE EMPLOYEES3(
	EmployeeId int primary key ,
	EmployeeName varchar(100) ,
	DOJ datetime,
	Salary float,
	Email varchar(100) unique
)
--unique constraint ensures that the values in the Email column are unique across all records in the EMPLOYEES3 table. This means that no two employees can have the same email address, and it helps maintain data integrity by preventing duplicate entries in the Email column.
--A unique constraint allows NULL values, but only one NULL value is allowed in the column.


INSERT INTO EMPLOYEES3(EmployeeId,EmployeeName,DOJ,Salary,Email) 
VALUES(1,'JACK','2022-11-24',30000,'jack123@gmail.com')

INSERT INTO EMPLOYEES3(EmployeeId,EmployeeName,DOJ,Salary,Email) 
VALUES(2,'JACKson','2021-11-24',40000,'jack123@gmail.com')


INSERT INTO EMPLOYEES3(EmployeeId,EmployeeName,DOJ,Salary,Email) 
VALUES(3,'JACKson','2021-11-24',40000,null)

INSERT INTO EMPLOYEES3(EmployeeId,EmployeeName,DOJ,Salary,Email) 
VALUES(4,'JACKson','2021-11-24',40000,null)

select * from EMPLOYEES3