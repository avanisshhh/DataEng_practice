SELECT EmployeeKey,FirstName,MiddleName,LastName FROM DimEmployee

SELECT FirstName + ' ' +  LastName FROM DimEmployee

SELECT FirstName + SPACE(1) + ISNULL(MiddleName,'') 
+ SPACE(1) + LastName FROM DimEmployee
--This query concatenates the FirstName, MiddleName, and LastName columns from the DimEmployee table to create a full name. The SPACE(1) function is used to add a single space between the names. The ISNULL function is used to handle cases where the MiddleName might be NULL; if MiddleName is NULL, it will be replaced with an empty string ('') to ensure that the concatenation still works correctly without resulting in a NULL value for the full name.
SELECT CONCAT(FirstName,space(1),MiddleName,space(1),LastName) 
FROM DimEmployee

SELECT CONCAT_WS(SPACE(1),FirstName,MiddleName,LastName) FROM DimEmployee
-- The CONCAT_WS function is used to concatenate strings with a specified separator. In this case, the separator is a single space (SPACE(1)). The function takes the FirstName, MiddleName, and LastName columns from the DimEmployee table and concatenates them into a full name, with a space between each name. If any of the name components are NULL, CONCAT_WS will skip them and not include extra separators, ensuring that the resulting full name is formatted correctly without unnecessary spaces.
SELECT CONCAT_WS('-',FirstName,MiddleName,LastName) FROM DimEmployee

SELECT EmployeeKey,FirstName,MiddleName,LastName,
CONCAT_WS(SPACE(1),FirstName,MiddleName,LastName) FullName
FROM DimEmployee

SELECT EmployeeKey,FirstName,MiddleName,LastName 
into EmployeesBk
FROM DimEmployee


select * from EmployeesBk


ALTER TABLE EmployeesBk
ADD Fullname varchar(50)


UPDATE EmployeesBk
SET FULLNAME = CONCAT_WS(SPACE(1),FirstName,MiddleName,LastName)