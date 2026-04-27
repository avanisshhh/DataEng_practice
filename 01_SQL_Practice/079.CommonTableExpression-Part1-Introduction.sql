
'''
A CTE (Common Table Expression) is a temporary result set that you define inside a query using WITH. Think of it as a named subquery that makes your SQL cleaner and easier to manage.
'''
WITH CteSelectData
AS
(
	SELECT ProductKey,YEAR(OrderDate) OrderYear ,SalesAmount 
	FROM FactInternetSales
)
SELECT ProductKey,OrderYear,SUM(SalesAmount) TotalSales FROM CteSelectData
GROUP BY ProductKey,OrderYear

