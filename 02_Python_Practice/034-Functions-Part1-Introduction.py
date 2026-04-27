# Databricks notebook source
def printmessage():
    print("hello john")

# COMMAND ----------

printmessage()

# COMMAND ----------

def printmessage2(empname):
    print(f"hello {empname}")

# COMMAND ----------

printmessage2()

# COMMAND ----------

printmessage2("test")

# COMMAND ----------

20 + 30

# COMMAND ----------

def AddNumbers(x,y):
    print( x + y)

# COMMAND ----------

AddNumbers(10,20)

# COMMAND ----------

AddNumbers(100,20)

# COMMAND ----------

total = AddNumbers(100,20)
print(total)

# COMMAND ----------

def AddNumbers2(x,y):
    return x + y 

# COMMAND ----------

AddNumbers2(10,20)

# COMMAND ----------

total2 = AddNumbers2(10,20)
print(total2)

# COMMAND ----------

help(AddNumbers)

# COMMAND ----------

