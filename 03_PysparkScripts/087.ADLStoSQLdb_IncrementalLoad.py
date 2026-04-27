# Databricks notebook source
# MAGIC %sql
# MAGIC DROP TABLE Incremental_Load_Mappings

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE Incremental_Load_Mappings(
# MAGIC   TableName string,
# MAGIC   WaterMarkColumn string,
# MAGIC   WateMarkValue DATE
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO Incremental_Load_Mappings(TableName, WaterMarkColumn, WateMarkValue)
# MAGIC VALUES
# MAGIC ('dbo.Sales', 'SalesDate', '2015-01-01');
# MAGIC
# MAGIC SELECT * FROM Incremental_Load_Mappings;

# COMMAND ----------

maxDate = spark.table("Incremental_Load_Mappings").select("WateMarkValue").where("TableName = 'dbo.Sales'").collect()
maxDate[0]['WateMarkValue']
'''
👉 Get first row from list Row(WateMarkValue=2023-01-05)
👉 Extract value from that row 2023-01-05

 maxDate[0]['WateMarkValue']  →  2023-01-05
'''
# COMMAND ----------

# MAGIC %run /Workspace/Users/avanish@datatailor.com/JDBC/Utilities

# COMMAND ----------

spark.conf.set("storage-account-key")
#here we are setting the storage account key in spark configuration to access the data from ADLS Gen2

# COMMAND ----------

df = (spark.read.format("csv")
      .option("header", "true")
      .option("inferSchema", "true")
      .load("abfss://mycontainer@mydatatraining.dfs.core.windows.net/IncrementalLoad/Sales/Sales1.csv")
)
display(df)

#collect ----Converts DataFrame → Python list

# COMMAND ----------

delta_load = df.filter(df.SalesDate > maxDate[0]['WateMarkValue'])
display(delta_load)

# COMMAND ----------

WriteDataframeToDatabaseMode(delta_load, "dbo.Sales", "append")


# COMMAND ----------

import pyspark.sql.functions as F

# COMMAND ----------

New_WaterMark_Value = delta_load.withColumn(
    "SalesDate", F.col("SalesDate").cast("date")
).agg(F.max("SalesDate")).collect()[0][0]
print(New_WaterMark_Value)
'''
First [0] → row
Second [0] → column inside that row
'''

# COMMAND ----------

query = f"""
UPDATE incremental_load_mappings 
SET WateMarkValue = CAST('{New_WaterMark_Value}' AS DATE)
WHERE TableName = 'dbo.Sales'
"""
'''
"""---It allows you to inject variables into SQL 
'''

spark.sql(query)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM incremental_load_mappings

# COMMAND ----------

#link for understanding https://chatgpt.com/g/g-p-69a52d2d17f081918cc2e426c7dfa117-data-engineering/c/69d60b89-61b8-83a2-85e4-a3babaaddd1f