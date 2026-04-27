# Databricks notebook source
help(sc.textFile)
#To create RDD from text file we use textFile() function of spark context and we need to provide the path of the file as argument to this function

rdd1 = sc.textFile("/FileStore/tables/001_Wordcount.txt")
#Here we have created RDD from text file and we have provided the path of the file as argument to textFile() function

# COMMAND ----------

rdd1.collect()
#To see the data in RDD we use collect() function and here we can see that data is in list format and each line of the file is an element of the list

# COMMAND ----------

rdd1.getNumPartitions()

# COMMAND ----------

rdd2 = sc.textFile("/FileStore/tables/001_Wordcount.txt",4)
rdd2.getNumPartitions()

# COMMAND ----------

rdd2.glom().collect()

# COMMAND ----------

