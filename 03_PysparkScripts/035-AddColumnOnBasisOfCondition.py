# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

from pyspark.sql.functions import col, when

# COMMAND ----------

df2=df.withColumn("Tier",when(col("Country")=="Australia",1))
display(df2)

# COMMAND ----------

df2=df.withColumn("Tier",when(col("Country")=="Australia",1).otherwise(0))
display(df2)

# COMMAND ----------

df2=df.withColumn("Tier",when(col("Country")=="Australia",1).when(col("Country")=="Canada",2).when(col("Country")=="France",3).when(col("Country")=="Italy",4).otherwise(5))
display(df2)

# COMMAND ----------


