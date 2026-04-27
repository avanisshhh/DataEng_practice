# Databricks notebook source
x = 10
y = 20
z = 10

# COMMAND ----------

x == y
#OP: False
# COMMAND ----------

x == z
#OP: True
# COMMAND ----------

x > y
#OP: False
# COMMAND ----------

x>=y
#OP: False

# COMMAND ----------

x<y
#OP: True
# COMMAND ----------

x != y

# COMMAND ----------

10 == 10
#OP: True

# COMMAND ----------

if x == z:
    print("both values are same")    

# COMMAND ----------

if x == z
    print("both values are same")    
#OP: SyntaxError: invalid syntax
# COMMAND ----------

if x == z:
print("both values are same")    
#OP: IndentationError: expected an indented block
# COMMAND ----------

if x == y:
    print("both values are same")
else:
    print("both values are not same")

# COMMAND ----------

if x==z and x==y:
    print("yes")
else:
    print("no")

# COMMAND ----------

if x==z or x==y:
    print("yes")
else:
    print("no")

# COMMAND ----------

