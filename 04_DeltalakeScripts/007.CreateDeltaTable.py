# Databricks notebook source
dfproducts = spark.read.format("csv").option("path","/FileStore/tables/Products.csv").option("header",True).option("inferSchema",True).load()
display(dfproducts)

# COMMAND ----------

dfproducts.write.format("delta").saveAsTable("tblProductsNew")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE DATABASE IF NOT EXISTS MyDb

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS MyDb.Products
# MAGIC (
# MAGIC  ProductId INT,
# MAGIC  ProductName STRING
# MAGIC )
# MAGIC USING DELTA
#managed Table
# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS MyDb.Products2
# MAGIC (
# MAGIC  ProductId INT,
# MAGIC  ProductName STRING
# MAGIC )
# MAGIC USING DELTA
# MAGIC LOCATION '/FileStore/tables/Products2'

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE DETAIL MyDB.products

# COMMAND ----------

df = spark.read.format("json").option("path","/user/hive/warehouse/mydb.db/products/_delta_log/00000000000000000000.json").load()
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE TABLE EXTENDED Mydb.products

# COMMAND ----------

from delta.tables import *
#  delta table api operations
# COMMAND ----------

help(DeltaTable.createIfNotExists(spark))

# COMMAND ----------

(DeltaTable.createIfNotExists(spark)
 .tableName("Mydb.tblProducts")
.addColumn("ProductId","INT")
.addColumn("ProductName","STRING")
.addColumn("Price","DOUBLE")
.addColumn("StartDate","TIMESTAMP")
.execute()
)

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE EXTENDED Mydb.tblProducts

# COMMAND ----------

