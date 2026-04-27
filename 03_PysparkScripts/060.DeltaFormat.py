# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df.write.format("delta").option("path","/FileStore/tables/DeltaFormat").save()
#delta format is a open source storage layer that brings ACID transactions to Apache Spark and big data workloads. It provides features like versioning, schema enforcement, and time travel, making it easier to manage and analyze large datasets efficiently.
# COMMAND ----------

df2 = (spark.read.format("json")
.option("path","/FileStore/tables/DeltaFormat/_delta_log/00000000000000000000.json")
.load())
display(df2)

# COMMAND ----------

df3 = (spark.read.format("delta")
.option("path","/FileStore/tables/DeltaFormat/")
.load())
display(df3)

# COMMAND ----------

df3 = (spark.read.format("delta")
.option("path","/FileStore/tables/park/")
.load())
display(df3)

# COMMAND ----------

df3 = (spark.read.format("parquet")
.option("path","/FileStore/tables/park/")
.load())
display(df3)

#Delta vs paraquet file format
#Delta format is a storage layer that provides ACID transactions, versioning, and schema enforcement, while Parquet is a columnar storage file format optimized for read performance. Delta format allows for efficient data management and analysis, while Parquet focuses on efficient storage and retrieval of data. Delta format is built on top of Parquet, providing additional features for data management and analysis, while Parquet is a standalone file format that can be used independently for storing and querying data.

# COMMAND ----------

