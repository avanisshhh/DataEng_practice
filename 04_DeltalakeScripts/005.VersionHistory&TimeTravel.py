# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True).option("inferSchema",True)
.load())
display(df)


# COMMAND ----------



# COMMAND ----------

df.write.format("delta").saveAsTable("tblproducts")

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history tblproducts

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC UPDATE tblproducts SET Country = 'USA' WHERE Country = 'United States'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tblproducts

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY tblproducts

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DELETE FROM tblproducts WHERE Country = 'USA'

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM tblproducts

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY tblproducts

# COMMAND ----------

# MAGIC %sql 
# MAGIC
# MAGIC SELECT * FROM tblproducts VERSION AS OF 0

# COMMAND ----------

# MAGIC %sql 
# MAGIC
# MAGIC SELECT * FROM tblproducts VERSION AS OF 1

# COMMAND ----------

# MAGIC %sql 
# MAGIC
# MAGIC SELECT * FROM tblproducts VERSION AS OF 2

# COMMAND ----------

# MAGIC %sql 
# MAGIC
# MAGIC SELECT * FROM tblproducts TIMESTAMP AS OF '2024-06-16T18:45:34.000+0000'

# COMMAND ----------

# MAGIC %sql
# MAGIC
#In order to get detailed table info use
# MAGIC DESCRIBE TABLE EXTENDED tblproducts

# COMMAND ----------

dfdt = spark.read.format("delta").option("versionAsOf", 0).load("/user/hive/warehouse/tblproducts")
display(dfdt)

# COMMAND ----------

dfdt = spark.read.format("delta").option("timeStampAsOf", "2024-06-16T18:45:34.000+0000").load("/user/hive/warehouse/tblproducts")
display(dfdt)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC RESTORE TABLE tblproducts TO VERSION AS OF 0
#Restore table to previous version 
# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM tblproducts

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY tblproducts

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DELETE FROM tblproducts WHERE Country = 'United States'

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY tblproducts

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC RESTORE TABLE tblproducts TO TIMESTAMP AS OF '2024-06-16T18:52:25.000+0000'

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY tblproducts

# COMMAND ----------

from delta.tables import *

# COMMAND ----------

help(DeltaTable.forName)

# COMMAND ----------

dtbl = DeltaTable.forName(spark,"tblproducts")
type(dtbl)

# COMMAND ----------

help(dtbl.restoreToVersion)

# COMMAND ----------

dtbl.restoreToVersion(2)

# COMMAND ----------

dtbl.restoreToTimestamp("2024-06-16T18:46:16.000+0000")

# COMMAND ----------

dtbl.restoreToVersion(10)

# COMMAND ----------

# MAGIC %sql
# MAGIC restore table tblproducts to version as of 1

# COMMAND ----------

dflog = (spark.read.format("json").
        option("path","/user/hive/warehouse/tblproducts/_delta_log/00000000000000000003.json").load())
display(dflog)

# COMMAND ----------

dflog = (spark.read.format("parquet").
        option("path","/user/hive/warehouse/tblproducts/_delta_log/00000000000000000003.checkpoint.parquet").load())
display(dflog)

# COMMAND ----------

