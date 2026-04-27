# Databricks notebook source
df = spark.read.format("csv").option("path","/FileStore/tables/Employees.csv").option("inferschema",True).option("header",True).load()
display(df)

# COMMAND ----------

df.write.saveAsTable("tbl_Employee")

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL tbl_Employee

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE tbl_employee SET salary = 50000 WHERE ID = 7

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from tbl_employee

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE tbl_Employee 
# MAGIC SET TBLPROPERTIES (delta.enableChangeDataFeed = true)
'''
IT also create a folder with name _change_data in the location of delta table where it will store the change data feed in parquet format

'''
# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL tbl_Employee

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE tbl_employee SET salary = 50000 WHERE ID = 6

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY tbl_employee

# COMMAND ----------

# MAGIC %sql
# MAGIC SET spark.databricks.delta.formatCheck.enabled=false

# COMMAND ----------

dfchanges =spark.read.format("parquet").option("path","/user/hive/warehouse/tbl_employee/_change_data/cdc-00000-de267a42-2723-444f-88dc-6052477ba60d.c000.snappy.parquet").load()
display(dfchanges)
'''
Reading the change data feed of a delta table. It will read the change data feed of a delta table and display it in a tabular format. The change data feed contains information about the changes that have occurred in the delta table, such as inserts, updates, and deletes. By reading the change data feed, you can track the history of changes made to the delta table and analyze how the data has evolved over time.
'''
# COMMAND ----------

dfchange2 =spark.read.format("parquet").option("path","/user/hive/warehouse/tbl_employee/_change_data/cdc-00000-35996073-4f51-439c-b07a-407939255b4f.c000.snappy.parquet").load()
display(dfchange2)


# COMMAND ----------

# MAGIC %sql
# MAGIC DELETE FROM tbl_employee where ID = 10

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO tbl_employee VALUES
# MAGIC (11,'Yusuf','PUNE',30000)

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY tbl_employee

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM table_changes('tbl_employee',2)
#table_changes function is used to read the change data feed of a delta table. It takes the table name and the version number as input and returns the changes that occurred in that version. The changes can include inserts, updates, and deletes that happened in the specified version of the delta table. This function is useful for tracking changes to the data over time and can be used for auditing, debugging, or building applications that need to react to data changes.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM table_changes('tbl_employee',2,4)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM table_changes('tbl_employee', '2024-10-04T15:04:21.000+00:00', '2024-10-04T15:05:46.000+00:00')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM table_changes('tbl_employee', '2024-10-04T14:15:00.000+00:00')

# COMMAND ----------

dfchangesnew = (spark.read.format("delta") 
 .option("readChangeFeed", "true") 
 .option("startingVersion", 2) 
 .option("endingVersion", 4) 
 .table("tbl_employee")
)
display(dfchangesnew)

# COMMAND ----------

dfchangesnew2= (spark.read.format("delta")
 .option("readChangeFeed", "true")
 .option("startingTimestamp", "2024-10-04T14:41:48.000+00:00")
 .option("endingTimestamp", "2024-10-04T14:43:22.000+00:00")
 .table("tbl_employee")
)
display(dfchangesnew2)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS tbl_employee2 (
# MAGIC   ID INTEGER,
# MAGIC   NAME STRING,
# MAGIC   CITY STRING,
# MAGIC   SALARY DOUBLE
# MAGIC ) 
# MAGIC TBLPROPERTIES (delta.enableChangeDataFeed = true);
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL tbl_employee2

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table tbl_Employee2

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC set spark.databricks.delta.properties.defaults.enableChangeDataFeed = true
# MAGIC

# COMMAND ----------

#benefitof enabling change data feed at the table level is that it allows you to track and capture changes to the data in that specific table. This can be useful for auditing, debugging, or building applications that need to react to data changes. By enabling change data feed at the table level, you can easily access the change history of that table and analyze how the data has evolved over time. Additionally, it can help with troubleshooting and identifying issues by providing a detailed record of all changes made to the data in that table.