# Databricks notebook source
lst = [(1,"John",10000),(2,"Sam",20000),(3,"Raj",30000),(4,"Ama",40000)]
print(lst)

# COMMAND ----------

rdd1=sc.parallelize(lst)
rdd1.collect()

# COMMAND ----------

help(rdd1.toDF)


# COMMAND ----------

df=rdd1.toDF()
#It converts an RDD (rdd1) into a Spark DataFrame (df).
display(df)

# COMMAND ----------

df3=rdd1.toDF(["Empid","Empname","Salary"])
#Output → proper DataFrame with column names
display(df3)

# COMMAND ----------

rdd2=df.rdd
#Converts a DataFrame back into an RDD
#Each row of the DataFrame becomes a Row object
rdd2.collect()

# COMMAND ----------

df4=spark.createDataFrame(rdd1,["Empid","Empname","Salary"])
display(df4)
'''
Converts your RDD (rdd1) into a DataFrame (df4) with column names:
Empid
Empname
Salary
'''


# COMMAND ----------

