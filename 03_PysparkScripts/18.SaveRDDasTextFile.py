# Databricks notebook source
rdd1=sc.textFile("/FileStore/tables/001_Wordcount.txt")
rdd2 = rdd1.flatMap(lambda x : x.split(" "))
rdd3 = rdd2.map(lambda y : (y,1))
rdd4 = rdd3.reduceByKey(lambda x,y: x + y)
rdd4.collect()

# COMMAND ----------

rdd4.saveAsTextFile("/FileStore/tables/RDDOutput")
#saveAsTextFile() function is used to save the RDD as a text file and it takes the path of the file as an argument and it saves the RDD as a text file in the specified path
# COMMAND ----------

rdd4.getNumPartitions()

# COMMAND ----------
'''
Twist OP will be stored in two partitions because the default number of partitions is 2 and the data will be distributed in two partitions and when we save the RDD as a text file, it will create two part files in the specified path and each part file will contain the data of one partition'''
rdd11=sc.textFile("/FileStore/tables/RDDOutput/part-00000")
rdd11.collect()

# COMMAND ----------

rdd11=sc.textFile("/FileStore/tables/RDDOutput/part-00001")
rdd11.collect()

# COMMAND ----------

