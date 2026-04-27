# Databricks notebook source
spark.conf.set(
    "access-key")



# COMMAND ----------

df = (spark.read.format("csv")
.option("path","abfss://mycontainer@cdudevmyadls.dfs.core.windows.net/CSVfiles/tripdata/tripdataNew.csv")
.load())

# COMMAND ----------

df = (spark.read.format("csv")
.option("path","abfss://mycontainer@cdudevmyadls.dfs.core.windows.net/CSVfiles/tripdata/tripdataNew.csv")
.option("header",True)
.load())

# COMMAND ----------

df = (spark.read.format("csv")
.option("path","abfss://mycontainer@cdudevmyadls.dfs.core.windows.net/CSVfiles/tripdata/tripdataNew.csv")
.option("header",True)
.option("inferschema",True)
.load())

# COMMAND ----------

df = (spark.read.format("csv")
.option("path","abfss://mycontainer@cdudevmyadls.dfs.core.windows.net/CSVfiles/tripdata/tripdataNew.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df.rdd.getNumPartitions()

# COMMAND ----------

spark.conf.get("spark.sql.files.maxPartitionBytes")

# COMMAND ----------

134217728/1024/1024

# COMMAND ----------

spark.conf.set("spark.sql.files.maxPartitionBytes",512*1024*1024)

# COMMAND ----------

df2 = (spark.read.format("csv")
.option("path","abfss://mycontainer@cdudevmyadls.dfs.core.windows.net/CSVfiles/tripdata/tripdataNew.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df2)

# COMMAND ----------

spark.conf.set("spark.sql.files.maxPartitionBytes",256*1024*1024)

# COMMAND ----------

df3= (spark.read.format("csv")
.option("path","abfss://mycontainer@cdudevmyadls.dfs.core.windows.net/CSVfiles/tripdata/tripdataNew.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df3)

# COMMAND ----------

df3.rdd.getNumPartitions()

# COMMAND ----------

from pyspark.sql.functions import spark_partition_id

# COMMAND ----------

display(df3.groupBy(spark_partition_id()).count())


# COMMAND ----------


