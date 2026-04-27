# Databricks notebook source

#reduce() is used to apply a function cumulatively to all items in a list and return a single result.
# COMMAND ----------

import functools

# COMMAND ----------

help(functools.reduce)

# COMMAND ----------

lst = [1,2,3,4,5]
print(lst)

# COMMAND ----------

sum(lst)

# COMMAND ----------

def Add(x,y):
    print(x,y)
    return x + y

# COMMAND ----------

functools.reduce(Add,lst)

# COMMAND ----------

functools.reduce(lambda x ,y : x  + y ,lst)

# COMMAND ----------

