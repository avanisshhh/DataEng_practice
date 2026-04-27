

CREATE TABLE #Employees(
	Empid int,
	Empname varchar(100)
)
--temporary table is created in tempdb database and it is automatically dropped when the session ends. It is only visible to the session that created it. 

SELECT * FROM #Employees



CREATE TABLE ##Employees(
	EMPID INT,
	EMPNAME VARCHAR(20)
)


SELECT * FROM ##Employees

SELECT * INTO #DIMPRODUCT FROM DIMPRODUCT

select * from #DIMPRODUCT