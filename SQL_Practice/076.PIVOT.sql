
SELECT * FROM(
SELECT CITY,DEPARTMENT,Salary FROM EMPLOYEES)T
PIVOT(SUM(Salary) FOR DEPARTMENT IN(IT,Sales))P
--t is the alias for the inner query and p is the alias for the pivoted result set. The PIVOT operator is used to transform rows into columns based on the specified aggregation (SUM in this case) and the values in the DEPARTMENT column. The resulting output will show the total salary for each city, with separate columns for IT and Sales departments.