# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df2=df.groupBy("Country").sum("SalesAmount")
display(df2)

# COMMAND ----------

df2=df.groupBy("Country","EnglishProductName").sum("SalesAmount")
display(df2)

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

df2=df.groupBy("Country","EnglishProductName").agg(round(sum("SalesAmount"),2).alias("TotalSales"))
display(df2)

# COMMAND ----------

df2=df.groupBy("Country","EnglishProductName").agg(round(sum("SalesAmount"),2).alias("TotalSales"),round(avg("SalesAmount"),2).alias("AvgSales"))
display(df2)

# COMMAND ----------


