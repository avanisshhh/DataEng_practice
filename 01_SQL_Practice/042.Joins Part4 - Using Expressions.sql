SELECT 'P-' + format(ProductKey,'0000') as ProductId,
EnglishProductName into DimProducts FROM DimProduct

SELECT * FROM DimProducts
SELECT * FROM FactInternetSales

SELECT RIGHT(ProductId,4) FROM DimProducts
---RIGHT(string, number_of_characters) returns the specified number of characters from the end of a string. In this case, it will return the last 4 characters of the ProductId column from the DimProducts table.
SELECT P.ProductId,P.EnglishProductName,F.SalesAmount
FROM DimProducts P JOIN FactInternetSales F
ON RIGHT(P.ProductId,4) = F.ProductKey

SELECT P.ProductId,P.EnglishProductName,F.SalesAmount
FROM DimProducts P JOIN FactInternetSales F
ON CAST(RIGHT(P.ProductId,4) AS INT) = F.ProductKey