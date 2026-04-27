# Databricks notebook source
rdd1=sc.textFile("/FileStore/tables/001_Wordcount.txt")
rdd2 = rdd1.flatMap(lambda x : x.split(" "))
rdd3 = rdd2.map(lambda y : (y,1))
rdd4 = rdd3.reduceByKey(lambda x,y: x + y)
rdd4.collect()

# COMMAND ----------

help(rdd4.filter)
#


# COMMAND ----------

rdd5=rdd4.filter(lambda x: x[0].startswith("h"))
rdd5.collect()

# COMMAND ----------

rdd5=rdd4.filter(lambda x: x[1]>30)
rdd5.collect()

# COMMAND ----------

