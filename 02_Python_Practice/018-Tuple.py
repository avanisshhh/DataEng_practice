# Databricks notebook source
mytup = (1,"John",1000,"nyc")
#--tuples are ordered collection of items, they are immutable, we cannot change the value of an item in a tuple, we can access items in a tuple using indexing, they can contain duplicate items, they can contain items of different data types  
# COMMAND ----------

print(mytup)

# COMMAND ----------

type(mytup)
#OP: tuple
# COMMAND ----------

mytup[0]
#OP: 1
#--we can access items in a tuple using indexing, indexing starts from 0, we can also use negative indexing to access items from the end of the tuple, -1 means last item
# COMMAND ----------

mytup[1]
#OP: 'John'
# COMMAND ----------

mytup[0] = 2
#OP: TypeError: 'tuple' object does not support item assignment
# COMMAND ----------

