# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE tbl_Employees_stage(
# MAGIC   id INTEGER,
# MAGIC   name STRING,
# MAGIC   city STRING,
# MAGIC   salary DOUBLE
# MAGIC )
# MAGIC USING DELTA

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC COPY INTO tbl_Employees_stage
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
# MAGIC delete from tbl_Employees where id>5

# COMMAND ----------

# MAGIC %sql
# MAGIC update tbl_Employees set salary = 5000
# MAGIC where id = 5

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from tbl_Employees_stage

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from tbl_Employees

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC MERGE INTO tbl_Employees as t
# MAGIC   USING tbl_Employees_stage as s 
# MAGIC     ON t.id = s.id
# MAGIC
# MAGIC WHEN MATCHED THEN
# MAGIC     UPDATE SET t.city = s.city,
# MAGIC                t.salary = s.salary
# MAGIC WHEN NOT MATCHED THEN
# MAGIC     INSERT (id,name,city,salary) VALUES (id,name,city,salary)
# MAGIC WHEN NOT MATCHED BY SOURCE THEN
# MAGIC     DELETE
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from tbl_employees

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY tbl_employees

# COMMAND ----------

