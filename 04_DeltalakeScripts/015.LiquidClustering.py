# Databricks notebook source
# MAGIC %md ##Liquid clustering
# MAGIC 1. Delta Lake liquid clustering replaces table partitioning and ZORDER.
# MAGIC 2. It simplifies data layout decisions and optimizes query performance. 
# MAGIC 3. It provides flexibility to redefine clustering keys without rewriting existing data, this allows data layout to evolve as per demand over the time

# COMMAND ----------

# MAGIC %md ##Use Cases
# MAGIC Tables often filtered by high cardinality columns.
#cardinality refers to the number of unique values in a column. High cardinality columns have a large number of unique values, which can lead to performance issues when filtering or querying the data. For example, if you have a table with a UserID column that has millions of unique user IDs, this would be considered a high cardinality column. When you filter on this column, it may require scanning through a large number of records to find the relevant data, which can slow down query performance. Liquid clustering can help optimize the layout of data based on these high cardinality columns, improving query performance by reducing the amount of data that needs to be read during query execution.
# MAGIC
# MAGIC Tables with significant skew in data distribution.
#skew in data distribution refers to an uneven distribution of data across different values of a column. For example, if you have a table with a Country column and most of the records belong to a few countries while other countries have very few records, this would be considered skewed data distribution. Skewed data can lead to performance issues during query execution, as it may require scanning through a large number of records for the skewed values while only a few records for the less common values. Liquid clustering can help address this issue by dynamically organizing the data based on the actual distribution, which can improve query performance.
# MAGIC
# MAGIC Tables that grow quickly and require maintenance and tuning effort.
# MAGIC
# MAGIC Tables with concurrent write requirements.
# MAGIC
# MAGIC Tables with access patterns that change over time.
# MAGIC
# MAGIC Tables where a typical partition key could leave the table with too many or too few partitions.

# COMMAND ----------

df = spark.read.format("csv").option("path","/FileStore/tables/Products.csv").option("inferSchema",True).option("header",True).load()
display(df)

# COMMAND ----------

# %sql
# DROP TABLE tblEmployees_new

# COMMAND ----------

# dbutils.fs.rm("user/hive/warehouse/tblemployees_new",recurse=True)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE tblEmployees_new(
# MAGIC   OrderDate TIMESTAMP,
# MAGIC   InvoiceNum STRING,
# MAGIC   Country STRING,
# MAGIC   SalesAmount DOUBLE
# MAGIC
# MAGIC )CLUSTER BY (Country);
'''
Can be done by adding CLUSTER BY (Country);
'''
# COMMAND ----------

# MAGIC %sql
# MAGIC describe table  tblemployees_new

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail  tblemployees_new

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE tblEmployees_new3(
# MAGIC   OrderDate TIMESTAMP,
# MAGIC   InvoiceNum STRING,
# MAGIC   Country STRING,
# MAGIC   SalesAmount DOUBLE
# MAGIC
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE tblEmployees_new3

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE tblEmployees_new3
# MAGIC CLUSTER BY (Country)

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE tblEmployees_new3

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

df.select(col("OrderDate").cast("timestamp"),"InvoiceNum","Country","SalesAmount").write.mode("append").saveAsTable("tblEmployees_new")

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE tblEmployees_new

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE tblEmployees_new3
# MAGIC CLUSTER BY NONE

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE tblEmployees_newz

# COMMAND ----------

# MAGIC %md ##Benefits
# MAGIC
# MAGIC 1. Consistent file size
# MAGIC 2. Small files are merged across partitions
# MAGIC 3. Partitions divided wherever necessary
# MAGIC 4. Reduced data skew and fragmentation
# MAGIC 5. Evolution of clustering keys.
# MAGIC 6. Reduced maintainance
# MAGIC 7. Significant improvement of read and writes
# MAGIC 8. Easier management
# MAGIC 9. Clustering keys can be changed easily without easily rebuilding the entire table
# MAGIC 10. Eliminates need of partitions and can dynamically merge or divide the files to arrive at a balanced state

# COMMAND ----------

# MAGIC %md ##Limitations
# MAGIC 1. Max 4 columns can be used in clustering
# MAGIC 2. Columns with statistics collected can only be used in clustering
# MAGIC 3. Not supported for structured streaming workloads on write
#available from version 13.0


#liquid clustering is a powerful feature in Delta Lake that can help optimize query performance and simplify data management. However, it does have some limitations that users should be aware of when considering its use for their workloads. It's important to evaluate these limitations in the context of your specific use case and requirements to determine if liquid clustering is the right choice for your Delta Lake tables.

#example to do liquid clustering on a streaming table:
# MAGIC %sql
# MAGIC CREATE TABLE tblStreaming (
# MAGIC   OrderDate TIMESTAMP,
# MAGIC   InvoiceNum STRING,
# MAGIC   Country STRING,
# MAGIC   SalesAmount DOUBLE
# MAGIC ) USING DELTA
# MAGIC
# MAGIC CLUSTER BY (Country)
# MAGIC
# MAGIC OPTIONS (
# MAGIC   'delta.liquidClustering.enabled' = 'true',
# MAGIC   'delta.liquidClustering.maxClusteringColumns' = '4',
# MAGIC   'delta.liquidClustering.clusteredFileSize' = '134217728' -- 128 MB
# MAGIC );
