

CREATE TABLE SalesTran(
	ProductId int,
	InvoiceNum varchar(10),
	Qty int,
	Sales money
)


INSERT INTO SalesTran(ProductId,InvoiceNum,Qty,Sales) VALUES
(1,'SOB982',10,3000),
(2,'SOB983',5,2500),
(3,'SOB984',5,376),
(1,'SOB985',7,2100),
(2,'SOB986',8,4000),
(4,'SOB987',10,838)

CREATE TABLE Products(
	ProductId int,
	ProductName varchar(50),
	UnitPrice money
)

INSERT INTO Products(ProductId,ProductName,UnitPrice) VALUES
(1,'ABC Logo Cap',300),
(2,'Ball Bearing',500),
(3,'Bell',75.2),
(4,'Trousers',83.8),
(5,'Shirt',200)


SELECT * FROM SalesTran

SELECT * FROM Products


SELECT * FROM SalesTran, Products

SELECT * FROM SalesTran JOIN Products 
ON SalesTran.ProductId = Products.ProductId
--BY DEFAULT INNER JOIN 

--The ON clause specifies the condition for the join, which is that the ProductId in the SalesTran table must match the ProductId in the Products table. This allows us to retrieve data from both tables in a single query, combining the relevant information based on the specified relationship.

SELECT * FROM SalesTran INNER JOIN Products 
ON SalesTran.ProductId = Products.ProductId
--Inner Join returns only the rows where there is a match in both tables based on the specified join condition. In this case, it will return only the rows where the ProductId in the SalesTran table matches the ProductId in the Products table. If there are any rows in either table that do not have a corresponding match in the other table, those rows will not be included in the result set.
SELECT SalesTran.* FROM SalesTran INNER JOIN Products 
ON SalesTran.ProductId = Products.ProductId
--Returns only columns from SalesTran
SELECT Products.* FROM SalesTran INNER JOIN Products 
ON SalesTran.ProductId = Products.ProductId

SELECT * FROM SalesTran AS S INNER JOIN Products AS P
ON S.ProductId = P.ProductId


SELECT S.* FROM SalesTran AS S INNER JOIN Products AS P
ON S.ProductId = P.ProductId


SELECT P.* FROM SalesTran AS S INNER JOIN Products AS P
ON S.ProductId = P.ProductId


SELECT P.ProductId,P.ProductName,S.InvoiceNum,S.Qty,S.Sales
FROM SalesTran AS S INNER JOIN Products AS P
ON S.ProductId = P.ProductId

SELECT P.ProductId,P.ProductName,S.InvoiceNum,S.Qty,S.Sales
FROM SalesTran  S INNER JOIN Products  P
ON S.ProductId = P.ProductId

SELECT * FROM SalesTran INNER JOIN Products 
ON SalesTran.ProductId = Products.ProductId

SELECT * FROM Products INNER JOIN   SalesTran
ON SalesTran.ProductId = Products.ProductId

SELECT * FROM SalesTran LEFT JOIN Products 
ON SalesTran.ProductId = Products.ProductId

SELECT * FROM Products LEFT JOIN  SalesTran
ON SalesTran.ProductId = Products.ProductId

SELECT * FROM SalesTran RIGHT JOIN Products 
ON SalesTran.ProductId = Products.ProductId