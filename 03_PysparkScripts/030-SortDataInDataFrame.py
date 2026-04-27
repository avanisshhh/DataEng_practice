# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df2=df.sort("ProductKey")
display(df2)

# COMMAND ----------

df3=df.sort("Country","EnglishProductName")
display(df3)

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

df4=df.sort(col("Country").desc())
display(df4)

# COMMAND ----------

df4=df.sort(col("Country").desc(),col("EnglishProductName"))
display(df4)

# COMMAND ----------

df4=df.sort(col("Country").desc(),col("EnglishProductName").desc())
display(df4)

# COMMAND ----------

