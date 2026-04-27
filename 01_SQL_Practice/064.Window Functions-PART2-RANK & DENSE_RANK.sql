

SELECT EmployeeId, EmpName, City, Department,Salary,
RANK() OVER(ORDER BY Salary DESC) Ranks
FROM EMPLOYEES

SELECT EmployeeId, EmpName, City, Department,Salary,
RANK() OVER(PARTITION BY CITY ORDER BY Salary DESC) Ranks
FROM EMPLOYEES


SELECT EmployeeId, EmpName, City, Department,Salary,
DENSE_RANK() OVER(ORDER BY Salary DESC) Ranks
FROM EMPLOYEES


SELECT EmployeeId, EmpName, City, Department,Salary,
DENSE_RANK() OVER(PARTITION BY CITY ORDER BY Salary DESC) Ranks
FROM EMPLOYEES


'''
In RANK():
Same salary → same rank
Gap appears (rank 3 is skipped)

In DENSE_RANK():
Same salary → same rank
No gaps 

'''