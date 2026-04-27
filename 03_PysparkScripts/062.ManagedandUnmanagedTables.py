# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)


#diff bw mamnaged and unmanaged tables:
#managed tables are the tables which are created and managed by databricks and they are stored in the default location of databricks which is /user/hive/warehouse. when we create a managed table and insert data into it, databricks will automatically manage the data and metadata of the table and when we drop the table databricks will automatically delete the data and metadata of the table. 
#unmanaged tables are the tables which are created and managed by the user and they are stored in the location specified by the user. when we create an unmanaged table and insert data into it, databricks will not manage the data and metadata of the table and when we drop the table databricks will not delete the data and metadata of the table. we have to manually delete the data and metadata of the table when we drop the table.

# COMMAND ----------
#Managaed table is created when we do not specify the path of the table while creating the table and unmanaged table is created when we specify the path of the table while creating the table. 

df.write.saveAsTable("tblorders")

# COMMAND ----------

# MAGIC %sql
# MAGIC describe table tblorders
# Schema (structure) of the table
# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail tblorders
#DETAIL gives us more information about the table like location, provider, etc.
#👉Detailed metadata of the table (especially Delta tables)
# COMMAND ----------

# MAGIC %sql
# MAGIC show tables

# COMMAND ----------

spark.catalog.listTables()

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table tblorders

# COMMAND ----------

# MAGIC %sql
# MAGIC create database testing

# COMMAND ----------

df.write.saveAsTable("testing.tblorders")

# COMMAND ----------

df.write.option("path","/FileStore/tables/Ext").saveAsTable("tblordersext")

# COMMAND ----------

df.write.option("path","/FileStore/tables/Ext2").saveAsTable("tblordersext")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from tblordersext

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail tblordersext

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table tblordersext

# COMMAND ----------

spark.catalog.listTables()

# COMMAND ----------

df.createTempView("vworders")

# COMMAND ----------

# MAGIC %sql
# MAGIC create table tblordersnew as
# MAGIC select * from vworders

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from tblordersnew

# COMMAND ----------


'''
DESCRIBE EXTENDED table_name;
DESCRIBE FORMATTED table_name;

Gives extra info like:
Location
Provider (parquet/delta)
Table properties'''
