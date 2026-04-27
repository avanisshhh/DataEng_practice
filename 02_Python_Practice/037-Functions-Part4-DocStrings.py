# Databricks notebook source
import random

# COMMAND ----------

help(random.random)

# COMMAND ----------

def Add(x,y):
    return x + y

# COMMAND ----------

help(Add)

# COMMAND ----------

random.random.__doc__
#Returns the docstring (documentation string) of the function.
# COMMAND ----------

Add.__doc__
#Shows documentation of your custom function/class Add


#  COMMAND ----------

def Add(x,y):
    """
        This function adds two numbers
    """
    return x + y

# COMMAND ----------

help(Add)

# COMMAND ----------

Add.__doc__

# COMMAND ----------

