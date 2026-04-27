# Databricks notebook source
display(dbutils.fs.ls("/FileStore/tables/"))
'''Lists files and directories
Returns metadata, not data
'''

# COMMAND ----------

display(spark.read.text("dbfs:/FileStore/tables/001_Wordcount.txt"))
'''Reads the file content
Returns a DataFrame
Each line of the file becomes a row in a DataFrame with a column named value.

KeyPoints:
Uses Spark SQL / DataFrame API
Schema-based (structured)
Optimized using Catalyst Optimizer
Can use SQL:

whereas sc.textFile() returns an RDD of strings, each string is a line from the file, and it is unstructured data. It does not have a schema and is not optimized by Spark's Catalyst Optimizer. It is a lower-level API that provides more control but requires more manual handling of data transformations and actions.
Returns an RDD
Each line = string
'''
#display() function is used to display the contents of the specified path and it takes the path as an argument and it displays the contents of the specified path and here we can see that there is a file named 001_Wordcount.txt in the specified path 

# COMMAND ----------

wc = sc.accumulator(0)
wc.value

# COMMAND ----------

rdd = sc.textFile("dbfs:/FileStore/tables/001_Wordcount.txt")
#RDD of strings: Each element is a line from the file
# COMMAND ----------

rdd.collect()

# COMMAND ----------

def SplitAndCount(x):
    arr=x.split(" ")
    wc.add(len(arr))

# COMMAND ----------
# FOREACH - Action: Executes immediately and updates accumulator
rdd.foreach(SplitAndCount)  
wc.value  # ✓ wc has been updated (accumulator holds the word count)

# COMMAND ----------
# MAP - Transformation: Creates new RDD, doesn't execute until an action is called
rdd1=rdd.map(SplitAndCount)  
# Only creates plan, doesn't run the function
rdd1.count()  
# ✓ Now the action triggers execution

