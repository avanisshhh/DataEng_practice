SELECT ProductId,InvoiceNum,OrderDate,City,Qty,
FIRST_VALUE(QTY) OVER(ORDER BY OrderDate) FirstVal
FROM Orders

SELECT ProductId,InvoiceNum,OrderDate,City,Qty,
FIRST_VALUE(QTY) OVER(PARTITION BY City ORDER BY OrderDate) FirstVal
FROM Orders


SELECT ProductId,InvoiceNum,OrderDate,City,Qty,
LAST_VALUE(QTY) OVER(ORDER BY OrderDate) LastVal
FROM Orders
--LAST_VALUE() returns the last value up to the current row, NOT the last value of the full dataset.

SELECT ProductId,InvoiceNum,OrderDate,City,Qty,
LAST_VALUE(QTY) OVER(ORDER BY (SELECT 0)) LastVal
FROM Orders
--(SELECT 0) → no real ordering (all rows treated equal)

SELECT ProductId,InvoiceNum,OrderDate,City,Qty,
LAST_VALUE(QTY) OVER(PARTITION BY CITY ORDER BY (SELECT 0)) LastVal
FROM Orders


'''
Why LAST_VALUE is not working as expected?”
Because by default LAST_VALUE works within the window frame ending at the current row. To get the actual last value, we must extend the frame to UNBOUNDED FOLLOWING.
'''

LAST_VALUE(QTY) OVER(
    ORDER BY OrderDate
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
)