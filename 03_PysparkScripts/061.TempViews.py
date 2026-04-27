# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

#local temp view:
df.createTempView("vwProducts")
#Benefit of temp view is we can use sql queries to query the data from dataframe and perform various operations on it. 
# 
# we can also create multiple temp views from the same dataframe and use them in different sql queries. temp view is session scoped so it will be available only in the current session and will be dropped automatically when the session ends.
# COMMAND ----------

# MAGIC %sql
# MAGIC select * from vwProducts

# COMMAND ----------

# MAGIC %sql
# MAGIC show databases

# COMMAND ----------

# MAGIC %sql
# MAGIC create database mydb

# COMMAND ----------

#catalog is used to get the list of databases and tables in the current session and also to perform various operations on them like creating database, dropping database, creating table, dropping table etc. it is a part of spark session and we can use it to perform various operations on databases and tables in databricks environment.
display(spark.catalog.listDatabases())

# COMMAND ----------

spark.catalog.listTables()


# COMMAND ----------

# MAGIC %sql
# MAGIC show tables

# COMMAND ----------

df.createTempView("vwProducts")

# COMMAND ----------

df.createOrReplaceTempView("vwProducts")
#in order to access temp view again use this 
# COMMAND ----------

df.createOrReplaceGlobalTempView("vwProductsGl")
#it can be accessible from anywher use prefix global_temp to access global temp view and it will be available across all sessions until we drop it explicitly. global temp view is also session scoped but it is available across all sessions until we drop it explicitly.
# COMMAND ----------

# MAGIC %sql
# MAGIC select * from global_temp.vwProductsGl

# COMMAND ----------

spark.catalog.dropTempView("vwProducts")
#dropTempView is used to drop the temp view 
# COMMAND ----------

# MAGIC %sql
# MAGIC select * from vwProducts

# COMMAND ----------

spark.catalog.dropGlobalTempView("vwProductsGl")
#dropGlobalTempView is used to drop the global temp view
# COMMAND ----------

# MAGIC %sql
# MAGIC select * from global_temp.vwProductsGl

# COMMAND ----------

