# Databricks notebook source
lst = list(range(10,60,10))
print(lst)
#OP: [10,20,30,40,50]

# COMMAND ----------

lst = [10,20,10,30,10]
print(lst)

# COMMAND ----------

lst.count(10)
#OP: 3
#--count method returns the number of occurrences of the specified item in the list

# COMMAND ----------

help(lst.copy)

# COMMAND ----------

lst2 = lst.copy()
#--copy method creates a shallow copy of the list


# COMMAND ----------

print(lst2)

# COMMAND ----------

lst.append(60)
print(lst)
#OP: [10,20,10,30,10,60]
print(lst2)
#OP: [10,20,10,30,10]

# COMMAND ----------

lst1 = [1,2,3,4,5]
print(lst1)

# COMMAND ----------

lst2=lst1.reverse()
print(lst2)
#OP: None 
#--reverse method reverses the list in place and returns None

# COMMAND ----------

lst1.reverse()
print(lst1)
#OP: [5,4,3,2,1]
# COMMAND ----------

help(lst.sort)

# COMMAND ----------

lst1.sort()
print(lst1)
#sort method sorts the list in place and returns None
# COMMAND ----------

lst1.sort(reverse=True)
print(lst1)
#OP: [5,4,3,2,1]
#--sort method with reverse=True sorts the list in descending order
# COMMAND ----------

