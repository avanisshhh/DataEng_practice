# Databricks notebook source
# MAGIC %md #Interpolation
# MAGIC
# MAGIC Interpolation is technique to replace values of variable in a placeholder/template

# COMMAND ----------

X = 100

# COMMAND ----------

print(X)

# COMMAND ----------

print("X")

# COMMAND ----------

print("The value of variable x is :" + str(X))
#OP: The value of variable x is :100

# COMMAND ----------

y = "Hello"

# COMMAND ----------

print("The value of variable y is :" + y)

# COMMAND ----------

print("The value of variable x is :" + str(X) + " and value of variable y is:" + y)

# COMMAND ----------

print("The value of variable x is : %s" %(X))
#OP: The value of variable x is : 100
#%s is a placeholder for string and %d is a placeholder for integer

# COMMAND ----------

print("The value of variable x is : %s and value of variable y is: %s" %(X,y))

# COMMAND ----------

print("The value of variable x is : {}".format(X))
#format is a method of string class and {} is a placeholder for variable
#OP: The value of variable x is : 100

# COMMAND ----------

print("The value of variable x is : {} and value of variable y is: {}".format(X,y))

# COMMAND ----------

print("The value of variable x is : {a1} and value of variable y is: {b1}".format(a1=X,b1=y))

# COMMAND ----------

print("The value of variable x is : {a1} and value of variable y is: {b1}".format(b1=y,a1=X))

# COMMAND ----------

print(f"The value of variable x is : {X}")
#f is a prefix for string and {} is a placeholder for variable
#OP: The value of variable x is : 100
# COMMAND ----------

print(f"The value of variable x is : {X} and value of variable y is: {y}")

# COMMAND ----------

a = 100.516813

# COMMAND ----------

type(a)
#OP: float

# COMMAND ----------

print("The value of variable x is : %s" %(a))
#OP: The value of variable x is : 100.516813
# COMMAND ----------

print("The value of variable a is : %.2f" %(a))
#OP: The value of variable a is : 100.52
#%.2f is a placeholder for float with 2 decimal places
# COMMAND ----------

print("The value of variable a is : %.3f" %(a))
#OP: The value of variable a is : 100.517
#%.3f is a placeholder for float with 3 decimal places
# COMMAND ----------

