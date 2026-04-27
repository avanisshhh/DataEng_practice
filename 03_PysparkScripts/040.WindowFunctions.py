# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Employees.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

from pyspark.sql.window import * 
from pyspark.sql.functions import * 

# COMMAND ----------

mywin = Window.orderBy("Salary")
#Sorts data by Salary (ascending by default)

df2=df.withColumn("Rownum",row_number().over(mywin))
display(df2)

# COMMAND ----------

mywin = Window.orderBy(col("Salary").desc())

df2=df.withColumn("Rownum",row_number().over(mywin))
display(df2)

# COMMAND ----------

mywin = Window.partitionBy("City").orderBy(col("Salary").desc())

df2=df.withColumn("Rownum",row_number().over(mywin))
display(df2)

# COMMAND ----------

mywin = Window.partitionBy("City","state").orderBy(col("Salary").desc())

df2=df.withColumn("Rownum",row_number().over(mywin))
display(df2)

# COMMAND ----------

mywin = Window.orderBy(col("Salary").desc())

df2=df.withColumn("Rank",rank().over(mywin))
display(df2)

# COMMAND ----------

mywin = Window.orderBy(col("Salary").desc())

df2=df.withColumn("Rank",dense_rank().over(mywin))
display(df2)

# COMMAND ----------

mywin = Window.orderBy(col("Salary"))

df2=df.withColumn("RunningTotal",sum("Salary").over(mywin))
display(df2)
'''
Calculates a cumulative (running) sum of Salary
Based on ascending Salary order
'''
# COMMAND ----------

mywin = Window.orderBy(col("Salary")).rowsBetween(Window.unboundedPreceding,Window.currentRow)
'''
unboundedPreceding: Start from the very first row of the window
unboundedPreceding: From the first row  currentRow:Up to the current row 

'''
df2=df.withColumn("RunningTotal",sum("Salary").over(mywin))
display(df2)

# COMMAND ----------

mywin = Window.orderBy(col("Salary")).rowsBetween(-2,Window.currentRow)
#Take current row + previous 2 rows (based on ordering)

df2=df.withColumn("RunningTotal",sum("Salary").over(mywin))
display(df2)

# COMMAND ----------

