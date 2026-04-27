# Databricks notebook source
rdd1=sc.textFile("/FileStore/tables/001_Wordcount.txt")
rdd2 = rdd1.flatMap(lambda x : x.split(" "))
rdd3 = rdd2.map(lambda y : (y,1))
rdd4 = rdd3.reduceByKey(lambda x,y: x + y)
rdd4.collect()

# COMMAND ----------

help(rdd4.first)
#first() function is used to return the first element of the RDD and it returns a tuple of (key, value) pairs where the key is the word and the value is the count of that word

# COMMAND ----------

rdd4.first()

# COMMAND ----------

type(rdd4.first())

# COMMAND ----------

rdd4.take(2)
#take() function is used to return the first n elements of the RDD and it returns a list of tuples of (key, value) pairs where the key is the word and the value is the count of that word

# COMMAND ----------

type(rdd4.take(2))

# COMMAND ----------

rdd4.sortBy(lambda x:x[1],ascending=False).take(2)

# COMMAND ----------

rdd4.sortBy(lambda x:x[1]).take(3)

# COMMAND ----------

rdd4.keys().collect()
#keys() function is used to return an RDD of the keys of the RDD and it returns an RDD of the words in this case

# COMMAND ----------

rdd4.values().collect()
#values() function is used to return an RDD of the values of the RDD and it returns an RDD of the counts of the words in this case

# COMMAND ----------

