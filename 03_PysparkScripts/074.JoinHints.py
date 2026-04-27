# Databricks notebook source
df1 = spark.range(1000000)
df2 = spark.range(1000000)


# COMMAND ----------

joindf = df1.join(df2,df1.id==df2.id)
display(joindf)

# COMMAND ----------

joindf.explain(True)

# COMMAND ----------

from pyspark.sql.functions import * 

# COMMAND ----------

joindf2=df1.join(df2.hint("broadcast"),df1.id==df2.id)
display(joindf2)

# COMMAND ----------

joindf2.explain(True)

# COMMAND ----------

joindf3=df1.join(broadcast(df2),df1.id==df2.id)
display(joindf3)

# COMMAND ----------

joindf3.explain(True)

# COMMAND ----------

joindf4=df1.join(broadcast(df2),df1.id>=df2.id)
display(joindf4)

# COMMAND ----------

joindf4.explain(True)

# COMMAND ----------

joindf5=df1.join(df2.hint("MERGE"),df1.id==df2.id)
#hint("MERGE") is used to specify the join strategy as sort merge join. when we use hint("MERGE") in the join method it will force spark to use sort merge join strategy to perform the join operation. 
display(joindf5)

# COMMAND ----------

joindf5.explain(True)

# COMMAND ----------

joindf6=df1.join(df2.hint("SHUFFLE_REPLICATE_NL"),df1.id>=df2.id)
#Non equi join here we get cartisian product 
display(joindf6)
'''
Shuffle Replicate Nested Loop Join
👉 This is NOT an equi-join (no = condition)
👉 It’s a range join / non-equi join

working:
1. Shuffle both DataFrames
Based on partitions (not key-based like SMJ)
2. Replicate one DataFrame (df2)
👉 df2 is copied to every partition of df1
3. Nested Loop Execution
For each row in df1:
Compare with ALL rows of df2


🔹 Why “Replicate”?
Because:
👉 df2 is sent to all partitions of df1
So each partition can independently do:
Full comparison (nested loop)
'''

# COMMAND ----------

joindf6.explain(True)

# COMMAND ----------


