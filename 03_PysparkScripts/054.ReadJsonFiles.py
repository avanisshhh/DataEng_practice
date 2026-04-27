# Databricks notebook source
df=(spark.read.format("json")
    .option("path","/FileStore/tables/Products.json")
    .option("multiline",True)
    .load())
display(df)
#give error because by default spark reads json files in single line mode. if the json file is in multiple lines, we have to set the multiline option to true.
# COMMAND ----------

display(spark.read.text("/FileStore/tables/Products.json"))

# COMMAND ----------

display(spark.read.text("/FileStore/tables/ProductsNested.json"))

# COMMAND ----------

df=(spark.read.format("json")
    .option("path","/FileStore/tables/ProductsNested.json")
    .option("multiline",True)
    .load())
display(df)

# COMMAND ----------

df2=df.select("ProductKey","Detail.ProductName","Detail.Price","Detail.SalesAmount")
'''2 step hirarchy: using "." notation '''
#we are selecting the ProductKey column and the nested columns ProductName, Price and SalesAmount from the Detail column in the ProductsNested.json file and displaying the result.
display(df2)

# COMMAND ----------


