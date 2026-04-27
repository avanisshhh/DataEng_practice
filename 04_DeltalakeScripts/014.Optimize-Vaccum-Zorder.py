# Databricks notebook source
df = spark.read.format("csv").option("path","/FileStore/tables/Products.csv").option("header",True).load()
display(df)
'''
Here we catering with small file problem

'''
# COMMAND ----------

# dbutils.fs.rm("/user/hive/warehouse/tblperformance/",recurse=True)
# dbutils.fs.rm("/user/hive/warehouse/tblperformanceNew/",recurse=True)
# dbutils.fs.rm("/user/hive/warehouse/tblperformanceZ/",recurse=True)

#recurse option is used to delete the directory and all its contents. If you set recurse to true, it will delete the directory and all files and subdirectories within it. If you set recurse to false, it will only delete the directory if it is empty, and it will not delete any files or subdirectories within it. In this case, since we want to delete the entire directory along with its contents, we set recurse to true.
# COMMAND ----------

# %sql
# drop table tblPerformance;
# drop table tblPerformanceNew;
# drop table tblPerformanceZ

# COMMAND ----------

df.repartition(4).write.format("delta").saveAsTable("tblPerformance")
'''
Breaking data into multiple file
'''
# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY tblPerformance

# COMMAND ----------

dflog = spark.read.format("json").option("path","/user/hive/warehouse/tblperformance/_delta_log/00000000000000000000.json").load()
display(dflog)

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE tblperformance SET COUNTRY = 'USA' WHERE COUNTRY = 'United States'

# COMMAND ----------
spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled","false")
'''
#check retention duration 

By default true.

It have two type of rentention : log and file 
Delta Table retention : 30 days
Deleted file retention : 7 days

'''

# COMMAND ----------



# MAGIC %sql
# MAGIC VACUUM tblperformance RETAIN 0 HOURS DRY RUN
# DRY RUN option is used to check which files will be deleted without actually deleting them. It allows you to see the list of files that would be removed if you were to run the VACUUM command without the DRY RUN option. This can be useful for verifying that you are not accidentally deleting important data before executing the actual VACUUM command.

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE tblperformance 

''' 
limit up of 1gb
 convert small into big file and mark the file to be deleted and it will be deleted when we run vacuum command

'''
# The OPTIMIZE command is used to optimize the layout of data files in a Delta Lake table. It can help improve query performance by reducing the number of files that need to be read during query execution. The OPTIMIZE command can be run on a specific partition or on the entire table, and it can also be used with ZORDER BY to optimize the layout of data based on specific columns.
# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM tblperformance RETAIN 0 HOURS 

''' 
delete small files created by the OPTIMIZE command

'''
#To delete small files created by the OPTIMIZE command, you can use the VACUUM command with a retention period of 0 hours. This will remove all files that are no longer needed for the current state of the Delta Lake table, including any small files that were created during the optimization process. It's important to note that using a retention period of 0 hours will permanently delete these files, so make sure to review the files that will be removed before executing the VACUUM command.
# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY tblperformance

# COMMAND ----------

dflog = spark.read.format("json").option("path","/user/hive/warehouse/tblperformance/_delta_log/00000000000000000001.json").load()
display(dflog)

# COMMAND ----------

spark.conf.get("spark.databricks.delta.optimize.maxFileSize") 

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC VACUUM tblperformance RETAIN 0 HOURS

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY tblperformance

# COMMAND ----------

from delta.tables import *
deltaTable = DeltaTable.forName(spark,"tblPerformance")
deltaTable.logRetentionDuration  = "interval 40 days"
deltaTable.deletedFileRetentionDuration  = "interval 10 days"  

# COMMAND ----------

deltaTable.logRetentionDuration

# COMMAND ----------

deltaTable.deletedFileRetentionDuration

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE tblperformance WHERE  Country = 'India'

# COMMAND ----------

df.repartition(4).write.format("delta").partitionBy("Country").saveAsTable("tblPerformanceNew")

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE tblPerformanceNew WHERE Country = 'India'

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM tblperformanceNew RETAIN 0 HOURS 

# COMMAND ----------

df.repartition(7).write.format("delta").saveAsTable("tblPerformanceZ")

# COMMAND ----------

# MAGIC %sql
# MAGIC SET spark.databricks.delta.formatCheck.enabled=false

# COMMAND ----------

df2 = spark.read.format("parquet").option("path","/user/hive/warehouse/tblperformancez/part-00000-47b51ff6-f688-4b85-bd32-8889ee8cbc89-c000.snappy.parquet").load()
display(df2)


# COMMAND ----------
'''
ZOrder cmd corelated the data basically it will try to store same data at one place
'''
# MAGIC %sql
# MAGIC OPTIMIZE tblperformanceZ ZORDER BY (Country)


#ZORDER BY is used to optimize the layout of data based on specific columns. When you use ZORDER BY, Delta Lake will organize the data files in a way that minimizes the amount of data that needs to be read during query execution for queries that filter on the specified columns. This can help improve query performance by reducing the number of files that need to be read and processed. In this case, by using ZORDER BY (Country), Delta Lake will optimize the layout of data files based on the Country column, which can help speed up queries that filter on the Country column.

# COMMAND ----------

