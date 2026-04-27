# Databricks notebook source
import datetime as dt

# COMMAND ----------

d1 = dt.datetime(2022,3,15,13,12,45)
print(d1)

# COMMAND ----------

help(dt.datetime.strftime)
#The strftime() method formats a datetime object into a string based on the specified format codes.

# COMMAND ----------

yr = d1.strftime("%y")
#%y gives last 2 digits of year
print(yr)

# COMMAND ----------

d1.strftime("%Y")
#%Y gives full year
#OP: 2022
# COMMAND ----------

d1.strftime("%m")
#%M gives month in 2 digits
# COMMAND ----------

d1.strftime("%d")
#%d gives day of month in 2 digits
# COMMAND ----------

d1.strftime("%H")
#%H gives hour in 24 hour format
# COMMAND ----------

d1.strftime("%M")
#%M gives minute in 2 digits
# COMMAND ----------

d1.strftime("%S")
#%S gives second in 2 digits
# COMMAND ----------

d1.strftime("%b")
#%b gives abbreviated month name
#OP: Mar
# COMMAND ----------

d1.strftime("%B")
#%B gives full month name
#OP: March
# COMMAND ----------

d1.strftime("%a")
#%a gives abbreviated weekday name
#OP: Wed
# COMMAND ----------

d1.strftime("%A")
#%A gives full weekday name
#OP: Wednesday
# COMMAND ----------

d1.strftime("%d-%m-%Y")
#This is a common date format used in many countries (day-month-year).
#OP: 15-03-2022
# COMMAND ----------

help(dt.datetime.strptime)

# COMMAND ----------

d2 = "15-03-2021"
type(d2)

# COMMAND ----------

dt.datetime.strptime(d2,"%d-%m-%Y")
#convert string to datetime
#OP: 2021-03-15 00:00:00

# COMMAND ----------

dt.datetime.strptime(d2,"%d/%m-%Y")
#This will throw an error because the format specified does not match the actual format of the string.


# COMMAND ----------

