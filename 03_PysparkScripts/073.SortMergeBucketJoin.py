# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

df = spark.range(10000000).withColumn("id2",expr("id *2"))
display(df)

# COMMAND ----------

df2 =df
display(df2)

# COMMAND ----------

joindf = df.join(df2,df.id==df2.id)
display(joindf)

# COMMAND ----------

joindf.explain(True)

# COMMAND ----------

df.write.format("parquet").mode("overwrite").bucketBy(10,"id").saveAsTable("Bucketids")
#In bucketing we have to use that column which is bucketed for query optimization 
# COMMAND ----------

bucketdf = spark.table("Bucketids")
#when we create a bucketed table using the bucketBy method, it creates a new table with the specified number of buckets and the specified column as the bucket key. in this case we are creating a bucketed table with 10 buckets and id column as the bucket key. when we query the bucketed table it will read the data from the bucketed files and it will use the bucket key to filter the data and it will return only the relevant data based on the bucket key. this can improve the performance of the query as it reduces the amount of data that needs to be read from disk.

# COMMAND ----------

joindf2=df.join(bucketdf,df.id==bucketdf.id)
display(joindf2)

# COMMAND ----------

joindf2.explain(True)

# COMMAND ----------

bucketdf2 = spark.table("Bucketids")

# COMMAND ----------

joindf3=bucketdf.join(bucketdf2,bucketdf.id==bucketdf2.id)
display(joindf3)

# COMMAND ----------

joindf3.explain(True)
#explain() method is used to get the execution plan of the dataframe  
# COMMAND ----------

joindf4=bucketdf.join(bucketdf2,bucketdf.id2==bucketdf2.id2)
display(joindf4)

# COMMAND ----------

joindf4.explain(True)

# COMMAND ----------

x=100

# COMMAND ----------

#Important is BroadcastHashJoin and SortMergeBucketJoin
#1. BroadcastHashJoin: This strategy is used when one of the tables in the join is small enough to fit in memory. The smaller table is broadcasted to all the worker nodes, and the join is performed locally on each node. This can significantly improve the performance of the join operation      
#SortMergeBucketJoin: This strategy is used when both tables in the join are bucketed and sorted on the join keys. In this strategy, the data from both tables is read in a sorted manner based on the bucket keys, and the join is performed by merging the sorted data. This can be more efficient than shuffle hash join for certain types of joins, such as range joins or inequality joins, but it can be less efficient for other types of joins, such as equi-joins. when we have bucketed tables and we are joining them on the bucket keys then spark will use sort merge bucket join strategy to perform the join operation which can improve the performance of the join operation as it avoids shuffling data across the network and it can also take advantage of the sorted nature of the data to perform the join operation more efficiently.

