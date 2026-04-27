

SELECT SUM(SalesAmount) FROM FactInternetSales

SELECT AVG(SalesAmount) FROM FactInternetSales

SELECT MIN(SalesAmount) FROM FactInternetSales

SELECT MAX(SalesAmount) FROM FactInternetSales


SELECT SUM(SalesAmount) AS TotalSales FROM FactInternetSales

SELECT SUM(SalesAmount)  TotalSales FROM FactInternetSales

SELECT SUM(SalesAmount)  [Total Sales] FROM FactInternetSales

SELECT SUM(SalesAmount)  Total_Sales FROM FactInternetSales

SELECT SUM(SalesAmount) AS TotalSales,
AVG(SalesAmount) as AvgSales
FROM FactInternetSales

SELECT COUNT(*) FROM DimProduct

SELECT COUNT(1000) FROM DimProduct
--COUNT(*)	All rows
--COUNT(1) / COUNT(1000)	All rows
--COUNT(column)	Non-NULL values only

SELECT ListPrice FROM DimProduct

SELECT COUNT(ListPrice) FROM DimProduct


SELECT COUNT(1) FROM DimProduct
WHERE ListPrice IS  NULL


SELECT COUNT(1) FROM DimProduct
WHERE ListPrice IS NOT NULL

SELECT * FROM DimProduct
WHERE ListPrice IS NULL


SELECT * FROM DimProduct
WHERE ListPrice IS NOT NULL
--IS NULL and IS NOT NULL are used to filter rows with NULL values in a specific column.