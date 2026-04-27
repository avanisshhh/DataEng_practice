# Databricks notebook source
myset = {10,20,30,40}

# COMMAND ----------

print(myset)

# COMMAND ----------

type(myset)
#OP: set
# COMMAND ----------

myset2 ={10,40,20,10,20,50}
print(myset2)
#OP: {10, 20, 40, 50}
#--sets are unordered collection of unique items, it automatically removes duplicates and stores only unique items  
# COMMAND ----------

lst = [10,40,20,10,20,50]
print(lst)

# COMMAND ----------

myset3 = set(lst)
print(myset3)
#OP: {10, 20, 40, 50}
#--we can convert a list to a set using set() function, it will remove duplicates
# COMMAND ----------

mynewlist = list(myset3)
print(mynewlist)

# COMMAND ----------

lst = [10,40,20,10,20,50]
uniqlist =list(set(lst))
print(uniqlist)
#OP: [40, 10, 50, 20]
#--we can remove duplicates from a list by converting it to a set and then back to a list, but it will not maintain the original order of the list

# COMMAND ----------

myset[0]
#OP: TypeError: 'set' object is not subscriptable
#--sets are unordered collection of unique items, we cannot access items in a set using indexing
# COMMAND ----------

myset[0] = 10
#OP: TypeError: 'set' object does not support item assignment
#--sets are unordered collection of unique items, we cannot change the value of an item in a set using indexing, sets are immutable, we cannot change the value of an item in a set
# COMMAND ----------

myset5 = {10,20,40,50}
myset6 = {20,10,70}


# COMMAND ----------

print(myset5.union(myset6))
#OP: {70, 10, 20, 40, 50}
#--union method returns a new set that contains all the items from both sets, it removes duplicates and returns only unique items
# COMMAND ----------

print(myset5.difference(myset6))
#OP: {40, 50}
#--difference method returns a new set that contains the items that are present in the first set
# COMMAND ----------

print(myset6.difference(myset5))

# COMMAND ----------

