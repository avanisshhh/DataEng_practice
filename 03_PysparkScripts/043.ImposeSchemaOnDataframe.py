# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Employees.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df = (spark.read.format("csv")
.option("path","/FileStore/tables/Employees.csv")
.option("header",True)
.load())
display(df)

# COMMAND ----------

#DDL String Schema
myschema = "id integer, name string, city string, salary integer"
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Employees.csv")
.option("header",True)
.schema(myschema)
.load())
display(df)

# COMMAND ----------

from pyspark.sql.types import * 

# COMMAND ----------
#Programmatic Schema (StructType)
myschema2 = StructType((
                       StructField("id",IntegerType()),
                       StructField("name",StringType()),
                       StructField("city",StringType()),
                       StructField("salary",IntegerType())
                       ))
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Employees.csv")
.option("header",True)
.schema(myschema2)
.load())
display(df)

# COMMAND ----------

