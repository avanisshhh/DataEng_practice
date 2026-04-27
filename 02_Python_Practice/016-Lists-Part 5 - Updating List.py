# Databricks notebook source
lst = [10,20,40,30,60,50]
print(lst)

# COMMAND ----------

lst[0]
#OP: 10
# COMMAND ----------

lst[0] = 80
print(lst)
#OP: [80,20,40,30,60,50]
#--lists are mutable, we can change the value of an item in the list using indexing 
# COMMAND ----------

mutability
immutability