# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df.explain()

# COMMAND ----------

df.explain(True)

# COMMAND ----------

df2 = df.filter("country='India'")
display(df2)

# COMMAND ----------

df2.explain(True)

# COMMAND ----------

from pyspark.sql.functions import * 

# COMMAND ----------

df3 = df.withColumn("CountryOfOrigin",lit("India"))
display(df3)

# COMMAND ----------

df3.explain(True)

# COMMAND ----------

df4 = df.withColumn("CountryOfOrigin",lit("India")).filter("Country='France'")
display(df4)

# COMMAND ----------

df4.explain(True)

# COMMAND ----------

df4.rdd.toDebugString().splitlines()
#toDebugString() method is used to get the execution plan of the dataframe in a human readable format. it returns a string representation of the execution plan which can be used for debugging and performance tuning. splitlines() method is used to split the string into a list of lines for better readability. --- IGNORE ---

# COMMAND ----------

df5=df.select(sum("SalesAmount")).alias("TotalSales")
display(df5)

# COMMAND ----------

df5.explain(True)

# COMMAND ----------

df6 = df.groupBy("Country").sum("SalesAmount")
display(df6)

# COMMAND ----------

df6.explain(True)

# COMMAND ----------

spark.conf.get("spark.sql.shuffle.partitions")

# COMMAND ----------

spark.conf.set("spark.sql.shuffle.partitions",50)
#Shuffle partitions are the number of partitions that will be used when shuffling data for joins or aggregations. By default, Spark uses 200 shuffle partitions, but you can adjust this setting based on the size of your data and the resources available in your cluster. Setting it too low may lead to large partitions and potential out-of-memory errors, while setting it too high may lead to excessive overhead from managing many small tasks.

# COMMAND ----------

spark.conf.get("spark.sql.shuffle.partitions")

# COMMAND ----------

df6 = df.groupBy("Country").sum("SalesAmount")
display(df6)

# COMMAND ----------

df6.explain(True)

# COMMAND ----------

countryDisdf = df.select("Country").distinct()
display(countryDisdf)
countryDisdf.explain(True)

# COMMAND ----------

df7 = spark.range(1000000)
display(df7)
df7.explain(True)

# COMMAND ----------

df8 = spark.range(1000000)
df9 = df8.selectExpr("id * 10 as id")
df9.explain(True)

# COMMAND ----------

df10=df8.repartition(6)
df10.explain(True)

# COMMAND ----------

x=100

# COMMAND ----------


