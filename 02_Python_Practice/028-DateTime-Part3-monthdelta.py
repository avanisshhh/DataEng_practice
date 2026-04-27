# Databricks notebook source
import monthdelta

# COMMAND ----------

# MAGIC %pip install monthdelta

# COMMAND ----------

import monthdelta

# COMMAND ----------

help(monthdelta)

# COMMAND ----------

help(monthdelta.monthdelta)

# COMMAND ----------

import datetime

# COMMAND ----------

dt=datetime.date(2022,5,12)

# COMMAND ----------

dt + monthdelta.monthdelta(4)
#OP: 2022-09-12
# COMMAND ----------

dt + monthdelta.monthdelta(-9)
#OP: 2021-08-12
# COMMAND ----------

dt + monthdelta.monthdelta(12)
#OP: 2023-05-12

# COMMAND ----------

d1 = datetime.date(2021,12,1)
d2 = datetime.date(2023,6,5)

monthdelta.monthmod(d1,d2)
'''
1. Count full months

From 2021-12-01 to 2023-06-01:

Dec 2021 → Dec 2022 = 12 months
Dec 2022 → Jun 2023 = 6 months
👉 Total = 18 full months
2. Remaining days

From 2023-06-01 to 2023-06-05:

👉 4 days remaining
'''
# COMMAND ----------

# MAGIC %pip uninstall -y monthdelta

# COMMAND ----------

