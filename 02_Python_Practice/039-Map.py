# Databricks notebook source
help(map)
'''
map() is used to apply a function to every item in an iterable (list, tuple, etc.) 
'''

# COMMAND ----------

def doublenum(x):
    return x * 2

# COMMAND ----------

doublenum(10)

# COMMAND ----------

lst = [1,2,3,4,5]
print(lst)

# COMMAND ----------

mp=map(doublenum,lst)
type(mp)

# COMMAND ----------

list(mp)

# COMMAND ----------

dlst = list(map(doublenum,lst))
print(dlst)

# COMMAND ----------

dlst = list(map(doublenum,[1,2,3,4,5]))
print(dlst)

# COMMAND ----------

dlst2 = list(map(lambda x : x* 2,[1,2,3,4,5]))
print(dlst2)

# COMMAND ----------

countries = ["india","uk","us"]
print(countries)

# COMMAND ----------

def converttoupper(x):
    return x.upper()

# COMMAND ----------

ucountries = list(map(converttoupper,countries))
print(ucountries)


# COMMAND ----------

ucont = list(map(lambda y : y.upper(),countries))
print(ucont)

# COMMAND ----------

