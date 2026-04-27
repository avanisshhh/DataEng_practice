# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Products.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

from pyspark.sql.functions import * 

# COMMAND ----------

df2=df.select(split("EnglishProductName"," ").alias("Productname"))

'''
#Splits product name by space " "
#Converts string → array
| Productname         |
| ------------------- |
| ["Mountain","Bike"] |

'''

display(df2)

# COMMAND ----------

df3=df2.selectExpr("Productname[0]")
display(df3)
#Get the first word

# COMMAND ----------

df3=df2.selectExpr("Productname[1]")
##Get the 2nd word
display(df3)

# COMMAND ----------

df3=df2.withColumn("NoOfElements",size("Productname"))
display(df3)
'''
#size() gives number of elements in array

| Productname         | NoOfElements |
| ------------------- | ------------ |
| ["Mountain","Bike"] | 2            |
'''

# COMMAND ----------

df4=df2.withColumn("Condition",array_contains("Productname","Bike"))
display(df4)
'''
Checks if array contains "Bike"
| Productname         | Condition |
| ------------------- | --------- |
| ["Mountain","Bike"] | true      |
| ["Road","Helmet"]   | false     |

'''

# COMMAND ----------

