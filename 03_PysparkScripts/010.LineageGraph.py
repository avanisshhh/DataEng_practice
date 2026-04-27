# Databricks notebook source
rdd1=sc.textFile("/FileStore/tables/001_Wordcount.txt")

# COMMAND ----------

rdd1.toDebugString()
#toDebugString() function is used to see the lineage graph of the RDD and it returns a string representation of the lineage graph of the RDD

# COMMAND ----------

rdd1=sc.textFile("/FileStore/tables/001_Wordcount.txt",4)

# COMMAND ----------

rdd1.toDebugString()

# COMMAND ----------

rdd2 = rdd1.flatMap(lambda x : x.split(" "))

# COMMAND ----------

rdd2.toDebugString().splitlines()
#splitlines() function is used to split the string into a list of lines
# COMMAND ----------

rdd3 = rdd2.map(lambda y : (y,1))

# COMMAND ----------

rdd3.toDebugString().splitlines()
#splitlines() function is used to split the string into a list of lines and it returns a list of lines in the string representation of the lineage graph of the RDD

# COMMAND ----------

rdd4 = rdd3.reduceByKey(lambda x,y: x + y)

# COMMAND ----------

rdd4.toDebugString().splitlines()

# COMMAND ----------

rddd4.collect()