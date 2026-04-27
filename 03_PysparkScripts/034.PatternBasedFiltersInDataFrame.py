# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

df2 = df.filter(col("EnglishProductName").startswith("A"))
display(df2)

# COMMAND ----------

df2 = df.filter(col("EnglishProductName").startswith("a"))
display(df2)

# COMMAND ----------

df2 = df.filter(col("EnglishProductName").startswith("AW"))
display(df2)

# COMMAND ----------

df2 = df.filter(col("EnglishProductName").endswith("e"))
display(df2)

# COMMAND ----------

df2 = df.filter(col("EnglishProductName").contains("a"))
display(df2)

# COMMAND ----------

df2 = df.filter(col("EnglishProductName").like("A%"))
display(df2)

# COMMAND ----------

df2 = df.filter(col("EnglishProductName").like("%e"))
display(df2)

# COMMAND ----------

df2 = df.filter(col("EnglishProductName").like("%a%"))
display(df2)

# COMMAND ----------

df2 = df.filter(col("EnglishProductName").like("A_C%"))
display(df2)

# COMMAND ----------

