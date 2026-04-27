# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df2=df.groupBy("EnglishProductName").pivot("Country").sum("SalesAmount")
display(df2)

# COMMAND ----------

df3=df.groupBy("ProductKey","EnglishProductName").pivot("Country").sum("SalesAmount")
#
display(df3)

# COMMAND ----------

help(df2.unpivot)
#unpivot is used to convert columns into rows here we are unpivoting the country columns into rows and getting the sales amount for each country in a new column Salesamount


# COMMAND ----------

df4=df2.unpivot("EnglishProductName",["Australia"],"Country","Salesamount")
display(df4)

# COMMAND ----------

df4=df2.unpivot("EnglishProductName",["Australia","France","Canada"],"Country","Salesamount")
display(df4)

# COMMAND ----------

df5=df3.unpivot(["ProductKey","EnglishProductName"],["Australia","France","Canada"],"Country","Salesamount")
display(df5)

# COMMAND ----------

df5=df3.unpivot(["ProductKey","EnglishProductName"],["Australia","France","Canada"],"Country","Salesamount").dropna()
#dropna is used to drop the rows with null values here we are dropping the rows with null values in the unpivoted dataframe
display(df5)

# COMMAND ----------

