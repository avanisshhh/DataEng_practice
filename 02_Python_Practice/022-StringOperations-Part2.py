# Databricks notebook source
x = "hello world"
print(x)

# COMMAND ----------

x.upper()

# COMMAND ----------

y = "I LOVE PYTHON"
print(y)

# COMMAND ----------

y.lower()

# COMMAND ----------

y.capitalize()
#
# COMMAND ----------

a = "Hello"
print(a)

# COMMAND ----------



#x = "hello world"

a.swapcase()
#--swapcase method converts uppercase letters to lowercase and lowercase letters to uppercase
# COMMAND ----------

x.islower()
#OP: True
# COMMAND ----------

x.isupper()

# COMMAND ----------

x = "hello"
print(x)

# COMMAND ----------

help(x.find)

# COMMAND ----------

x.find("e")
#OP: 1
#--find method returns the index of the first occurrence of the specified substring, if the substring is not found, it returns -1
# COMMAND ----------

x.find("p")
#OP: -1
# COMMAND ----------

x.find("E")
#
# COMMAND ----------

x.find("l")
#OP: 2
#--find method returns the index of the first occurrence of the specified substring, if the substring
# COMMAND ----------

a = "heleale"

# COMMAND ----------

a.find("e")
#OP: 1
# COMMAND ----------

a.find("e",2)
#2 → start searching from index 2
#OP: 3

# COMMAND ----------

a.find("e",a.find("e")+1)
#a.find("e") → 1, a.find("e")+1 → 2, so it will start searching from index 2
# COMMAND ----------

help(a.index)

# COMMAND ----------

a.index("e")
#OP: 1
# COMMAND ----------

a.index("E")

# COMMAND ----------

X = "HELLO"

# COMMAND ----------

X.isalpha()
#--isalpha method returns True if all characters in the string are alphabetic and there is at least one character, otherwise it returns False
# COMMAND ----------

X.isnumeric()
#--isnumeric method returns True if all characters in the string are numeric and there is at least one character, otherwise it returns False
# COMMAND ----------

X.isalnum()
#--isalnum method returns True if all characters in the string are alphanumeric and there is at least one character, otherwise it returns False
# COMMAND ----------

y = "hello@a"

# COMMAND ----------

y.isalpha()
#OP: False
# COMMAND ----------

x = "I love python"
print(x)

# COMMAND ----------

x = "I love \"python\""
print(x)
#OP: I love "python"
#--we can use escape character \ to include special characters in the string, it will treat the special character as a normal character and include it in the string

# COMMAND ----------

