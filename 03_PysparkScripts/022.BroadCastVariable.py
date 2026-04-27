# Databricks notebook source
# MAGIC %md ## Broadcast Variables
# MAGIC
# MAGIC 1. Broadcast variables are shared variables in spark
# MAGIC 2. It is a read only variable which is cached on each machine in a cluster
# MAGIC 3. Spark uses efficient algorithms to distribute broadcasted variables to reduce communication costs
# MAGIC

# COMMAND ----------

data = [(1,"India",10000),(2,"UK",50000),(3,"US",100000),(4,"FRANCE",90000)]

# COMMAND ----------

rdd = sc.parallelize(data)
rdd.collect()

# COMMAND ----------

products={1:"Phone",2:"Ipad",3:"Iphone",4:"Laptop"}

# COMMAND ----------

products[1]

# COMMAND ----------
'''we are implementing a broadcast variable to share the products dictionary across all the nodes in the cluster. This allows us to efficiently access the product names without having to send the entire dictionary with each task, thus reducing communication overhead and improving performance.'''
prodbc = sc.broadcast(products)
#broadcast() function is used to create a broadcast variable and it takes the variable to be broadcasted as an argument and it returns a broadcast variable

# COMMAND ----------

prodbc.value

# COMMAND ----------

type(prodbc)

# COMMAND ----------

rdd2 = rdd.map(lambda x : (x[0],prodbc.value[x[0]],x[1],x[2]))
rdd2.collect()

# COMMAND ----------

