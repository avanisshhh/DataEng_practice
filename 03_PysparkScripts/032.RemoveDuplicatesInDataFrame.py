# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/EmployeesNew.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df2=df.distinct()
#distinct is used to get distinct rows from dataframe here we are getting distinct rows from employee dataframe
display(df2)

# COMMAND ----------

display(df.select("City").distinct())
#distinct can also be used with select statement to get distinct values of a column here we are getting distinct cities from employee dataframe

# COMMAND ----------

df3=df.dropDuplicates()
#dropDuplicates is used to get distinct rows from dataframe here we are getting distinct rows from employee dataframe
display(df3)

# COMMAND ----------

df4=df.dropDuplicates(["city"])
display(df4)

# COMMAND ----------

df4=df.dropDuplicates(["name","city"])
#dropDuplicates can also be used with subset of columns to get distinct rows based on those columns here we are getting distinct rows based on name and city columns
display(df4)

# COMMAND ----------

