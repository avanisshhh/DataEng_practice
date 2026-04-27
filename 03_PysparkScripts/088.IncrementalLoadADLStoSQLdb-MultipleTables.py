# Databricks notebook source
# MAGIC %sql
# MAGIC DROP TABLE Incremental_Load_Mappings_Multi

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE Incremental_Load_Mappings_Multi(
# MAGIC   TableName STRING,
# MAGIC   ADLS_Path STRING,
# MAGIC   WaterMarkColumn STRING,
# MAGIC   WateMarkValue TIMESTAMP,
# MAGIC   IsActive INT
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO Incremental_Load_Mappings_Multi(TableName,ADLS_Path, WaterMarkColumn, WateMarkValue,IsActive)
# MAGIC VALUES
# MAGIC ('dbo.Sales', 'IncrementalLoad/Sales/','SalesDate', '2015-01-01',1),
# MAGIC ('dbo.Orders', 'IncrementalLoad/Orders/','OrderDate', '2015-01-01',1),
# MAGIC ('dbo.Purchase', 'IncrementalLoad/Purchase/','PurchaseDate' ,'2015-01-01',1);
# MAGIC
# MAGIC SELECT * FROM Incremental_Load_Mappings_Multi;

# COMMAND ----------

# MAGIC %run /Workspace/Users/avanish@datatailor.com/JDBC/Utilities

# COMMAND ----------

spark.conf.set("storage-account-key")


# COMMAND ----------

Base_Path = "abfss://mycontainer@mydatatraining.dfs.core.windows.net/"

# COMMAND ----------

table_metadf = spark.sql("select * from incremental_load_mappings_multi where IsActive=1")
display(table_metadf)

# COMMAND ----------

from pyspark.sql.functions import col,lit
from datetime import datetime


rows = table_metadf.collect()

for tablerow in rows:
    TableName = tablerow["TableName"]
    ADLS_Path = tablerow["ADLS_Path"]
    WaterMarkColumn = tablerow["WaterMarkColumn"]
    WaterMarkValue = tablerow["WateMarkValue"]
    print( WaterMarkValue)
    print(f"Loading incremental data for table: {TableName}")

    # Read new data from ADLS
    df = (spark.read.format("csv")
          .option("inferschema","true")
          .option("header","true")
          .option("path",Base_Path + ADLS_Path)
          .load()).withColumn(WaterMarkColumn, col(WaterMarkColumn).cast("timestamp")).filter(col(WaterMarkColumn) > lit(WaterMarkValue))
          
    print(df.count())
    if df.count() > 0:
        # Write to SQL
        WriteDataframeToDatabaseMode(df,TableName,"append")

        # Update watermark (get max value from current data)
        new_watermark = df.agg({WaterMarkColumn: "max"}).collect()[0][0]
        

        # Here you would persist the new watermark to a config file or table
        query = f"""
                UPDATE incremental_load_mappings_multi 
                SET WateMarkValue = CAST('{new_watermark}' AS timestamp)
                WHERE TableName = '{TableName}'
                """
        spark.sql(query)

        print(f"Updated watermark for {TableName}: {new_watermark}")
    else:
        print(f"No new data found for table: {TableName}")


# COMMAND ----------

# MAGIC %sql
# MAGIC select * from incremental_load_mappings_multi

# COMMAND ----------


#link https://chatgpt.com/g/g-p-69a52d2d17f081918cc2e426c7dfa117-data-engineering/c/69d61022-c7fc-8322-bfaa-7f3716718731
