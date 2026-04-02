

SELECT GETDATE()
--GETDATE() is a built-in function in SQL Server that returns the current date and time of the system on which the SQL Server instance is running. The value returned by GETDATE() includes both the date and time components, and it is typically used to capture the current timestamp for various purposes, such as logging, auditing, or inserting records with a timestamp.
--eg: If you run the query on November 4, 2023, at 10:30:45 AM, GETDATE() will return '2023-11-04 10:30:45.000' (the exact format may vary based on your SQL Server settings).
SELECT SYSDATETIME()
--eg: If you run the query on November 4, 2023, at 10:30:45 AM, SYSDATETIME() will return '2023-11-04 10:30:45.1234567' (the exact format may vary based on your SQL Server settings).

SELECT SYSUTCDATETIME()
--eg: If you run the query on November 4, 2023, at 10:30:45 AM UTC, SYSUTCDATETIME() will return '2023-11-04 10:30:45.1234567' (the exact format may vary based on your SQL Server settings).

SELECT '2023-11-04'
--

SELECT DATEFROMPARTS(2023,11,4)

SELECT DATETIMEFROMPARTS(2023,11,4,8,15,45,0)