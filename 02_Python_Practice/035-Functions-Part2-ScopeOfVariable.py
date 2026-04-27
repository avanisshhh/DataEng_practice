# Databricks notebook source
def printmessage():
    x = "hi"
    print(x)

# COMMAND ----------

printmessage()

# COMMAND ----------


print(x)

# COMMAND ----------

y = "hello"
def printmessage():
    print(y)

# COMMAND ----------

printmessage()

# COMMAND ----------

def printmessage2():
    global a 
    a = "hi"
    print(a)

# COMMAND ----------

printmessage2()

# COMMAND ----------

print(a)

# COMMAND ----------

'''
Variable created inside a function → only accessible there.
Variable created outside a function → accessible inside and outside the function.
Global variable → created outside a function but can be accessed inside the function using global keyword.
Local variable → created inside a function and can only be accessed there.

'''
