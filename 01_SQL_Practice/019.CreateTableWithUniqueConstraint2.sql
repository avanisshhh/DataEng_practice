CREATE TABLE EMPLOYEES4(
	EmployeeId int primary key ,
	EmployeeName varchar(100) ,
	DOJ datetime,
	Salary float,
	Email varchar(100) unique not null
)
--unique not nulL constraint ensures that the values in the Email column are unique across all records in the EMPLOYEES4 table. This means that no two employees can have the same email address, and it helps maintain data integrity by preventing duplicate entries in the Email column. Additionally, the NOT NULL constraint ensures that every employee must have an email address, and it cannot be left blank or contain NULL values. This further enforces data integrity by ensuring that the Email column always contains valid and unique email addresses for each employee.


INSERT INTO EMPLOYEES3(EmployeeId,EmployeeName,DOJ,Salary,Email) 
VALUES(1,'JACK','2022-11-24',30000,'jack123@gmail.com')

INSERT INTO EMPLOYEES4(EmployeeId,EmployeeName,DOJ,Salary,Email) 
VALUES(2,'JACKson','2021-11-24',40000,'jack123@gmail.com')


INSERT INTO EMPLOYEES4(EmployeeId,EmployeeName,DOJ,Salary,Email) 
VALUES(3,'JACKson','2021-11-24',40000,null)

INSERT INTO EMPLOYEES3(EmployeeId,EmployeeName,DOJ,Salary,Email) 
VALUES(4,'JACKson','2021-11-24',40000,null)

select * from EMPLOYEES3