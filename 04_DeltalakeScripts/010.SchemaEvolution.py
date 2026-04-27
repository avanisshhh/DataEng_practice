# Databricks notebook source
dfproducts = spark.read.format("csv").option("path","/FileStore/tables/Products.csv").option("header",True).option("inferSchema",True).load()
display(dfproducts)


# COMMAND ----------

dfproducts.write.format("parquet").option("path","/FileStore/tables/ParquetSchema").save()

# COMMAND ----------

dfnew = spark.createDataFrame([(0.05,0.02),(0.05,0.01),(0.04,0.02),(0.05,0.01)],["VatPercent","DiscountPercent"])
display(dfnew)

# COMMAND ----------

dfnew.write.format("parquet").mode("append").option("path","/FileStore/tables/ParquetSchema").save()
#parquet have a drawback that it does not support schema evolution. If you try to write a new dataframe with a different schema to the same parquet location, it will throw an error. This is because parquet files have a fixed schema, and any changes to the schema require creating a new parquet file with the updated schema. 
'''
This is handled in delta format using mergescheme'''
# COMMAND ----------

df_products_parquet = spark.read.format("parquet").option("path","/FileStore/tables/ParquetSchema").load()
display(df_products_parquet)

# COMMAND ----------

(dfproducts.write.format("delta")
    .option("path","/FileStore/tables/DeltaSchema").save()
    )

# COMMAND ----------

(dfnew.write.format("delta")
    .mode("append")
    .option("mergeSchema",True)
    .option("path","/FileStore/tables/DeltaSchema").save()
    )
#mergeSchema option is used to merge the new schema with the existing schema of the delta table. If there are new columns in the new data that are not present in the existing delta table, those columns will be added to the delta table schema. This allows for schema evolution, where you can add new columns to your delta table without having to recreate it.

# COMMAND ----------

df_delta_products = spark.read.format("delta").option("path","/FileStore/tables/DeltaSchema").load()
display(df_delta_products)

# COMMAND ----------

spark.conf.get("spark.databricks.delta.schema.autoMerge.enabled")

# COMMAND ----------

#By default its False
spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled",True)

# COMMAND ----------

spark.conf.get("spark.databricks.delta.schema.autoMerge.enabled")

# COMMAND ----------

(dfnew.write.format("delta")
    .mode("overwrite")
    .option("mergeSchema",True)
    .option("path","/FileStore/tables/DeltaSchema").save()
    )

# COMMAND ----------

df_delta_ow = spark.read.format("delta").option("path","/FileStore/tables/DeltaSchema").load()
display(df_delta_ow)

# COMMAND ----------

(dfnew.write.format("delta")
    .mode("overwrite")
    .option("mergeSchema",True)
    .option("overwriteSchema", "true")
    .option("path","/FileStore/tables/DeltaSchema").save()
    )

# COMMAND ----------

df_delta_ow = spark.read.format("delta").option("path","/FileStore/tables/DeltaSchema").load()
display(df_delta_ow)

# COMMAND ----------

