# Databricks notebook source
# Accumulator
# MAGIC 1. Accumulator is a shared variable in spark
# MAGIC 2. As the name suggests it accumulates values
# MAGIC 3. Worker nodes can add values to accumulator variable, but cannot read it
# MAGIC 4. Only driver can read the values of accumulator using value 
# MAGIC 5. Accumulators can be created/defined using sparkcontext
# MAGIC 6. It supports data types like int and float


# COMMAND ----------

help(sc.accumulator)
#accumulator() function is used to create an accumulator variable and it takes the initial value of the accumulator as an argument and it returns an accumulator variable

# COMMAND ----------

x = sc.accumulator(0)

# COMMAND ----------

x.value
#value attribute is used to read the value of the accumulator variable and it returns the current value of the accumulator variable

# COMMAND ----------

type(x)
#x is an accumulator variable and it is of type pyspark.accumulators.Accumulator

# COMMAND ----------

x.add(1)
#add() function is used to add a value to the accumulator variable 

# COMMAND ----------

x.value

# COMMAND ----------

rdd = sc.parallelize([1,2,3,4,5])
rdd.collect()

# COMMAND ----------

y = sc.accumulator(0)
y.value
#OP = 0
# COMMAND ----------

def IncrementAccumulator(x):
    y.add(1)

# COMMAND ----------

rdd.foreach(IncrementAccumulator)
#foreach() function is used to apply a function to each element of the RDD and it takes the function as an argument and it applies the function to each element of the RDD

# COMMAND ----------

y.value
#OP = 5 because there are 5 elements in the RDD 
# COMMAND ----------

z = sc.accumulator(0)

# COMMAND ----------

def GreaterValue(x):
    if x > 3:
        z.add(1)

# COMMAND ----------

rdd.foreach(GreaterValue)

# COMMAND ----------

z.value

# COMMAND ----------

