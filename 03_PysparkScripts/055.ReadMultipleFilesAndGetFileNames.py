# Databricks notebook source
df =(spark.read.format("csv")
        .option("header",True)
        .option("inferschema",True)
        .option("path","/FileStore/tables/Countries")
        .load()
)
display(df)

# COMMAND ----------

from pyspark.sql.functions import input_file_name,split,regexp_replace

# COMMAND ----------

df2=df.withColumn("Filename",input_file_name())
display(df2)

# COMMAND ----------

df3=df.withColumn("Filename",input_file_name()).select("Filename").distinct()
display(df3)

# COMMAND ----------

df4=df.withColumn("Country",regexp_replace(split(input_file_name(),"/")[4],".csv",""))

'''
Here what we doing
1. getting only file name via [4]
2.splitting for it
3. removing .csv from file name using regexp_replace
'''
display(df4)
