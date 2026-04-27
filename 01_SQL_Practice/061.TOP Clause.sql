

SELECT TOP 10 * FROM DimProduct

SELECT TOP 10 ProductKey,EnglishProductName,ListPrice FROM DimProduct

SELECT * FROM(
SELECT TOP 10 * FROM DimProduct
ORDER BY ProductKey DESC)T
ORDER BY ProductKey
--Sorts DimProduct by ProductKey in descending order
--Picks TOP 10 rows
-- So you get the 10 highest ProductKey values


SELECT TOP 10 PERCENT * FROM DimProduct
--TOP 10 PERCENT → returns 10% of total rows from the table
--👉 So if DimProduct has 1000 rows, you’ll get 100 rows