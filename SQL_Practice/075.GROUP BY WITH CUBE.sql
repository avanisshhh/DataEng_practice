SELECT YEAR(OrderDate) OrderYear ,SUM(SalesAmount) TotalSales
FROM FactInternetSales
GROUP BY YEAR(OrderDate)


SELECT YEAR(OrderDate) OrderYear ,SUM(SalesAmount) TotalSales
FROM FactInternetSales
GROUP BY ROLLUP(YEAR(OrderDate))


SELECT YEAR(OrderDate) OrderYear ,SUM(SalesAmount) TotalSales
FROM FactInternetSales
GROUP BY CUBE(YEAR(OrderDate))
---Generates ALL possible combinations of the grouping columns, including subtotals and grand totals.


SELECT YEAR(OrderDate) OrderYear ,FORMAT(OrderDate,'MMM') MonthNm,
SUM(SalesAmount) TotalSales
FROM FactInternetSales
GROUP BY CUBE(YEAR(OrderDate),FORMAT(OrderDate,'MMM'))