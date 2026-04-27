# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE MyDb.Employees(
# MAGIC   EmpId INT,
# MAGIC   EmpName STRING,
# MAGIC   DOJ TIMESTAMP,
# MAGIC   YearOfJoining INT GENERATED ALWAYS AS (YEAR(DOJ)),
# MAGIC   MonthOfJoining INT GENERATED ALWAYS AS (MONTH(DOJ)),
# MAGIC   DayOfJoining INT GENERATED ALWAYS AS (DAY(DOJ))
# MAGIC )
# MAGIC USING DELTA
# MAGIC


'''
we cant insert value in generated column as it is auto generated based on the expression provided during table creation.'''
# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE FORMATTED Mydb.Employees

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into MyDb.Employees(EmpId,EmpName,DOJ) VALUES(1,'John','2020-01-12'),(2,'Sam','2021-04-16')
# MAGIC ,(3,'Aman','2022-08-09')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from MyDb.Employees

# COMMAND ----------

df = spark.read.format("json").option("path","dbfs:/user/hive/warehouse/mydb.db/employees/_delta_log/00000000000000000000.json").load()
display(df)

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC Generated columns are stored as if they were normal columns. That is, they occupy storage.
# MAGIC
# MAGIC The following restrictions apply to generated columns:
# MAGIC
# MAGIC A generation expression can use any SQL functions in Spark that always return the same result when given the same argument values, except the following types of functions:
# MAGIC
# MAGIC User-defined functions.
# MAGIC
# MAGIC Aggregate functions.
# MAGIC
# MAGIC Window functions.
# MAGIC
# MAGIC Functions returning multiple rows.

# COMMAND ----------

