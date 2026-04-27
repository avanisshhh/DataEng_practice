
SELECT SUM(SalesAmount) FROM FactInternetSales

SELECT YEAR(OrderDate) OrderYear,SUM(SalesAmount) TotalSales,
FORMAT(SUM(SalesAmount) /(SELECT SUM(SalesAmount) FROM FactInternetSales),'P')
Contribution
FROM FactInternetSales
GROUP BY YEAR(OrderDate)
ORDER BY YEAR(OrderDate)


--format(...,p) is used to format the output as a percentage. In this case, it takes the result of the division (SUM(SalesAmount) / (SELECT SUM(SalesAmount) FROM FactInternetSales)) and formats it as a percentage string. The 'P' format specifier indicates that the value should be displayed as a percentage, which means it will multiply the value by 100 and append a '%' symbol to the end. For example, if the division results in 0.25, it will be formatted as '25.00%'. This allows for easier interpretation of the contribution of each year's sales amount to the total sales amount.