# Databricks notebook source
dbutils.help()
#dbutils is a utility provided by databricks to perform various operations like file system operations, notebook operations, widget operations etc. it has various modules like fs, notebook, widgets etc. each module has various functions to perform specific operations. we can use dbutils to perform various operations in databricks environment.

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.help("ls")

# COMMAND ----------

display(dbutils.fs.ls("/FileStore/tables"))

# COMMAND ----------

display(dbutils.fs.ls("/FileStore/tables/WriteModes"))
#ls is used to list the files and directories in a specified path. 
# COMMAND ----------

display(dbutils.fs.ls("/FileStore/tables/SalesMultiline.csv"))
#It gives error because ls is used to list the files and directories in a specified path. it cannot be used to read a file. we can use spark.read to read a file.
# COMMAND ----------

dbutils.fs.help("mkdirs")
#mkdirs is used to create a directory in the specified path. if the directory already exists, it will not throw an error. it will simply return false. if the directory is created successfully, it will return true.

# COMMAND ----------

dbutils.fs.mkdirs("/FileStore/Myfolder")
#mkdirs is used to create a directory in the specified path. if the directory already exists, it will not throw an error. it will simply return false. if the directory is created successfully, it will return true.
# COMMAND ----------

dbutils.fs.mkdirs("/FileStore/Myfolder")

# COMMAND ----------

dbutils.fs.mkdirs("/FileStore/Myfolder2/test")

# COMMAND ----------

dbutils.fs.rm("/FileStore/Myfolder")

# COMMAND ----------

dbutils.fs.rm("/FileStore/Myfolder")

# COMMAND ----------

dbutils.fs.rm("/FileStore/tables/WriteModes2",recurse=True)
'''
recurse is used to delete a directory and all its contents. if the directory is not empty, it will throw an error. if we set recurse to true, it will delete the directory and all its contents without throwing an error.
'''
# COMMAND ----------

dbutils.fs.rm("/FileStore/tables/EmployeesSpace.csv")
'''
If file exists:
File is deleted permanently
If file does NOT exist:
You’ll get an error
'''

# COMMAND ----------

dbutils.fs.cp("/FileStore/tables/Output","/FileStore/tables/Output2",recurse=True)
#recurse=True → copies all files and subfolders inside

# COMMAND ----------

dbutils.fs.mv("/FileStore/tables/Output","/FileStore/tables/Output2",recurse=True)

# COMMAND ----------

