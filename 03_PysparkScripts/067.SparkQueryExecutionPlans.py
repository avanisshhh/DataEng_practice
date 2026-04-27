# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferSchema",True)
.load())
display(df)

# COMMAND ----------

df.explain()
#explain() method is used to print the physical plan of the query. it shows the steps that spark will take to execute the query. it is useful for debugging and optimizing the query. it shows the operations that will be performed on the data, such as filter, join, aggregate, etc. it also shows the order of the operations and the data flow between them.

# COMMAND ----------

df.explain(extended=True)
#explain(extended=True) method is used to print the physical plan of the query in a more detailed way. it shows the steps that spark will take to execute the query, along with the cost of each step. it is useful for debugging and optimizing the query. it shows the operations that will be performed on the data, such as filter, join, aggregate, etc. it also shows the order of the operations and the data flow between them. it also shows the cost of each operation, which can help in identifying the bottlenecks in the query.

# COMMAND ----------


