# Databricks notebook source
help(input)

# COMMAND ----------

input()

# COMMAND ----------

x = input("Please enter a number")

# COMMAND ----------

print(x)

# COMMAND ----------

type(x)
#OP: str

# COMMAND ----------

x = int(input("Please enter a number"))
print(x)
type(x)
#OP: int

# COMMAND ----------

y = int(input("Please enter a number"))
if y >=80:
    print("High")
else:
    print("Low")

# COMMAND ----------

