# Databricks notebook source
customers_df = (spark.read.format("csv")
               .option("header",True)
               .option("inferSchema",True)
               .option("path","/FileStore/tables/CustomerInfo.csv").load()
               )
display(customers_df)

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

help(hash) #32 bit

# COMMAND ----------

customersHash_df = customers_df.withColumn("HashKey",hash("CustomerKey"))
display(customersHash_df)

# COMMAND ----------

customersHash_df = customers_df.withColumn("HashKey",hash("EmailAddress","Phone"))
display(customersHash_df)

# COMMAND ----------

help(md5)

# COMMAND ----------

customersHash_df = customers_df.withColumn("HashKey",md5("EmailAddress"))
display(customersHash_df)


# COMMAND ----------

customersHash_df = customers_df.withColumn("HashKey",md5(concat("EmailAddress","Phone")))
#concat() function is used to concatenate two or more columns into a single column. here we are concatenating EmailAddress and Phone columns
display(customersHash_df)

# COMMAND ----------

help(sha1)

# COMMAND ----------

customersHash_df = customers_df.withColumn("HashKey",sha1("EmailAddress"))

display(customersHash_df)

# COMMAND ----------

customersHash_df = customers_df.withColumn("HashKey",sha1(concat("EmailAddress","Phone")))
display(customersHash_df)

# COMMAND ----------

help(sha2)

# COMMAND ----------

customersHash_df = customers_df.withColumn("HashKey",sha2("EmailAddress",256))
display(customersHash_df)

# COMMAND ----------

customersHash_df = customers_df.withColumn("HashKey",sha2(concat("EmailAddress","Phone"),256))
display(customersHash_df)

# COMMAND ----------

help(xxhash64)

# COMMAND ----------

customersHash_df = customers_df.withColumn("HashKey",xxhash64("EmailAddress"))

display(customersHash_df)

# COMMAND ----------

customersHash_df = customers_df.withColumn("HashKey",xxhash64("EmailAddress","Phone"))
display(customersHash_df)

# COMMAND ----------



