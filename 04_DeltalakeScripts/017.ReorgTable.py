# Databricks notebook source
df = spark.read.format("csv").option("path","/FileStore/tables/Employees.csv").option("inferschema",True).option("header",True).load()
display(df)

# COMMAND ----------

df.write.saveAsTable("employees")

# COMMAND ----------

dflog = spark.read.format("json").option("path","/user/hive/warehouse/employees/_delta_log/00000000000000000000.json").load()
display(dflog)

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE employees
# MAGIC DROP COLUMN CITY

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE employees SET TBLPROPERTIES (
# MAGIC    'delta.columnMapping.mode' = 'name',
# MAGIC    'delta.minReaderVersion' = '2',
# MAGIC    'delta.minWriterVersion' = '5')

# COMMAND ----------

dflog2 = spark.read.format("json").option("path","/user/hive/warehouse/employees/_delta_log/00000000000000000001.json").load()
display(dflog2)

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE employees
# MAGIC DROP COLUMN CITY

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM employees

# COMMAND ----------

dflog2 = spark.read.format("json").option("path","/user/hive/warehouse/employees/_delta_log/00000000000000000002.json").load()
display(dflog2)

# COMMAND ----------

# MAGIC %sql
# MAGIC SET spark.databricks.delta.formatCheck.enabled=false

# COMMAND ----------

dfdata = spark.read.format("parquet").option("path","/user/hive/warehouse/employees/part-00000-db0c957a-c9f2-4cc0-b807-8cfeb954935a-c000.snappy.parquet").load()
display(dfdata)


# COMMAND ----------

# MAGIC %sql
# MAGIC REORG TABLE employees APPLY(PURGE)
'''
Diff name for delete
'''
#purge option is used to permanently delete the data files associated with the dropped column. When you drop a column from a delta table, the data files that contain the data for that column are not immediately deleted. Instead, they are marked for deletion and will be removed during the next REORG TABLE operation. By using the PURGE option, you can ensure that these files are permanently deleted and will not take up storage space in your delta lake. It's important to note that once the files are purged, they cannot be recovered, so make sure to review the data before executing the REORG TABLE command with the PURGE option.
# COMMAND ----------

dflog3 = spark.read.format("json").option("path","/user/hive/warehouse/employees/_delta_log/00000000000000000003.json").load()
display(dflog3)

# COMMAND ----------

dfdata = spark.read.format("parquet").option("path","/user/hive/warehouse/employees/6O/part-00000-03bd8eb0-f37b-493c-83fe-cb1557278d73-c000.snappy.parquet").load()
display(dfdata)


# COMMAND ----------

# MAGIC %sql
# MAGIC optimize employees

# COMMAND ----------

# MAGIC %sql
# MAGIC set spark.databricks.delta.retentionDurationCheck.enabled = false

# COMMAND ----------

# MAGIC %sql
# MAGIC vacuum employees retain 0 hours

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM employees

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table employees

# COMMAND ----------

