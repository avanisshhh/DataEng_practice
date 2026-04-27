CREATE TABLE EMPLOYEES8(
	EmployeeId int,
	EmployeeName varchar(100),
	DOJ datetime,
	Salary float,
	City varchar(30) default 'London'
)
--default constraint is used to specify a default value for a column when no value is provided during an insert operation. In this case, the City column has a default value of 'London'. This means that if a new record is inserted into the EMPLOYEES8 table without specifying a value for the City column, it will automatically be assigned the value 'London'. This helps ensure that there is always a valid value in the City column, even if the user forgets to provide one during data entry.


INSERT INTO EMPLOYEES8(EmployeeId,EmployeeName,DOJ,Salary) 
VALUES(1,'JACK','2022-11-24',30000)

INSERT INTO EMPLOYEES8(EmployeeId,EmployeeName,DOJ,Salary,City) 
VALUES(2,'JACK','2022-11-24',30000,'nyc')

select * from EMPLOYEES8
