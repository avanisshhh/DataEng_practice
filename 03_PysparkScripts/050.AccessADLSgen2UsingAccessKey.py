# Databricks notebook source
spark.conf.set(
    "access-key")
#Access Key 



# COMMAND ----------

display(dbutils.fs.ls("abfss://mycontainer@cdudevmyadls.dfs.core.windows.net/"))


# COMMAND ----------

display(dbutils.fs.ls("abfss://mycontainer@cdudevmyadls.dfs.core.windows.net/Countries"))


# COMMAND ----------

df = spark.read.format("csv").option("header",True).option("path","abfss://mycontainer@cdudevmyadls.dfs.core.windows.net/orders.csv").load()
display(df)

# COMMAND ----------

df.write.format("csv").option("header",True).option("path","abfss://mycontainer@cdudevmyadls.dfs.core.windows.net/TestWrite").save()

# COMMAND ----------


