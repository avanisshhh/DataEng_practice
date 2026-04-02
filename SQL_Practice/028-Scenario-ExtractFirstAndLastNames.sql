SELECT FULLNAME FROM EMPLOYEESBK


SELECT FULLNAME ,
LEFT(FULLNAME,3)
FROM EMPLOYEESBK

SELECT FULLNAME,LEFT(FULLNAME,CHARINDEX(' ',FULLNAME)) Firstname
FROM EMPLOYEESBK
--The CHARINDEX function is used to find the position of the first occurrence of a space character (' ') in the FULLNAME column. The LEFT function then extracts the substring from the FULLNAME starting from the leftmost character up to the position of the space character, effectively giving us the first name of the employee.
SELECT FULLNAME,TRIM(LEFT(FULLNAME,CHARINDEX(' ',FULLNAME)))
Firstname
FROM EMPLOYEESBK

SELECT FULLNAME,LEFT(FULLNAME,CHARINDEX(' ',FULLNAME)-1) Firstname
FROM EMPLOYEESBK

SELECT FULLNAME,RIGHT(FULLNAME,
LEN(FULLNAME)-CHARINDEX(' ',FULLNAME,CHARINDEX(' ',FULLNAME)+1)) LastName
FROM EMPLOYEESBK
--The RIGHT function is used to extract a substring from the FULLNAME column, starting from the rightmost character. The length of the substring is determined by the total length of the FULLNAME minus the position of the second space character. The CHARINDEX function is used twice to find the position of the second space character in the FULLNAME, which allows us to extract the last name of the employee correctly, even if there are middle names present.


SELECT FULLNAME,LEFT(FULLNAME,CHARINDEX(' ',FULLNAME)-1) Firstname,
RIGHT(FULLNAME,
LEN(FULLNAME)-CHARINDEX(' ',FULLNAME,CHARINDEX(' ',FULLNAME)+1)) LastName
FROM EMPLOYEESBK


SELECT 
    FULLNAME,
    LEFT(FULLNAME, CHARINDEX(' ', FULLNAME) - 1) AS FirstName,
    RIGHT(FULLNAME, CHARINDEX(' ', REVERSE(FULLNAME)) - 1) AS LastName
FROM EMPLOYEESBK;