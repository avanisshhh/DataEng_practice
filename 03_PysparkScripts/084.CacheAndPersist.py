# Databricks notebook source
df1 = (spark.read.format("csv")
    .option("header",True)
    .option("inferSchema",True)
    .option("path","/FileStore/tables/Products.csv").load()
)
# display(df1)

# COMMAND ----------
'''
Identify the base dataframe and perform the following transformations on it.
cache like df2.cache() as base dataframe and perform the following transformations on it.



'''
df2 = df1.select("OrderDate","InvoiceNum","ProductKey","EnglishProductName","Country","SalesAmount")

# COMMAND ----------

from pyspark.sql.functions import * 

# COMMAND ----------

df3 = df2.withColumn("Vat",expr("SalesAmount * 0.05 as Vat"))

# COMMAND ----------

df4 = df3.filter("Country='India'")

# COMMAND ----------

df1.count()

# COMMAND ----------

df2.count()

# COMMAND ----------

df3.count()

# COMMAND ----------

df4.count()

# COMMAND ----------

df2.cache()
#cache the dataframe in memory for faster access
# COMMAND ----------

df2.count()

# COMMAND ----------

df1.is_cached

# COMMAND ----------

df2.is_cached
#check the cache status of the dataframe
# COMMAND ----------

df2.unpersist()
#remove df from cache
# COMMAND ----------


#👉 StorageLevel defines how Spark stores (persists/caches) your DataFrame or RDD
from pyspark.storagelevel import StorageLevel

# COMMAND ----------

help(StorageLevel)

# COMMAND ----------

df2.persist(StorageLevel.MEMORY_ONLY)
#“Store this DataFrame in memory only”
# COMMAND ----------

df2.count()

# COMMAND ----------

df2.unpersist()

# COMMAND ----------

df2.persist(StorageLevel.MEMORY_ONLY_SER)
'''
✔ Serialized (compressed) in memory
✔ Saves space
❌ Slightly slower (needs deserialization)
'''
# COMMAND ----------

df2.persist(StorageLevel.MEMORY_AND_DISK)
'''
✔ Stores in memory
✔ Extra spills to disk
✔ Most commonly used
'''
# COMMAND ----------

df2.count()

# COMMAND ----------

df2.unpersist()

# COMMAND ----------

df2.persist(StorageLevel.DISK_ONLY)

# COMMAND ----------

df2.count()

# COMMAND ----------

df2.unpersist()

# COMMAND ----------

df2.persist(StorageLevel.MEMORY_ONLY_2)
#create 2 replicas of the dataframe in memory
# COMMAND ----------

df2.count()

# COMMAND ----------

df2.unpersist()

# COMMAND ----------

df2.persist(StorageLevel.DISK_ONLY_3 )

# COMMAND ----------

df2.count()

# COMMAND ----------

display(df3)

# COMMAND ----------


