# Databricks notebook source
#create a dataframe from range and save as delta format
df = spark.range(1,11)
df.write.format("delta").save("/FileStore/tables/DeltaTables/tblrange")

# COMMAND ----------

#read delta format
df2 = spark.read.format("delta").load("/FileStore/tables/DeltaTables/tblrange")
df2.show()

# COMMAND ----------

#write as table
df.write.saveAsTable("tblrange_Managed") #creates a managed table

# COMMAND ----------

#write as table
df.write.option("path","/FileStore/tables/tblrangeUnmanaged").saveAsTable("tblrange_UnManaged") #creates an unmanaged table

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from tblrange  --query table
# MAGIC

# COMMAND ----------

spark.catalog.listTables() #list tables

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE delta.`/FileStore/tables/DeltaTables/tablerangenew` USING DELTA AS SELECT col1 as id FROM VALUES 1,2,3,4,5,6,7,8,9,10;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from delta.`/FileStore/tables/DeltaTables/tablerangenew`

# COMMAND ----------

