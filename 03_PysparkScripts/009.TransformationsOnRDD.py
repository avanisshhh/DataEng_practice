# Databricks notebook source
rdd1=sc.textFile("/FileStore/tables/001_Wordcount.txt")


# COMMAND ----------

rdd1.collect()

# COMMAND ----------

help(rdd1.flatMap)

# COMMAND ----------

rdd2 = rdd1.flatMap(lambda x : x.split(" "))
'''
Takes each element of rdd1 (usually a string/sentence)
Splits it into words using " "
Flattens the result into a single RDD
['hello', 'world', 'spark', 'is', 'fast']
'''
rdd2.collect()

# COMMAND ----------

rdd3 = rdd2.map(lambda y : (y,1))
'''A tuple is an ordered, immutable collection

'''
#Here we have used map() function to create a new RDD where each element is a tuple of (word, 1) and we have used lambda function to split the lines into words and assign the value 1 to each word
rdd3.collect()

# COMMAND ----------

rdd4 = rdd3.reduceByKey(lambda x,y: x + y)
#Here we have used reduceByKey() function to create a new RDD where each element is a tuple of (word, count) and we have used lambda function to sum the values for each key

rdd4.collect()

# COMMAND ----------

