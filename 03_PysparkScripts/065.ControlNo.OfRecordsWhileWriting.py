# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df.write.format("csv").option("path","/FileStore/tables/MaxRecords").option("header",True).option("maxRecordsPerFile",500).save()

# COMMAND ----------

df2 = (spark.read.format("csv")
.option("path","/FileStore/tables/MaxRecords/part-00000-tid-1409910137430413517-80ae5c82-7271-4fd8-8eab-64222b202683-3-1-c000.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df2)

# COMMAND ----------

display(dbutils.fs.ls("/FileStore/tables/MaxRecords/"))

# COMMAND ----------


