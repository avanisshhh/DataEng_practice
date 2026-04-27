# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df.count()
#Not used in production just for dev purpose
# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.columns
#Display the column names of the DataFrame and it returns a list of column name 
# COMMAND ----------

len(df.columns)

# COMMAND ----------


