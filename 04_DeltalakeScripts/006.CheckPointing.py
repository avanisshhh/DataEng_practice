# Databricks notebook source
schema ="ProductId : int, ProductName : string"
df = spark.createDataFrame([(1,'Adjustable Race')],schema)
display(df)

# COMMAND ----------

df.write.format("delta").saveAsTable("Products")


# COMMAND ----------

lst = ['Bearing Ball','BB Ball Bearing','Headset Ball Bearings','Blade','LL Crankarm','ML Crankarm','HL Crankarm','Chainring Bolts','Chainring Nut']
for i in range(2,11):
    df = spark.createDataFrame([(i,lst[i-2])],schema)
    df.write.format("delta").mode("append").saveAsTable("Products")


# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from Products

# COMMAND ----------

df = spark.createDataFrame([(11,'Chainring')],schema)
df.write.format("delta").mode("append").saveAsTable("Products")

# COMMAND ----------

dfchk = spark.read.format("parquet").option("path","/user/hive/warehouse/products/_delta_log/00000000000000000010.checkpoint.parquet").load()
display(dfchk)

# COMMAND ----------

# MAGIC %sql
# MAGIC alter table Products set tblproperties ("delta.checkpointInterval" = "1")
#Default is 10

#checkpointInterval is a table property in Delta Lake that specifies the frequency at which checkpoint files are created for a Delta Lake table. A checkpoint file is a snapshot of the state of the Delta Lake table at a specific point in time, and it contains metadata about the table's schema, partitioning, and other properties. By setting the checkpointInterval to 1, you are instructing Delta Lake to create a checkpoint file after every transaction or operation that modifies the table. This can help improve query performance and reduce the time it takes to recover from failures, as the checkpoint files can be used to quickly restore the state of the table without having to replay all the transactions from the beginning.

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail products

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table products

# COMMAND ----------

