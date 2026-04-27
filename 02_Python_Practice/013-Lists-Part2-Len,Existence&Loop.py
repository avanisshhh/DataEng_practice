# Databricks notebook source
lst = [10,20,30,40,50]

# COMMAND ----------

print(lst)

# COMMAND ----------

len(lst)
#OP: 5

# COMMAND ----------

20 in lst
#OP: True
# COMMAND ----------

100 in lst

# COMMAND ----------

if 10 in lst:
    print("Item exists in list")
else:
    print("Item doesnt exist in list")

# COMMAND ----------

if 100 in lst:
    print("Item exists in list")
else:
    print("Item doesnt exist in list")

# COMMAND ----------

for i in lst:
    print(i)

# COMMAND ----------

