# Databricks notebook source
import random

# COMMAND ----------

help(random.random)

# COMMAND ----------

random.random()
#returns a random float number between 0.0 and 1.0
# COMMAND ----------

help(random.randint)

# COMMAND ----------

random.randint(1,100)
#returns a random integer between 1 and 100 (both inclusive)
#OP: 42
#OP: 17
#OP: 99
# COMMAND ----------

help(random.randrange)

# COMMAND ----------

random.randrange(1,10)
#returns a random integer between 1 and 10 (but not including 10)
#OP: 7

# COMMAND ----------

random.randrange(2,10,2)
#returns a random even integer between 2 and 10 (but not including 10)
#OP: 2
#OP: 4
#OP: 6
#OP: 8  
# COMMAND ----------

random.random() * 1000
#returns a random float number between 0.0 and 1000.0
# COMMAND ----------

