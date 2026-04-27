# Databricks notebook source
x

# COMMAND ----------

prnt

# COMMAND ----------

for i in x
    print(i)

# COMMAND ----------

100/0

# COMMAND ----------

10 + "s"

# COMMAND ----------

lst = [1,2,3,4]
lst[5]

# COMMAND ----------

x = 100
print(x)
x/0
y = "hello"
print(y)

# COMMAND ----------
#try-except is used to handle errors gracefully so your program doesn’t crash.
try:
    x = 100
    print(x)
    x/0
    y = "hello"
    print(y)
except:
    print("some error occured")

# COMMAND ----------

try:
    x = 100
    print(x)
    x/1
    y = "hello"
    print(y)
except:
    print("some error occured")

# COMMAND ----------

try:
    x = 100
    print(x)
    x/0
    y = "hello"
    print(y)
except Exception as e:
    print(e)

# COMMAND ----------

try:
    x = 100
    print(x)
    x/1
    5 + "s"
    y = "hello"
    print(y)
except ZeroDivisionError as z:
    print(z)
except TypeError as t:
    print(t)
        

# COMMAND ----------

try:
    x = 100
    print(x)
    x/0
    y = "hello"
    print(y)
except Exception as e:
    print(e)
finally:
    print("This runs always")

# COMMAND ----------

try:
    x = 100
    print(x)
    x/1
    y = "hello"
    print(y)
except Exception as e:
    print(e)
finally:
    print("This runs always")

# COMMAND ----------

raise ZeroDivisionError

# COMMAND ----------

raise ZeroDivisionError("Cannot divide by zero")

# COMMAND ----------

