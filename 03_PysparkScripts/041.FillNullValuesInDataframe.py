# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/EmployeeNulls.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------
'''
data cleaning step in Spark

df.na.fill(0):
Replaces all NULL values in the DataFrame with 0

'''
df2=df.na.fill(0)
display(df2)

# COMMAND ----------

df2=df.na.fill("na")
display(df2)

# COMMAND ----------

df2=df.na.fill("na").na.fill(0)
display(df2)
'''
first part:
Replaces NULL values in string columns with "na"
Works only on string-type columns
Numeric columns remain unchanged
Second:
Replaces remaining NULL values in numeric columns with 0

'''

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

df3=df.withColumn("id",coalesce("id",lit(0)))
#coalesce is used to replace null values in a specific column here we are replacing null values in id column with 0
display(df3)

# COMMAND ----------

