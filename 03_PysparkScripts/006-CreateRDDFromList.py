# Databricks notebook source
lst = [1,2,3,4,5]
print(lst)
type(lst)
#OP: <class 'list'>
# COMMAND ----------

sparkcon = spark.sparkContext
type(sparkcon)
#OP: <class 'pyspark.context.SparkContext'>

# COMMAND ----------

help(sparkcon.parallelize)
#parallelize() is used to create RDD from list, collection or any python object
# COMMAND ----------

rdd1 = sparkcon.parallelize(lst)
#
# COMMAND ----------

type(rdd1)
#OP: <class 'pyspark.rdd.RDD'>
# COMMAND ----------

rdd1.collect()
#collect() is used to get all the data from RDD to driver program as list

# COMMAND ----------

rdd2=sc.parallelize(lst)
rdd2.collect()

# COMMAND ----------

rdd2.getNumPartitions()
#By default no of partition is 2 in local mode and 200 in cluster mode
'''
parallelize()	sc defaultParallelism (CPU cores)
textFile()	Based on file blocks
DataFrame → RDD	Usually 200 (shuffle partitions)
'''


# COMMAND ----------

rdd2.glom().collect()
#To know how data is distributed in partition we use glom() function

# COMMAND ----------

