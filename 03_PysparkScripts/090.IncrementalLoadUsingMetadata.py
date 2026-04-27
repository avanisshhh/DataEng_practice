# Databricks notebook source
# MAGIC %run /Workspace/Users/avanish@datatailor.com/JDBC/Utilities

# COMMAND ----------

spark.conf.set("storage-account-key")


# COMMAND ----------

ADLS_Path = "abfss://mycontainer@mydatatraining.dfs.core.windows.net/IncrementalLoad/Sales/"

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE Incremental_Load_Mappings

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE Incremental_Load_Mappings(
# MAGIC   TableName string,
# MAGIC   FileModifiedDateTime TIMESTAMP
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO Incremental_Load_Mappings(TableName, FileModifiedDateTime)
# MAGIC VALUES
# MAGIC ('dbo.Sales', '2018-01-01');
# MAGIC
# MAGIC SELECT * FROM Incremental_Load_Mappings;

# COMMAND ----------

df = (spark.read.format("csv")
      .option("header", "true")
      .option("inferSchema", "true")
      .load(ADLS_Path)
      .select("_metadata").distinct()
)
display(df)
'''
_metadata is a hidden column in Databricks
It contains:
file_path
file_modification_time

'''


# COMMAND ----------

meta_df = df.select("_metadata.file_path","_metadata.file_modification_time")
display(meta_df)

#| file_path | file_modification_time |

# COMMAND ----------

latest_watermark = spark.sql("select  FileModifiedDateTime from incremental_load_mappings where TableName='dbo.Sales'")
lastmodifiedtime = latest_watermark.select("FileModifiedDateTime").collect()[0].FileModifiedDateTime 
print(lastmodifiedtime)


# COMMAND ----------

New_WaterMark_Value = meta_df.select("file_modification_time").collect()[-1][0]
print(New_WaterMark_Value)

'''
What this does:

Collects all file timestamps
Takes the last one

⚠️ Issue here:

This assumes data is sorted, which is risky

👉 Better approach:

from pyspark.sql.functions import max

New_WaterMark_Value = meta_df.agg(max("file_modification_time")).collect()[0][0]
'''

# COMMAND ----------

if New_WaterMark_Value == lastmodifiedtime:
    dbutils.notebook.exit("No data")

# COMMAND ----------

sales_df = (spark.read.format("csv")
      .option("header", "true")
      .option("inferSchema", "true")
      .option("modifiedAfter",lastmodifiedtime)
      .load(ADLS_Path)
)
#modifiedAfter ensures:
#Only new/updated files are read

display(sales_df)

# COMMAND ----------

WriteDataframeToDatabaseMode(sales_df,"dbo.Sales","append")

# COMMAND ----------

query = f"""
UPDATE incremental_load_mappings 
SET FileModifiedDateTime = CAST('{New_WaterMark_Value}' AS timestamp)
WHERE TableName = 'dbo.Sales'
"""

spark.sql(query)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from Incremental_Load_Mappings

# COMMAND ----------

