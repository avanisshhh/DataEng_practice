SELECT * FROM DimProduct

SELECT UPPER('hello')

SELECT EnglishProductName,
UPPER(EnglishProductName) EnglishProductName FROM DimProduct


SELECT LOWER('HELLO')

SELECT EnglishProductName,
LOWER(EnglishProductName) EnglishProductName FROM DimProduct

SELECT LEFT('HELLO',2)

SELECT EnglishProductName,
LEFT(EnglishProductName,3) EnglishProductName FROM DimProduct

SELECT EnglishProductName,
LEFT(EnglishProductName,30) EnglishProductName FROM DimProduct


SELECT RIGHT('HELLO',3)

SELECT EnglishProductName,
RIGHT(EnglishProductName,3) EnglishProductName FROM DimProduct


SELECT SUBSTRING('HELLO',2,3)

SELECT EnglishProductName,
SUBSTRING(EnglishProductName,3,4) EnglishProductName FROM DimProduct
--substring(string, start, length)

SELECT LEN(' H EL LO ')
--len function returns the number of characters in a string, including spaces. In this case, the string ' H EL LO ' has 9 characters (including the leading and trailing spaces), so the LEN function will return 9.
SELECT EnglishProductName,
LEN(EnglishProductName) EnglishProductName FROM DimProduct


SELECT TRIM(' H EL LO ')
--TRIM function removes leading and trailing spaces from a string. In this case, the string ' H EL LO ' has leading and trailing spaces, so the TRIM function will return 'H EL LO' without the extra spaces.
SELECT EnglishProductName,
TRIM(EnglishProductName) EnglishProductName FROM DimProduct

SELECT LTRIM(' H EL LO ')

SELECT RTRIM(' H EL LO ')

' H EL LO'