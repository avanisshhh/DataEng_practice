

SELECT YEAR(OrderDate) OrderYear ,SUM(SalesAmount) TotalSales
FROM FactInternetSales
GROUP BY YEAR(OrderDate)


SELECT YEAR(OrderDate) OrderYear ,SUM(SalesAmount) TotalSales
FROM FactInternetSales
GROUP BY ROLLUP(YEAR(OrderDate))
--NULL row = Grand Total 
'''It adds hierarchical totals
Year-wise totals
Grand Total
'''
SELECT YEAR(OrderDate) OrderYear ,FORMAT(OrderDate,'MMM') MonthNm,
SUM(SalesAmount) TotalSales
FROM FactInternetSales
GROUP BY YEAR(OrderDate),FORMAT(OrderDate,'MMM')


SELECT YEAR(OrderDate) OrderYear , MONTH(OrderDate) MonthNum,
SUM(SalesAmount) TotalSales
FROM FactInternetSales
GROUP BY ROLLUP(YEAR(OrderDate),MONTH(OrderDate))


SELECT ISNULL(FORMAT(OrderDate,'yyyy'),'Grand Total') OrderYear ,
SUM(SalesAmount) TotalSales
FROM FactInternetSales
GROUP BY ROLLUP(FORMAT(OrderDate,'yyyy'))
--Replaces NULL with readable label


SELECT ISNULL(FORMAT(OrderDate,'yyyy'),'Grand Total') OrderYear ,
ISNULL(FORMAT(OrderDate,'MM'),FORMAT(OrderDate,'yyyy') + ' Total') MonthNum,
SUM(SalesAmount) TotalSales
FROM FactInternetSales
GROUP BY ROLLUP(FORMAT(OrderDate,'yyyy'),FORMAT(OrderDate,'MM'))

'''
Month is NULL → show "Year Total"
Year is NULL → show "Grand Total"
Using FORMAT() in GROUP BY is slow

ROLLUP creates hierarchical aggregates, giving detailed rows, subtotals, and grand total in a single query.
'''

--Better version:
SELECT 
    ISNULL(CAST(YEAR(OrderDate) AS VARCHAR), 'Grand Total') AS OrderYear,
    ISNULL(CAST(MONTH(OrderDate) AS VARCHAR),
           CAST(YEAR(OrderDate) AS VARCHAR) + ' Total') AS MonthNum,
    SUM(SalesAmount) AS TotalSales
FROM FactInternetSales
GROUP BY ROLLUP(YEAR(OrderDate), MONTH(OrderDate));