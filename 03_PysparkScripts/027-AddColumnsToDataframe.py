# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

from pyspark.sql.functions import col,round,lit


# COMMAND ----------
#WithColumn is used to add a new column or replace an existing column in dataframe here we are adding a new column vat which is 5% of SalesAmount and rounded to 2 decimal places
df2 = df.withColumn("Vat",round(col("SalesAmount") * 0.05,2))
display(df2)

# COMMAND ----------
#lit is used to add a constant value in a new column here we are adding a new column CountryOfOrigin with constant value USA
df3 = df2.withColumn("CountryOfOrigin",lit("USA"))
display(df3)

# COMMAND ----------

df4=df3.withColumn("TotalProductCost",round(col("TotalProductCost"),2))
display(df4)

# COMMAND ----------

len(df4.columns)

# COMMAND ----------

dfnew = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.load())
display(dfnew)

# COMMAND ----------

df6 = dfnew.withColumn("ProductKey",col("ProductKey").cast("int"))
display(df6)

# COMMAND ----------

df4=df3.withColumn("TotalProductCost",round(col("TotalProductCost"),2)).withColumn("SalesAmount",round(col("SalesAmount"),2))
display(df4)

# COMMAND ----------

help(df.withColumns)
#withColumns is used to add multiple columns in a single statement here we are adding two columns Vat and Country in a single statement


# COMMAND ----------

df7=df.withColumns({'Vat':round(col("SalesAmount")*0.05,2),'Country':lit("USA")})
display(df7)

# COMMAND ----------


