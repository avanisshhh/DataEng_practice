# Databricks notebook source
rdd1=sc.textFile("/FileStore/tables/001_Wordcount.txt")
rdd2 = rdd1.flatMap(lambda x : x.split(" "))
rdd3 = rdd2.map(lambda y : (y,1))
rdd4 = rdd3.reduceByKey(lambda x,y: x + y)
rdd4.collect()


help(rdd3.groupByKey)
'''
("hello", [1,1])
("world", [1])
("spark", [1])
'''
#groupByKey() function is used to group the data based on key and it returns an RDD of (key, iterable) pairs where the iterable contains all the values for that key


help(rdd3.groupByKey().mapValues)
#mapValues() function is used to apply a function to the values of the RDD and it returns an RDD of (key, value) pairs where the value is the result of applying the function to the values of the RDD
rdd5=rdd3.groupByKey().map(lambda x : (x[0],sum(x[1])))

rdd5.collect()

rdd5=rdd3.groupByKey().mapValues(sum)
'''
mapValues() only works on values
Automatically keeps key same
Cleaner version of above
("hello",2), ("world",1), ("spark",1)

'''
#Here we have used mapValues() function to apply sum() function to the values of the RDD and it returns an RDD of (key, value) pairs where the value is the sum of the values for that key
rdd5.collect()

rdd5=rdd3.groupByKey().mapValues(list)
'''
Converts iterable into list
("hello", [1,1])
("world", [1])
("spark", [1])
'''
#Here we have used mapValues() function to apply list() function to the values of the RDD and it returns an RDD of (key, value) pairs where the value is a list of the values for that key
rdd5.collect()

# COMMAND ----------

