# Databricks notebook source

#Installing JDBC connection from Utilites file avail all fn and variable
# MAGIC %run ./Utilities

# COMMAND ----------

df=ReadTableFromDatabase("dbo.ordersnew")
display(df)

# COMMAND ----------

empdf = QueryFromDatabase("select orderdate, productkey , country, salesamount from ordersnew")
display(empdf)

# COMMAND ----------

WriteDataframeToDatabase(df,"dbo.orders3")

# COMMAND ----------

WriteDataframeToDatabaseOverwrite(df,"Orders2")

# COMMAND ----------

WriteDataframeToDatabaseMode(df,"dbo.Orders2","append")

# COMMAND ----------

WriteDataframeToDatabaseMode(df,"dbo.Orders2","overwrite")

# COMMAND ----------

