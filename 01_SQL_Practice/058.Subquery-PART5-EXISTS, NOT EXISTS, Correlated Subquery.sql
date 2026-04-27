

SELECT * FROM FactInternetSales
WHERE ProductKey IN(SELECT ProductKey FROM DimProduct WHERE Color='Red')

SELECT * FROM FactInternetSales
WHERE  EXISTS(SELECT ProductKey FROM DimProduct WHERE Color='Red')
--EXISTS returns true if the subquery returns any rows. In this case, it will return all rows from FactInternetSales where there is at least one matching ProductKey in the DimProduct table with the color 'Red'. If there are no matching rows in the subquery, EXISTS will return false and those rows from FactInternetSales will not be included in the result set.
SELECT * FROM FactInternetSales
WHERE  NOT EXISTS(SELECT ProductKey FROM DimProduct WHERE Color='Red')


SELECT * FROM FactInternetSales F
WHERE  EXISTS
(SELECT ProductKey FROM DimProduct P 
WHERE F.ProductKey=P.ProductKey AND P.Color = 'Red')

