# Databricks notebook source
[10,20,30,40,50]

# COMMAND ----------

mynums = [10,20,30,40,50]

# COMMAND ----------

print(mynums)

# COMMAND ----------

type(mynums)
#OP: list

# COMMAND ----------

countries = ["India","UK","US","Germany"]

# COMMAND ----------

print(countries)

# COMMAND ----------

type(countries)
#OP: list

# COMMAND ----------

lstmix = [1,"a",2,"b",3,"c"]
type(lstmix)
#OP: list

# COMMAND ----------

print(mynums)

# COMMAND ----------

mynums[0]

# COMMAND ----------

mynums[1]


# COMMAND ----------
mynums = [10,20,30,40,50]
mynums[-1]
#OP: 50
#--1 means last element, -2 means second last element and so on
# COMMAND ----------

mynums[-2]

# COMMAND ----------

mynums[0:2]
#OP: 10,20
#--0:2 means from index 0 to 1, 2 is exclusive
# COMMAND ----------

mynums[0:3]
#OP: 10,20,30
#--0:3 means from index 0 to 2, 3 is exclusive
# COMMAND ----------

mynums[2:]
#OP: 30,40,50
#--2: means from index 2 to end of the list
# COMMAND ----------

mynums[:3]
#OP: 10,20,30
#--:3 means from start of the list to index 2, 3 is exclusive
# COMMAND ----------

mynums[0:5:2]
#OP: 10,30,50
#--0:5:2 means from index 0 to 4, step size is 2

# COMMAND ----------

print(mynums)

# COMMAND ----------

mynums[-3:]
#OP: 30,40,50
#-- -3: means from index -3 to end of the list
# COMMAND ----------

