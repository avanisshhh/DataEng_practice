# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df2 = df.select("OrderDate")
display(df2)

# COMMAND ----------

df2 = df.select("OrderDate","EnglishProductName","SalesAmount")
display(df2)

# COMMAND ----------

df2 = df.selectExpr("OrderDate")
display(df2)

# COMMAND ----------

df2 = df.selectExpr("OrderDate","EnglishProductName","SalesAmount")
display(df2)

# COMMAND ----------
#Benefit of selectExpr is that we can write expressions in select statement here we added a new column vat which is 5% of SalesAmount and rounded to 2 decimal places

df4=df.selectExpr("OrderDate","EnglishProductName","SalesAmount","round(SalesAmount * 0.05,2) as vat")
display(df4)

# COMMAND ----------

from pyspark.sql.functions import expr

# COMMAND ----------

df4=df.select("OrderDate","EnglishProductName","SalesAmount",expr("round(SalesAmount * 0.05,2) as vat"))
display(df4)

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

df5 = df.select(col("OrderDate"),col("SalesAmount"))
display(df5)

# COMMAND ----------

from pyspark.sql.functions import col, expr

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------


