# Databricks notebook source
employee_df = (spark.read.format("csv")
               .option("header",True)
               .option("inferSchema",True)
               .option("path","/FileStore/tables/Employees.csv").load()
               )
display(employee_df)

# COMMAND ----------

employee_df.write.saveAsTable("tblemployee")

# COMMAND ----------

employeeUpdates_df = (spark.read.format("csv")
               .option("header",True)
               .option("inferSchema",True)
               .option("path","/FileStore/tables/EmployeesUpdate.csv").load()
               )
display(employeeUpdates_df)

# COMMAND ----------

employeeUpdates_df.write.saveAsTable("tblemployee_stage")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tblemployee_stage
# MAGIC EXCEPT
# MAGIC SELECT * FROM tblemployee

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC MERGE INTO tblemployee AS T
# MAGIC   USING tblemployee_stage AS S
# MAGIC     ON T.id = S.id
# MAGIC
# MAGIC WHEN MATCHED THEN
# MAGIC   UPDATE SET 
# MAGIC       T.name = S.name,
# MAGIC       T.city = S.city,
# MAGIC       T.salary = S.salary
# MAGIC
# MAGIC WHEN NOT MATCHED THEN
# MAGIC   INSERT (
# MAGIC         id,
# MAGIC         name,
# MAGIC         city,
# MAGIC         salary 
# MAGIC   )VALUES(
# MAGIC         S.id,
# MAGIC         S.name,
# MAGIC         S.city,
# MAGIC         S.salary 
# MAGIC   )
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tblemployee

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE tblemployee

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE tblemployee_stage

# COMMAND ----------

from delta.tables import *

# COMMAND ----------

employeeTable = DeltaTable.forName(spark,"tblemployee")
print(type(employeeTable))

# COMMAND ----------
'''Here we are implementing using delta table 
'''
(employeeTable.alias("Target")
    .merge(source = employeeUpdates_df.alias("Source"),
           condition = "Target.id = Source.id"
           ).whenMatchedUpdateAll()
           .whenNotMatchedInsertAll()
           .execute() 
)


# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tblemployee

# COMMAND ----------

(employeeTable.alias("Target")
    .merge(source = employeeUpdates_df.alias("Source"),
           condition = "Target.id = Source.id"
           ).whenMatchedUpdate(set ={
               "city":"Source.city",
               "salary":"Source.salary"
           }               
           )
           .whenNotMatchedInsert(
               values = {
                   "id":"Source.id",
                   "name":"Source.name",
                   "city":"Source.city",
                   "salary":"Source.salary"
               }
               
           )
           .execute() 
)


# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tblemployee

# COMMAND ----------

