# Databricks notebook source
spark.conf.set(
    "access-key")


# COMMAND ----------

df = (spark.read.format("csv")
.option("path","abfss://mycontainer@cdudevmyadls.dfs.core.windows.net/CSVfiles/tripdata/tripdataNew.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

display(dbutils.fs.ls("/FileStore/tables/PaymentTypes.csv"))

# COMMAND ----------

ptypedf = (spark.read.format("csv")
.option("path","/FileStore/tables/PaymentTypes.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(ptypedf)

# COMMAND ----------

joindf = df.join(ptypedf,df.payment_type == ptypedf.PaymentTypeID)
display(joindf)

# COMMAND ----------

spark.conf.get("spark.sql.autoBroadcastJoinThreshold")

# COMMAND ----------

10485760/1024/1024

# COMMAND ----------

joindf.explain(True)

# COMMAND ----------

spark.conf.get("spark.sql.broadcastTimeout")

# COMMAND ----------
#BroadcastJoinStrategy is a join strategy in Spark that is used when one of the tables in the join is small enough to fit in memory. In this strategy, the smaller table is broadcasted to all the worker nodes, and the join is performed locally on each node. This can significantly improve the performance of the join operation, as it avoids the need for shuffling data across the network. The threshold for determining whether a table is small enough to be broadcasted can be configured using the spark.sql.autoBroadcastJoinThreshold setting.

from pyspark.sql.functions import broadcast

# COMMAND ----------

joindf = df.join(broadcast(ptypedf),df.payment_type == ptypedf.PaymentTypeID)
display(joindf)

# COMMAND ----------

spark.conf.set("spark.sql.autoBroadcastJoinThreshold",20*1024*1024)

# COMMAND ----------

spark.conf.get("spark.sql.autoBroadcastJoinThreshold")

# COMMAND ----------

spark.conf.set("spark.sql.autoBroadcastJoinThreshold",-1)
#disable
#-1 value for spark.sql.autoBroadcastJoinThreshold means that there is no size limit for broadcasting a table, and all tables will be considered for broadcasting regardless of their size. This can lead to performance issues if large tables are broadcasted, as it can consume a lot of memory and network bandwidth. It is generally recommended to set a reasonable threshold for broadcasting tables to avoid such issues.

# COMMAND ----------

spark.conf.get("spark.sql.autoBroadcastJoinThreshold")

# COMMAND ----------

spark.conf.set("spark.sql.autoBroadcastJoinThreshold",40)
#setting the spark.sql.autoBroadcastJoinThreshold to a very low value like 40 bytes will effectively disable the broadcast join strategy, as it is unlikely that any table will be small enough to be broadcasted. This means that Spark will use other join strategies, such as shuffle hash join or sort merge join, which may not perform as well as broadcast join for small tables. It is generally recommended to set a reasonable threshold for broadcasting tables to avoid performance issues.

# COMMAND ----------

spark.conf.get("spark.sql.autoBroadcastJoinThreshold")

# COMMAND ----------

spark.conf.get("spark.sql.join.preferSortMergeJoin")
#spark.sql.join.preferSortMergeJoin is a configuration setting in Spark that determines whether Spark should prefer using sort-merge join over other join strategies, such as broadcast join or shuffle hash join. When this setting is set to true, Spark will prefer using sort-merge join for joining large datasets, as it can be more efficient for certain types of joins. However, when this setting is set to false, Spark will not prefer sort-merge join and may choose other join strategies based on the size of the datasets and the available resources. It is generally recommended to set this setting to true for better performance when joining large datasets.
# COMMAND ----------

joindf2 = df.join(ptypedf,df.payment_type == ptypedf.PaymentTypeID)
display(joindf2)

# COMMAND ----------

joindf2.explain(True)

# COMMAND ----------

spark.conf.set("spark.sql.join.preferSortMergeJoin",False)

# COMMAND ----------

spark.conf.get("spark.sql.join.preferSortMergeJoin")

# COMMAND ----------

joindf3 = df.join(ptypedf,df.payment_type == ptypedf.PaymentTypeID)
display(joindf3)

# COMMAND ----------

joindf3.explain(True)

# COMMAND ----------


#Types of join strategies in Spark are:
#1. Broadcast Hash Join: This strategy is a variation of the broadcast join, where the smaller table is hashed and broadcasted to all the worker nodes, and the join is performed locally on each node using the hash values. This can be more efficient than the regular broadcast join for certain types of joins, such as equi-joins, as it can reduce the amount of data that needs to be broadcasted and processed on each node.

