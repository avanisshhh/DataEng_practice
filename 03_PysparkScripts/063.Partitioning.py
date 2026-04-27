# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df.write.option("path","/FileStore/tables/CountriesNew").partitionBy("Country").save()

# COMMAND ----------

df2 = (spark.read.format("parquet")
.option("path","/FileStore/tables/CountriesNew/Country=Australia/part-00000-f6383583-0cb7-4d71-ae5b-626beb010e6e.c000.snappy.parquet")
.load())
display(df2)

# COMMAND ----------

# MAGIC %sql
# MAGIC SET spark.databricks.delta.formatCheck.enabled=false

# COMMAND ----------

df2 = (spark.read.format("parquet")
.option("path","/FileStore/tables/CountriesNew/Country=Australia/part-00000-f6383583-0cb7-4d71-ae5b-626beb010e6e.c000.snappy.parquet")
.load())
display(df2)

# COMMAND ----------

df3 = (spark.read.format("delta")
.option("path","/FileStore/tables/CountriesNew/")
.load())
display(df3)

# COMMAND ----------

df.write.option("path","/FileStore/tables/CountriesNew").partitionBy("Country","EnglishProductName").save()

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

dfnew = df.withColumn("Year",year("OrderDate"))
display(dfnew)

# COMMAND ----------

dfnew.write.option("path","/FileStore/tables/CountriesNew2").partitionBy("Country","Year").save()

# COMMAND ----------

df5 = (spark.read.format("delta")
.option("path","/FileStore/tables/CountriesNew2/")
.load())
display(df5)

# COMMAND ----------

df5.createTempView("countries")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from countries where country = 'Australia'

# COMMAND ----------



# COMMAND ----------

