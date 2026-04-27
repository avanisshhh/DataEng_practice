# Databricks notebook source
rdd1=sc.textFile("/FileStore/tables/001_Wordcount.txt")

rdd2 = rdd1.flatMap(lambda x : x.split(" "))

rdd3 = rdd2.map(lambda y : (y,1))

rdd4 = rdd3.reduceByKey(lambda x,y: x + y)

rdd4.collect()

# COMMAND ----------

help(rdd3.reduceByKey)
#reduceByKey() function is used to reduce the values for each key using the specified binary function and it returns a new RDD of (key, value) pairs where the value is the result of reducing the values for that key

# COMMAND ----------

help(rdd3.reduceByKeyLocally)
#reduceByKeyLocally() function is used to reduce the values for each key using the specified binary function and it returns a dictionary of (key, value) pairs where the value is the result of reducing the values for that key

'''Output = Python dictionary
Data comes to driver (local machine)
Risk of memory issue if data is large
Good for small datasets only
rdd = sc.parallelize([("a",1), ("b",2), ("a",3)])
rdd.reduceByKeyLocally(lambda a,b: a+b)
{'a': 4, 'b': 2}
'''

# COMMAND ----------

#reduceByKeyLocally for small datasets and reduceByKey for large datasets because reduceByKeyLocally collects the data to the driver node and it can cause memory issues if the dataset is large
dct = rdd3.reduceByKeyLocally(lambda x,y : x + y)
type(dct)
print(dct)

# COMMAND ----------

