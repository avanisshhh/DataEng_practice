# Databricks notebook source
import datetime as dt
import dateutil.relativedelta as rel

# COMMAND ----------

d1 = dt.date(2010,1,5)
d2 = dt.date.today()

# COMMAND ----------

help(rel)

# COMMAND ----------

rel.relativedelta(d2,d1)
'''
It calculates the difference between:

Start: 5 Jan 2010
End: today (2026-04-02, as per system date)

and returns the result in years, months, days (not just total days).
'''
# COMMAND ----------

d1 + rel.relativedelta(years=4)
#It shifts the date forward by 4 calendar years.

# COMMAND ----------

d1 + rel.relativedelta(months=5)
#Add 5 months → June 2010
#2010-06-05
# COMMAND ----------

d1 + rel.relativedelta(year=2020)
#Change the year part of the date to 2020, keep month/day same
# COMMAND ----------

d1 + rel.relativedelta(month=6)
#Replace the month with June (6), keep year and day same
#op: 2010-06-05

# COMMAND ----------

d1 + rel.relativedelta(year=2022,month=7,day=4)
#This is full field overwrite, it will change all 3 fields to the specified values
#OP: 2022-07-04
# COMMAND ----------

current_Date = dt.date.today()
print(current_Date)

# COMMAND ----------

current_Date + rel.relativedelta(day=1)
#Change day of current month to 1
# COMMAND ----------

dt.date.today() + rel.relativedelta(day=1,months=1,days=-1)
#This is a common way to get the last day of the current month
'''
Step 1: day=1

👉 Go to 1st of current month

2026-04-02 → 2026-04-01
Step 2: months=1

👉 Move to next month’s 1st day

2026-05-01
Step 3: days=-1

👉 Go back 1 day

2026-04-30
'''

# COMMAND ----------

