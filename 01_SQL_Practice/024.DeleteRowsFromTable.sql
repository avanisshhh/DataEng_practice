DROP TABLE DimProduct_BkUP
--drops the DimProduct_BkUP table from the database. This action is irreversible and will permanently remove the table and all of its data.
SELECT * INTO DimProduct_BkUP FROM DimProduct

DELETE FROM DimProduct_BkUP

DELETE FROM DimProduct_BkUP
WHERE COLOR = 'RED'

SELECT * FROM DimProduct_BkUP

TRUNCATE TABLE DimProduct_BkUP
WHERE COLOR = 'RED'
--truncate table does not support where clause. It removes all rows from the table and cannot be used to delete specific rows based on a condition. If you want to delete specific rows, you should use the DELETE statement with a WHERE clause instead.