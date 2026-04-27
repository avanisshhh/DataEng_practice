# Databricks notebook source
dir()

# COMMAND ----------

import datetime

# COMMAND ----------

dir()

# COMMAND ----------

datetime.datetime.now()
#returns the current local date and time

# COMMAND ----------

help(datetime.datetime.now())

# COMMAND ----------

current_datetime = datetime.datetime.now()
#Can accept timezone
print(current_datetime)
#
# COMMAND ----------

type(current_datetime)
#OP: datetime.datetime
# COMMAND ----------

current_datetime = datetime.datetime.today()
print(current_datetime)



# COMMAND ----------

help(datetime.datetime.today())

# COMMAND ----------

yr = current_datetime.year
print(yr)

# COMMAND ----------

mn = current_datetime.month
print(mn)

# COMMAND ----------

dy = current_datetime.day
print(dy)

# COMMAND ----------

hr = current_datetime.hour
print(hr)

# COMMAND ----------

mins = current_datetime.minute
print(mins)

# COMMAND ----------

sec = current_datetime.second
print(sec)

# COMMAND ----------

datetime.datetime(2021,4,12)

# COMMAND ----------

help(datetime.date)

# COMMAND ----------

datetime.date(2021,4,12)
#Creates only a date object (no time)
# COMMAND ----------

help(datetime.time)

# COMMAND ----------

datetime.time(12,34,45)
#Creates only a time object (no date)
# COMMAND ----------

