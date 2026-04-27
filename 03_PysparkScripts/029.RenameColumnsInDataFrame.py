# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df2=df.withColumnRenamed("ProductKey","ProductId")
display(df2)

# COMMAND ----------

df2=df.withColumnRenamed("ProductKey","ProductId").withColumnRenamed("InvoiceNum","InvoiceId")
display(df2)

# COMMAND ----------

df3=df.selectExpr("*","ProductKey as ProductId").drop("ProductKey")
display(df3)

'''
withColumnRenamed
👉 Pure rename operation
👉 No new column created
selectExpr
👉 Creates a new column (ProductId)
👉 Then removes old column
'''

# COMMAND ----------

