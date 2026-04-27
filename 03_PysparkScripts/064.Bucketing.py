# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df.write.format("csv").option("path","/FileStore/tables/Buckets").bucketBy(5,"ProductKey").saveAsTable("PurchaseBkt")

# COMMAND ----------

df.write.format("csv").option("path","/FileStore/tables/Buckets2").partitionBy("Country").bucketBy(5,"ProductKey").saveAsTable("PurchaseBkt2")
'''
👉 Creates 5 buckets based on ProductKey hash
👉 Bucketing does NOT work with normal .save()
Data split into 5 files per partition
Same ProductKey values go to same bucket

'''
# COMMAND ----------

df2 = (spark.read.format("csv")
.option("path","/FileStore/tables/Buckets2/Country=Italy/part-00000-tid-3483949231015354760-af0985f4-1d3b-4022-966c-c52b41a771e3-401-26_00000.c000.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df2)

# COMMAND ----------

/dbfs/FileStore/tables/Buckets2/Country=Italy/part-00000-tid-3483949231015354760-af0985f4-1d3b-4022-966c-c52b41a771e3-401-26_00000.c000.csv