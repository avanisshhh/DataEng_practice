# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

from pyspark.sql.functions import col, upper,lower,initcap

# COMMAND ----------

df2=df.withColumn("Country",upper(col("country")))
display(df2)

# COMMAND ----------

df3=df2.withColumn("Country",lower(col("country")))
display(df3)

# COMMAND ----------

df2=df.withColumn("EnglishProductName",lower(col("EnglishProductName"))).withColumn("EnglishProductName",initcap(col("EnglishProductName")))
display(df2)

# COMMAND ----------


