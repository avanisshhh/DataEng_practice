

SELECT * FROM DimProduct
ORDER BY Color ASC


SELECT * FROM DimProduct
ORDER BY Color DESC


SELECT ProductKey,EnglishProductName,COLOR,ListPrice
FROM DimProduct
ORDER BY ListPrice DESC


SELECT ProductKey,EnglishProductName,COLOR
FROM DimProduct
ORDER BY ListPrice DESC


SELECT ProductKey,EnglishProductName,COLOR,ListPrice
FROM DimProduct
ORDER BY COLOR,ListPrice

SELECT ProductKey,EnglishProductName,COLOR,ListPrice
FROM DimProduct
ORDER BY COLOR,ListPrice DESC

SELECT ProductKey,EnglishProductName,COLOR,ListPrice
FROM DimProduct
ORDER BY COLOR DESC,ListPrice DESC

SELECT ProductKey,EnglishProductName,COLOR,ListPrice
FROM DimProduct
ORDER BY 1 DESC
--1 refers to the first column in the select statement, which is ProductKey. This will sort the results by ProductKey in descending order.
SELECT ProductKey,EnglishProductName,COLOR,ListPrice
FROM DimProduct
ORDER BY 3

SELECT ProductKey,EnglishProductName,COLOR,ListPrice
FROM DimProduct
ORDER BY 3,4