

CREATE TABLE EMPLOYEES5(
	EmployeeId int,
	EmployeeName varchar(100),
	DOJ datetime,
	Salary float check(salary>=10000)
)
--CHECK constraint is used to enforce a condition on the values in a column. In this case, the CHECK constraint ensures that the Salary column can only accept values that are greater than or equal to 10,000. This helps maintain data integrity by preventing the insertion of invalid salary values into the EMPLOYEES5 table. If someone tries to insert a salary value less than 10,000, the database will reject the entry and return an error message, ensuring that only valid salary data is stored in the table.

INSERT INTO EMPLOYEES VALUES(1,'JOHN','2023-01-14',40000)

INSERT INTO EMPLOYEES5(EmployeeId,EmployeeName,DOJ,Salary) 
VALUES(1,'JACK','2022-11-24',30000)

INSERT INTO EMPLOYEES5(EmployeeId,EmployeeName,DOJ,Salary) 
VALUES(2,'JACKson','2022-11-24',9999)