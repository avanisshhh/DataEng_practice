# Databricks notebook source
rdd1=sc.textFile("/FileStore/tables/001_Wordcount.txt")
rdd2 = rdd1.flatMap(lambda x : x.split(" "))
rdd3 = rdd2.map(lambda y : (y,1))
rdd4 = rdd3.reduceByKey(lambda x,y: x + y)
rdd4.collect()

# COMMAND ----------

help(rdd4.sortByKey)
#sortByKey() function is used to sort the RDD by key and it returns a new RDD sorted by key

# COMMAND ----------

help(rdd4.sortBy) #SORT BY specified function
#sortBy() function is used to sort the RDD by a specified function and it returns a new RDD sorted by the specified function

# COMMAND ----------

rdd5 =rdd4.sortByKey()
rdd5.collect()

# COMMAND ----------

rdd5 =rdd4.sortByKey(ascending=False)
rdd5.collect()

# COMMAND ----------

rdd6 = rdd4.sortBy(lambda x : x[1])
rdd6.collect()

# COMMAND ----------

rdd6 = rdd4.sortBy(lambda x : x[1],ascending=False)
rdd6.collect()

# COMMAND ----------

