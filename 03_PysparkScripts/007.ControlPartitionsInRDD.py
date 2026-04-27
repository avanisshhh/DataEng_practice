# Databricks notebook source
lst = [1,2,3,4,5]
rdd1 = sc.parallelize(lst)
rdd1.collect()

# COMMAND ----------

rdd1.getNumPartitions()
#Default number of partitions is 2 in local mode and 200 in cluster mode

# COMMAND ----------

rdd2=sc.parallelize(lst,5)
#Here we can see that data is distributed in 5 partitions and each partition has 1 record each
rdd2.collect()


# COMMAND ----------

rdd2.getNumPartitions()

# COMMAND ----------

rdd2.glom().collect()

# COMMAND ----------

rdd3 = sc.parallelize(lst,3)
rdd3.glom().collect()
#Here we can see that data is distributed in 3 partitions and 1st partition has 2 records and 2nd and 3rd partition has 1 record each



