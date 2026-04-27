# Databricks notebook source
lst =[10,20,30,40,50]
print(lst)

# COMMAND ----------

help(lst.append)

# COMMAND ----------

lst.append(60)
print(lst)
#OP: [10,20,30,40,50,60]  
#--append method adds the item at the end of the list

help(lst.insert)

# COMMAND ----------

lst.insert(1,70)
#OP: [10,70,20,30,40,50,60]
#--insert method takes two arguments, first is index and second is the item to be added

# COMMAND ----------

print(lst)

# COMMAND ----------

lst1 = [10,20,30]
lst2 = [40,50,60]
print(lst1)
print(lst2)

# COMMAND ----------

help(lst1.extend)

# COMMAND ----------

lst1.extend(lst2)
print(lst1)
#OP: [10,20,30,40,50,60]
#--extend method adds the items of lst2 to lst1

# COMMAND ----------

lst1 = [10,20,30]
lst2 = [40,50,60]
lst3 = lst1 + lst2
print(lst3)

# COMMAND ----------

lst =[10,20,30,40,50]
print(lst)

# COMMAND ----------

help(lst.pop)

# COMMAND ----------

lst.pop()
#OP: 50
#--pop method removes the last item from the list and returns it

# COMMAND ----------

print(lst)

# COMMAND ----------

lst.pop(1)
print(lst)
#OP: [10,30,40]
#--pop method with index removes the item at the specified index and returns it
# COMMAND ----------

lst =[10,20,30,10,40,50,10]
print(lst)

# COMMAND ----------

help(lst.remove)

# COMMAND ----------

lst.remove(10)
#OP: [20,30,10,40,50,10]
#--remove method removes the first occurrence of the item from the list
print(lst)

# COMMAND ----------

lst.clear()
#OP: []
#--clear method removes all the items from the list

# COMMAND ----------

print(lst)

# COMMAND ----------

del lst
#--del keyword deletes the list from memory
# COMMAND ----------

print(lst)
#--NameError: name 'lst' is not defined because the list has been deleted from memory

# COMMAND ----------

