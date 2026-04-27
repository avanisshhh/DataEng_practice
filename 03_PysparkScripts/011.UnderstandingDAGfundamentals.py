# Databricks notebook source
rdd1=sc.textFile("/FileStore/tables/001_Wordcount.txt")

# COMMAND ----------

rdd1.collect()

# COMMAND ----------

rdd2 = rdd1.flatMap(lambda x : x.split(" "))

# COMMAND ----------

rdd2.collect()

# COMMAND ----------

rdd3 = rdd2.map(lambda y : (y,1))

# COMMAND ----------

rdd3.collect()

# COMMAND ----------

rdd4 = rdd3.reduceByKey(lambda x,y: x + y)

# COMMAND ----------

rdd4.collect()

# COMMAND ----------

