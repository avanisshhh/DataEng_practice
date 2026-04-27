# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Employees.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df = (spark.read.format("csv")
.option("path","/FileStore/tables/Employees_comment.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

df = (spark.read.format("csv")
.option("path","/FileStore/tables/Employees_comment.csv")
.option("header",True)
.option("inferschema",True)
.option("delimiter","|")
.load())
display(df)

# COMMAND ----------

df = (spark.read.format("csv")
.option("path","/FileStore/tables/Employees_comment.csv")
.option("header",True)
.option("inferschema",True)
.option("delimiter","|")
.option("comment","#")
.load())
#comment option is used to ignore the lines starting with a specific character here we are ignoring the lines starting with # in the specified file
#delimiter option is used to specify the delimiter used in the file here we are using | as a delimiter in the specified file default delimiter is , (comma)
display(df)

# COMMAND ----------

df = (spark.read.format("csv")
.option("path","/FileStore/tables/SalesMultiline.csv")
.option("header",True)
.option("inferschema",True)
.option("delimiter","|")
.option("multiline",True)
.load())
#multiline option is used to allow a single column value to span multiple lines here we are allowing the address column to span multiple lines in the specified file
display(df)


'''

Without delimiter Spark assumes , (comma)
comment :Ignores lines starting with a specific character
multiline:Allows a single column value to span multiple lines

e.g 101|John|"Address line1 Address line2"
EmpId | Name | Address
101   | John | Address line1 Address line2

bcs Spark treats new line as new row → data breaks



Without multiline:
EmpId | Name | Address
101   | John | Address line1
Address line2 
**Here data corruption occurs because Spark treats new line as new row, so the address column value is split into two rows, which is not the intended outcome.**
With multiline:
EmpId | Name | Address
101   | John | Address line1 Address line2
'''
# COMMAND ----------

df = (spark.read.format("csv")
.option("path","/FileStore/tables/EmployeesSpace.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

from pyspark.sql.functions import * 

# COMMAND ----------

df3=df.withColumn("Collen",length("name"))
display(df3)

# COMMAND ----------

df = (spark.read.format("csv")
.option("path","/FileStore/tables/EmployeesSpace.csv")
.option("header",True)
.option("inferschema",True)
.option("ignoreLeadingWhiteSpace",True)
.option("ignoreTrailingWhiteSpace",True)
.load())
display(df)

# COMMAND ----------

df3=df.withColumn("Collen",length("name"))
display(df3)

# COMMAND ----------

