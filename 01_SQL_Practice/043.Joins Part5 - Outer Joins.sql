

SELECT * FROM Products P LEFT JOIN SalesTran S
ON P.ProductId = S.ProductId

SELECT * FROM Products P LEFT OUTER JOIN SalesTran S
ON P.ProductId = S.ProductId
--Both are EXACTLY the same
---All rows from Products (left table)
---Matching rows from SalesTran
---If no match → NULL in SalesTran columns

SELECT * FROM SalesTran S RIGHT JOIN Products P
ON P.ProductId = S.ProductId


SELECT * FROM SalesTran S RIGHT OUTER JOIN Products P
ON P.ProductId = S.ProductId

SELECT * FROM SalesTran S FULL OUTER JOIN Products P
ON P.ProductId = S.ProductId
--All rows from both tables
--Matching rows combined
--Non-matching rows from either side → NULL