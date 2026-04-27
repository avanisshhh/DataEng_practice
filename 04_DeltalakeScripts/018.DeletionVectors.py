# Databricks notebook source
df = spark.range(100000000)

# COMMAND ----------

df.write.saveAsTable("tblids")

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TBLPROPERTIES tblids

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL tblids

# COMMAND ----------

# MAGIC %sql
# MAGIC DELETE FROM tblids where id = 182638

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE tblids SET TBLPROPERTIES ('delta.enableDeletionVectors' = true);
#enableDeletionVectors: Deletion vectors are a feature that enables efficient handling of deleted records in a Delta Lake table. 

'''
when u delete something it will not rewrite the parquet file instead it will create a deletevector file and mark the file for deletion when u do vaccume 
THis situation is soft delete.
'''
# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL tblids

# COMMAND ----------

# MAGIC %sql
# MAGIC DELETE FROM tblids where id = 37535

# COMMAND ----------


df  = spark.read.json("/user/hive/warehouse/tblids/_delta_log/00000000000000000003.json")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC SET spark.databricks.delta.retentionDurationCheck.enabled = false

# COMMAND ----------

# MAGIC %sql
# MAGIC REORG TABLE tblids APPLY (PURGE);
'''In order to delete physically u hv to run REORG TABLE tblids APPLY (PURGE);
This command will permanently delete the data files 
associated with the deleted records in the tblids table.'''

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM tblids RETAIN 0 HOURS
'''
after soft delete and physical delete run vaccum command to delete the file which are marked for deletion
'''

# COMMAND ----------

df  = spark.read.json("/user/hive/warehouse/tblids/_delta_log/00000000000000000003.json")
display(df)

# COMMAND ----------


df  = spark.read.json("/user/hive/warehouse/tblids/_delta_log/00000000000000000004.json")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC DELETE FROM tblids where id = 645433

# COMMAND ----------

# MAGIC %sql
# MAGIC DELETE FROM tblids where id = 253425

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL tblids

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM tblids RETAIN 0 HOURS

# COMMAND ----------

# MAGIC %sql
# MAGIC DELETE FROM tblids where id in(253420,83535,172632,9742)
#this will gen only one deletion vector file as all the deletes are in the same version of the delta table. If the deletes were in different versions, then multiple deletion vector files would be generated.
# COMMAND ----------


df  = spark.read.json("/user/hive/warehouse/tblids/_delta_log/00000000000000000007.json")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL tblids

# COMMAND ----------


df  = spark.read.json("/user/hive/warehouse/tblids/_delta_log/00000000000000000009.json")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table tblids

# COMMAND ----------

