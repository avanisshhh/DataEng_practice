# Databricks notebook source
# MAGIC %run /Workspace/Users/avanish@datatailor.com/JDBC/Utilities

# COMMAND ----------

spark.conf.set("storage-account-key")


# COMMAND ----------

ADLS_Path = "abfss://mycontainer@mydatatraining.dfs.core.windows.net/IncrementalLoad/Sales/"

# COMMAND ----------

from pyspark.sql.functions import col, xxhash64, concat_ws

# COMMAND ----------

source_df = (spark.read.format("csv")
            .option("path",ADLS_Path)
            .option("header","true")
            .option("inferschema","true")
            .load().withColumn("SalesDate",col("SalesDate").cast("timestamp"))
            .withColumn("SalesAmount",col("SalesAmount").cast("decimal(19,4)"))
)
display(source_df)


# COMMAND ----------

target_df = ReadTableFromDatabase("dbo.Sales")
display(target_df)

# COMMAND ----------

source_hash_df = source_df.withColumn("HashKey",xxhash64(concat_ws("||", *source_df.columns)))
display(source_hash_df)

# COMMAND ----------


# target_hash_df = target_df.withColumn("HashKey",xxhash64(concat_ws("||", "SalesDate","Country")))
target_hash_df = target_df.withColumn("HashKey",xxhash64(concat_ws("||", *target_df.columns)))
display(target_hash_df)


# COMMAND ----------

delta_load = source_hash_df.join(target_hash_df,on="HashKey",how="left_anti")
display(delta_load)
#Rows present in source but NOT in target
# COMMAND ----------

final_df = delta_load.drop("HashKey")

# COMMAND ----------

WriteDataframeToDatabaseMode(final_df,"dbo.Sales","append")

#link: https://chatgpt.com/g/g-p-69a52d2d17f081918cc2e426c7dfa117-data-engineering/c/69d61721-f82c-8320-aea1-fad51077afbc