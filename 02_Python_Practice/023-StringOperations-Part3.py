# Databricks notebook source
x = "hello"
print(x)

# COMMAND ----------

help(x.replace)

# COMMAND ----------

x.replace("e","x")
#OP: hxllo
# COMMAND ----------

x.replace("e","abc")
#OP: habcllo
# COMMAND ----------

x.replace("e","")
#OP: hllo
# COMMAND ----------

x.replace("e"," ")
#OP: h llo
# COMMAND ----------

x.replace("l","a")

# COMMAND ----------

x.replace("l","a",1)
#OP: healo
#First "l" (index 2) → replaced with "a"
#Only 1 replacement allowed

# COMMAND ----------

x.replace("l","a",2)
#OP: heaao
# COMMAND ----------

x.replace("E","x")
#OP: hello
# COMMAND ----------

help(x.count)

# COMMAND ----------

x.count("l")

# COMMAND ----------

x.startswith("h")

# COMMAND ----------

x.startswith("e")

# COMMAND ----------

x.startswith("he")
#OP: True
# COMMAND ----------

x.startswith("hq")
#OP: False
# COMMAND ----------

x.endswith("o")

# COMMAND ----------

x.endswith("lo")

# COMMAND ----------

x.startswith("H")
#OP: False
# COMMAND ----------

x = "i love python"
print(x)

# COMMAND ----------

y = x.split(" ")
print(y)
#OP: ['i', 'love', 'python']
#--split() method splits the string into a list of substrings based on the specified separator
# COMMAND ----------

for i in y:
    print(i)
#OP: i, love, python
#--we can iterate over the list of substrings and print each substring on a new line
# COMMAND ----------

x = "hello"
print(x)

# COMMAND ----------

x[0] ="i"
print(x)
#OP: TypeError: 'str' object does not support item assignment
#--strings are immutable in python, we cannot change the value of a string after it is created
# COMMAND ----------

