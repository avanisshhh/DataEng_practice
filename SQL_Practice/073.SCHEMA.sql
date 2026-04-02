
--For Specific sales purchase marketing schema

CREATE SCHEMA SALES


CREATE TABLE SALES.SalesTran(
	Orderid int,
	orderdate datetime,
	qty int
)

SELECT * FROM SalesTran

SELECT * FROM SALES.SalesTran


DROP SCHEMA SALES
--Will not work bcs there are some table exist
--first we have to delete table.



DROP TABLE SALES.SalesTran