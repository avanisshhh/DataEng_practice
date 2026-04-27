# Databricks notebook source
def doublenum(x):
    return x * 2

# COMMAND ----------

doublenum(10)

# COMMAND ----------

lambda x : x * 2

# COMMAND ----------

y = lambda x : x * 2

# COMMAND ----------

type(y)
#OP: function
# COMMAND ----------

print(y(10))

# COMMAND ----------

def Add(x,y):
    return x + y

# COMMAND ----------

Add(10,30)

# COMMAND ----------

a = lambda x,y : x + y
print(a(10,30))

# COMMAND ----------

