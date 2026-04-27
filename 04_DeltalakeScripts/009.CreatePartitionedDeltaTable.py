# Databricks notebook source
dfproducts = spark.read.format("csv").option("path","/FileStore/tables/Products.csv").option("header",True).option("inferSchema",True).load()
display(dfproducts)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE MyDb.tblProducts_Partitioned(
# MAGIC   OrderDate DATE,
# MAGIC   InvoiceNum STRING,
# MAGIC   ProductKey INTEGER,
# MAGIC   Country STRING,
# MAGIC   EnglishProductName STRING,
# MAGIC   SalesAmount DOUBLE,
# MAGIC   UnitPrice DOUBLE,
# MAGIC   OrderQuantity INTEGER,
# MAGIC   TaxAmt DOUBLE,
# MAGIC   TotalProductCost DOUBLE
# MAGIC )
# MAGIC USING DELTA
# MAGIC PARTITIONED BY (Country)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE EXTENDED mydb.tblproducts_partitioned

# COMMAND ----------

dfproducts.write.format("delta").mode("append").saveAsTable("MyDb.tblProducts_Partitioned")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from mydb.tblproducts_partitioned

# COMMAND ----------

df = spark.read.format("json").option("path","dbfs:/user/hive/warehouse/mydb.db/tblproducts_partitioned/_delta_log/00000000000000000000.json").load()
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE MyDb.tblProducts_Partitioned2(
# MAGIC   OrderDate DATE,
# MAGIC   InvoiceNum STRING,
# MAGIC   ProductKey INTEGER,
# MAGIC   Country STRING,
# MAGIC   EnglishProductName STRING,
# MAGIC   SalesAmount DOUBLE,
# MAGIC   UnitPrice DOUBLE,
# MAGIC   OrderQuantity INTEGER,
# MAGIC   TaxAmt DOUBLE,
# MAGIC   TotalProductCost DOUBLE,
# MAGIC   OrderYear INTEGER GENERATED ALWAYS AS (YEAR(OrderDate))
# MAGIC )
# MAGIC USING DELTA
# MAGIC PARTITIONED BY (Country,OrderYear)

# COMMAND ----------

dfproducts.write.format("delta").mode("append").saveAsTable("MyDb.tblProducts_Partitioned2")

# COMMAND ----------

