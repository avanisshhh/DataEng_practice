# Databricks notebook source
df = (spark.read.format("csv")
.option("path","/FileStore/tables/Employees.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df)

# COMMAND ----------

help(df.write)

# COMMAND ----------

df.write.format("csv").option("path","/FileStore/tables/WriteModes").save()

# COMMAND ----------

df2 = (spark.read.format("csv")
.option("path","/FileStore/tables/WriteModes")
.option("header",True)
.option("inferschema",True)
.load())
display(df2)

# COMMAND ----------



# COMMAND ----------

df.write.format("csv").option("path","/FileStore/tables/WriteModes").option("header",True).save()
#header option is used to specify whether the first line of the file contains the column names or not here we are specifying that the first line of the file contains the column names and it will be used as the column names in the dataframe when we read the file again
'''
❌ Without header=True (default = False):
Columns → _c0, _c1, _c2
Data → ("id","name","age"), (1,Alice,25), (2,Bob,30)

'''

# COMMAND ----------

(df.write.format("csv")
.option("path","/FileStore/tables/WriteModes")
.option("header",True)
.mode("append")
.save())
'''
👉 Adds new data to existing files/folder
👉 Does NOT delete existing data
'''
# COMMAND ----------

df2 = (spark.read.format("csv")
.option("path","/FileStore/tables/WriteModes/part-00000-tid-1704317011183956692-243beb99-3de5-44b4-b211-7daf5a319b6f-207-1-c000.csv")
.option("header",True)
.option("inferschema",True)
.load())
display(df2)


# COMMAND ----------

(df.write.format("csv")
.option("path","/FileStore/tables/WriteModes")
.option("header",True)
.mode("overwrite")
.save())
#It deletes the existing data at the target location and writes the new DataFrame data.

# COMMAND ----------

(df.write.format("csv")
.option("path","/FileStore/tables/WriteModes")
.option("header",True)
.mode("ignore")
.save())
#Does nothing if data exists 
# COMMAND ----------

(df.write.format("csv")
.option("path","/FileStore/tables/WriteModes")
.option("header",True)
.mode("errorifexists")
.save())
#Throws error if data exists
# COMMAND ----------

