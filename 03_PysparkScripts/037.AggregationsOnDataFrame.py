# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

from pyspark.sql.functions import * 

# COMMAND ----------

df2=df.select(sum("SalesAmount"))
display(df2)

# COMMAND ----------

df2=df.select(sum("SalesAmount").alias("TotalSales"))
display(df2)

# COMMAND ----------

df2=df.select(round(sum("SalesAmount"),2).alias("TotalSales"))
#round it to 2 decimal places 
display(df2)

# COMMAND ----------

df2=df.select(round(avg("SalesAmount"),2).alias("AvgSales"))

display(df2)

# COMMAND ----------

df2=df.select(min("SalesAmount").alias("MinSales"))
display(df2)

# COMMAND ----------

df2=df.select(max("SalesAmount").alias("MinSales"))
display(df2)

# COMMAND ----------

df2=df.select(count("Country").alias("CountryRows"))
display(df2)

# COMMAND ----------

df2=df.select(countDistinct("Country").alias("CountryRows"))
display(df2)

# COMMAND ----------

df2=df.select(round(sum("SalesAmount"),2).alias("TotalSales"),round(avg("SalesAmount"),2).alias("AvgSales"))
display(df2)

# COMMAND ----------

df3=df.selectExpr("round(sum(SalesAmount),2) as TotalSales")
display(df3)

# COMMAND ----------

df3=df.selectExpr("round(sum(SalesAmount),2) as TotalSales","round(avg(SalesAmount),2) as AvgSales")
display(df3)

# COMMAND ----------


