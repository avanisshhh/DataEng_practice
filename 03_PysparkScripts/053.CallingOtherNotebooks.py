# Databricks notebook source
# MAGIC %run /PYSPARK/ENGLISH/Utilities

#run is used to call another notebook in the current notebook and we can also pass parameters to the called notebook. here we are calling the Utilities notebook and we can use the functions defined in the Utilities notebook in our current notebook.
#we can also call the notebook from another folder by providing the relative path of the notebook.

# COMMAND ----------

x

# COMMAND ----------

double(3)

# COMMAND ----------

# MAGIC %run ./Utilities
#relative path calling the notebook from the same folder
# COMMAND ----------

# MAGIC %run ../test
#one folder back we do ..
#. current folder
#.. one folder back
# COMMAND ----------

y

# COMMAND ----------

# MAGIC 
# %run /PYSPARK/ENGLISH/052.Widgets $txtcountry='UK'

'''Default value can be pass like this mentioned above '''

#we can also pass parameters to the called notebook by providing the parameter name and value in the run command. here we are passing the value UK to the parameter txtcountry in the 052.Widgets notebook and we can use this value in our current notebook by using the get function of widgets module. here we are getting the value of txtcountry parameter and storing it in a variable cnt and then printing the value of cnt variable.

# COMMAND ----------

dbutils.notebook.run("/PYSPARK/ENGLISH/Utilities",10)
#10 is timeout factor. if the called notebook takes more than 10 seconds to execute, it will throw an error. we can set the timeout factor as per our requirement. if we set it to 0, it will wait indefinitely for the called notebook to execute.

#we can also use the run function of notebook module to call another notebook and it will return the value returned by the called notebook. here we are calling the Utilities notebook and it will return the value returned by the Utilities notebook and we are storing that value in a variable result and then printing the value of result variable.
# COMMAND ----------


