# Databricks notebook source
x = "hello world"
print(x)

# COMMAND ----------

len(x)

# COMMAND ----------

x[0]
#OP: h
# COMMAND ----------

x[1]

# COMMAND ----------

x[-1]
#OP: d
# COMMAND ----------

x[-3]
#OP: r

# COMMAND ----------

x[0:6]
#OP: hello
# COMMAND ----------

"e" in x
#OP: True
# COMMAND ----------

"E" in x
#OP: False
# COMMAND ----------

"e" in "hello"

# COMMAND ----------

if "e" in x:
    print("character exists")
else:
    print("character doesnt exists")

# COMMAND ----------

for i in x:
    print(i)

# COMMAND ----------

for i in enumerate(x):
    print(i)
#OP: (0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, ' '), (6, 'w'), (7, 'o'), (8, 'r'), (9, 'l'), (10, 'd')  
#enumerate() function adds a counter to an iterable and returns it in a form of enumerate object, which is an iterator that produces pairs of index and value for each item in the iterable, we can convert the enumerate object to a list of tuples using the list() function, where each tuple contains the index and the corresponding value from the original iterable
# COMMAND ----------

list(enumerate(x))
#OP: [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, ' '), (6, 'w'), (7, 'o'), (8, 'r'), (9, 'l'), (10, 'd')]
# COMMAND ----------

x = "   hello    world     "
print(x)
#
# COMMAND ----------

x.strip()
#OP: "hello    world"
#--strip method removes the leading and trailing whitespace from the string,


# COMMAND ----------

y = x.strip()
print(y)
#--we can assign the result of the strip method to a new variable, it will remove the leading and trailing whitespace from the string and return a new string without modifying the original string

# COMMAND ----------

x.lstrip()
#OP: "hello    world     "
#--lstrip method removes the leading whitespace from the string, 
# COMMAND ----------

x.rstrip()
#OP: "   hello    world"
#--rstrip method removes the trailing whitespace from the string, 
# COMMAND ----------

x = "*******hello world**********"
print(x)
x.strip("*")
#OP: "hello world" 
# COMMAND ----------

