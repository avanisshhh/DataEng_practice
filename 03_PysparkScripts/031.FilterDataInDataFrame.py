# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df2=df.filter("ProductKey == 214")
display(df2)

# COMMAND ----------

df2=df.filter("ProductKey > 214")
display(df2)

# COMMAND ----------

df2=df.filter("ProductKey != 214")
display(df2)

# COMMAND ----------

df2=df.filter("Country =='Australia'")
display(df2)

# COMMAND ----------

df2=df.filter("ProductKey == 214 AND Country =='Australia'")
display(df2)

# COMMAND ----------

df2=df.filter("Country == 'Italy' OR Country =='Australia'")
display(df2)

# COMMAND ----------

df2=df.filter("SalesAmount >=1000 and SalesAmount <= 2000")
display(df2)

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

df2=df.filter(col("SalesAmount").between(1000,2000))
display(df2)

# COMMAND ----------

