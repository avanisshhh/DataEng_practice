# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df2=df.drop("InvoiceNum")
display(df2)

# COMMAND ----------

df2=df.drop("InvoiceNum","EnglishProductName")
display(df2)

# COMMAND ----------

