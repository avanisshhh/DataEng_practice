# Databricks notebook source
server_name = "jdbc:sqlserver://ctdevmysqlserver1.database.windows.net"
database_name = "mytrainingsqldb "
url = server_name + ";" + "databaseName=" + database_name + ";"

table_name = "dbo.ordersnew"
username = dbutils.secrets.get("adbdevscope","sqlusername")
password = dbutils.secrets.get("adbdevscope","sqlpassword")


 


# COMMAND ----------

df = (spark.read.format("jdbc")
        .option("url",url)
        .option("dbtable", table_name)
        .option("user", username) 
        .option("password", password).load()) 
display(df)

# COMMAND ----------

sqlquery = "select orderdate, productkey , country, salesamount from ordersnew"

df2 = (spark.read.format("jdbc")
        .option("url",url)
        .option("query", sqlquery)
        .option("user", username) 
        .option("password", password).load()) 
display(df2)

# COMMAND ----------

 (df.write
    .format("jdbc")
    .option("url", url) 
    .option("dbtable", "neworders2")
    .option("user", username) 
    .option("password", password) 
    .save())

# COMMAND ----------

 (df.write
    .format("jdbc")
    .option("url", url) 
    .mode("overwrite")
    .option("dbtable", "Orders2")
    .option("user", username) 
    .option("password", password) 
    .save())

# COMMAND ----------

 (df.write
    .format("jdbc")
    .option("url", url) 
    .mode("append")
    .option("dbtable", "Orders2")
    .option("user", username) 
    .option("password", password) 
    .save())

# COMMAND ----------

df3 = (spark.read.format("jdbc")
        .option("url",url)
        .option("dbtable", "ordersnew")
        .option("user", username) 
        .option("numpartitions",10)
        #numpartitions option is used to specify the number of partitions to read the data from the database and fetchsize option is used to specify the number of rows to fetch in each round trip to the database. when we use numpartitions option it will create the specified number of partitions and it will read the data from the database in parallel and when we use fetchsize option it will fetch the specified number of rows in each round trip to the database which can improve the performance of reading data from the database as it reduces the number of round trips to the database.
        .option("password", password).load()) 
display(df3)

# COMMAND ----------

df4 = (spark.read.format("jdbc")
        .option("url",url)
        .option("dbtable", "ordersnew")
        .option("user", username) 
        .option("numpartitions",10)
        .option("fetchsize",20)
        .option("password", password).load())
#fetchsize option is used to specify the number of rows to fetch in each round trip to the database. when we use fetchsize option it will fetch the specified number of rows in each round trip to the database which can improve the performance of reading data from the database as it reduces the number of round trips to the database. 

display(df4)

# COMMAND ----------

df4 = (spark.read.format("jdbc")
        .option("url",url)
        .option("dbtable", "ordersnew")
        .option("user", username) 
        .option("numpartitions",5)
        .option("partitioncolumn","productkey")
        .option("lowerbound",1)
        .option("upperbound",1000)
        .option("password", password).load()) 
#lowerbound and upperbound options are used to specify the range of values for the partition column when we use partitioncolumn option to read the data from the database in parallel. when we use partitioncolumn option it will read the data from the database in parallel based on the values of the partition column and when we use lowerbound and upperbound options it will specify the range of values for the partition column which can improve the performance of reading data from the database as it allows us to read only a subset of data based on the values of the partition column.
display(df4)

# COMMAND ----------
#Truncate table using JDBC connection
driver_manager = spark._sc._gateway.jvm.java.sql.DriverManager
con = driver_manager.getConnection(url, username, password)
statement =f"""TRUNCATE TABLE dbo.neworders2"""
exec_statement = con.prepareCall(statement)

exec_statement.execute()

exec_statement.close()
con.close()


# COMMAND ----------
#Stored procedure execution using JDBC connection
driver_manager = spark._sc._gateway.jvm.java.sql.DriverManager
con = driver_manager.getConnection(url , username, password)
statement =f"""EXEC sp_InsertData3 '2023-04-01',310,'UK','TV',2000,200"""
exec_statement = con.prepareCall(statement)

exec_statement.execute()

exec_statement.close()
con.close()


# COMMAND ----------
#we can also pass the parameters to the stored procedure using the JDBC connection and we can also execute the stored procedure using the JDBC connection. here we are passing the parameters to the stored procedure sp_InsertData3 and executing it using the JDBC connection. we are passing the orderdate, productkey, country, product, sales and tax as parameters to the stored procedure and executing it using the JDBC connection.
orderdate = '2023-04-01'
productkey = 312
country = "UK"
product ="TV"
sales= 20000
tax = 2000

driver_manager = spark._sc._gateway.jvm.java.sql.DriverManager
con = driver_manager.getConnection(url, username, password)
statement =f"""EXEC sp_InsertData3 '{orderdate}',{productkey},'{country}','{product}',{sales},{tax}"""
print(statement)
exec_statement = con.prepareCall(statement)

exec_statement.execute()

exec_statement.close()
con.close()


# COMMAND ----------

