# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Employees.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df2 = (spark.read.format("csv")
.option("path","/FileStore/tables/Employees.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df2)

# COMMAND ----------

df3 = (spark.read.format("csv")
.option("path","/FileStore/tables/EmployeesNew2.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df3)

# COMMAND ----------

df4=df.union(df2)
display(df4)

# COMMAND ----------

df4=df.union(df2).distinct()
#union is used to combine two dataframes with same schema here we are combining employee and employeeNew2 dataframes and then we are using distinct to get distinct rows from the combined dataframe
display(df4)

# COMMAND ----------

df5=df.union(df3)
display(df5)
'''
Normal union() works by position, which can break data if column order differs.


👉 It combines two DataFrames row-wise
👉 Matches columns by column name (NOT position)
unionByName() 
👉 Match columns by label, then stack

df.unionByName(df3, allowMissingColumns=True)
'''
# COMMAND ----------

df4=df.unionByName(df3)
#unionByName is used to combine two dataframes based on column names here we are combining employee and employeeNew2 dataframes based on column names and it will automatically handle the missing columns in both dataframes
display(df4)

# COMMAND ----------

df5=df.union(df2).union(df3)

'''
❌ unionAll → Deprecated / removed
'''
