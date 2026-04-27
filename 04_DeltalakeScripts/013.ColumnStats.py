# Databricks notebook source
df = spark.read.format("csv").option("path","/FileStore/tables/ColumnStats.csv").option("header",True).load()
display(df)

# COMMAND ----------

df.write.format("delta").option("path","/FileStore/tables/ColumnStatistics").saveAsTable("tblcolstats")

# COMMAND ----------

df_log = spark.read.format("json").option("path","/FileStore/tables/ColumnStatistics/_delta_log/00000000000000000000.json").load()
display(df_log)

'''
#reading log of file
By default it will do for 32 columns

It is used for skipping data using query used as it will not read unnecessry file

'''

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE
# MAGIC  tblcolstats
# MAGIC SET
# MAGIC  TBLPROPERTIES ('delta.dataSkippingNumIndexedCols' = 40);

# COMMAND ----------

df_log = spark.read.format("json").option("path","/FileStore/tables/ColumnStatistics/_delta_log/00000000000000000001.json").load()
display(df_log)


# COMMAND ----------

df.write.format("delta").option("path","/FileStore/tables/ColumnStatistics").mode("overwrite").saveAsTable("tblcolstats")

# COMMAND ----------

df_log = spark.read.format("json").option("path","/FileStore/tables/ColumnStatistics/_delta_log/00000000000000000002.json").load()
display(df_log)


# COMMAND ----------

