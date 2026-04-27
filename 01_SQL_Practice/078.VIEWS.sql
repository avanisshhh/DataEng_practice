
'''
A VIEW in SQL is like a virtual table created from a query. It doesn’t store data itself (in most cases), it just stores the SQL logic.
'''

CREATE VIEW VwSelectData
AS
SELECT ProductKey,EnglishProductName,ListPrice FROM DIMPRODUCT


SELECT * FROM VwSelectData


CREATE VIEW VwDailySales
AS
SELECT P.EnglishProductName, F.orderdate,
SUM(SalesAmount) TotalSales
FROM DIMPRODUCT P JOIN FactInternetSales F
ON P.ProductKey = F.ProductKey
GROUP BY P.EnglishProductName, F.orderdate

SELECT * FROM [VwDailySales]


ALTER VIEW VwSelectData
AS
SELECT ProductKey,EnglishProductName,ListPrice,Color FROM DIMPRODUCT


DROP VIEW VwSelectData