# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE tbl_Employees(
# MAGIC   id INTEGER,
# MAGIC   name STRING,
# MAGIC   city STRING,
# MAGIC   salary DOUBLE
# MAGIC )
# MAGIC USING DELTA

# COMMAND ----------
'''
Use of COPY INTO is that we can load directly into table from file

'''
# MAGIC %sql
# MAGIC
# MAGIC COPY INTO tbl_Employees
# MAGIC FROM 'dbfs:/FileStore/tables/Employees.csv'
# MAGIC FILEFORMAT=CSV
# MAGIC FORMAT_OPTIONS('header' = 'true')
'''Default everything in csv is string so we need to cast it to appropriate data type'''
# COMMAND ----------
''' we are  casting it to appropriate data type'''

# MAGIC %sql
# MAGIC
# MAGIC COPY INTO tbl_Employees
# MAGIC FROM (
# MAGIC       SELECT 
# MAGIC             id::integer,
# MAGIC             name::string,
# MAGIC             city::string,
# MAGIC             salary::double
# MAGIC             FROM
# MAGIC   'dbfs:/FileStore/tables/Employees.csv')
# MAGIC FILEFORMAT=CSV
# MAGIC FORMAT_OPTIONS('header' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tbl_employees

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC COPY INTO tbl_Employees
# MAGIC FROM (
# MAGIC       SELECT 
# MAGIC             id::integer,
# MAGIC             name::string,
# MAGIC             city::string,
# MAGIC             salary::double
# MAGIC             FROM
# MAGIC   'dbfs:/FileStore/tables/Employees.csv')
# MAGIC FILEFORMAT=CSV
# MAGIC FORMAT_OPTIONS('header' = 'true')
'''If we run again the same cmd and file exist so it will not load the data again. 
This feature is called idempotent load.

'''
# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE tbl_Employees_NEW
# MAGIC USING DELTA

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC COPY INTO tbl_Employees_NEW
# MAGIC FROM 'dbfs:/FileStore/tables/Employees.csv'
# MAGIC FILEFORMAT=CSV
# MAGIC FORMAT_OPTIONS ('inferSchema' = 'true', 'mergeSchema' = 'true','header' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from tbl_employees_NEW

# COMMAND ----------

FORMAT_OPTIONS ('mergeSchema' = 'true',
                  'delimiter' = '|',
                  'header' = 'true')