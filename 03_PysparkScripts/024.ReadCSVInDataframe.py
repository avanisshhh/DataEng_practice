# Databricks notebook source
help(spark.read.csv)


# COMMAND ----------

df = spark.read.csv("/FileStore/tables/Products.csv")


# COMMAND ----------

display(df)

# COMMAND ----------

df.display()

# COMMAND ----------

df.show()

# COMMAND ----------

df.show(5)

# COMMAND ----------

df2 = spark.read.csv("/FileStore/tables/Products.csv",header=True)
#show headers of file
display(df2)


# COMMAND ----------

df3 = spark.read.csv("/FileStore/tables/Products.csv",header=True,inferSchema=True)
#
display(df3)



# COMMAND ----------

help(spark.read.format)



# COMMAND ----------

df3 = spark.read.format("csv").option("path","/FileStore/tables/Products.csv").option("header",True).option("inferSchema",True).load()


display(df3)


# COMMAND ----------

df3 = spark.read.format("csv") \
.option("path","/FileStore/tables/Products.csv") \
.option("header",True).option("inferSchema",True) \
.load()
display(df3)


# COMMAND ----------

df3 = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True).option("inferSchema",True)
.load())
display(df3)


# COMMAND ----------


