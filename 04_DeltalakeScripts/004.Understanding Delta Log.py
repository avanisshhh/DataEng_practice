# Databricks notebook source
dflog = (spark.read.format("json").
        option("path","/FileStore/tables/DeltaTables/tblrange/_delta_log/00000000000000000000.json").load())
display(dflog)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from  delta.`/FileStore/tables/DeltaTables/tblrange` 

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE delta.`/FileStore/tables/DeltaTables/tblrange` SET id = 20 WHERE id =5

# COMMAND ----------

dflog2 = (spark.read.format("json").
        option("path","/FileStore/tables/DeltaTables/tblrange/_delta_log/00000000000000000001.json").load())
display(dflog2)

# COMMAND ----------

# MAGIC %sql
# MAGIC DELETE FROM delta.`/FileStore/tables/DeltaTables/tblrange` WHERE id = 3

# COMMAND ----------

dflog2 = (spark.read.format("json").
        option("path","/FileStore/tables/DeltaTables/tblrange/_delta_log/00000000000000000002.json").load())
display(dflog2)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from  delta.`/FileStore/tables/DeltaTables/tblrange` 

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY delta.`/FileStore/tables/DeltaTables/tblrange` 

# COMMAND ----------

from delta.tables import *
from pyspark.sql.functions import *

# COMMAND ----------

help(DeltaTable.forPath)
#It help u implement operation on delta table

# COMMAND ----------

dtable  = DeltaTable.forPath(spark,"/FileStore/tables/DeltaTables/tblrange")
type(dtable)

# COMMAND ----------

help(dtable.update)

# COMMAND ----------

dtable.update(
    condition="id=6",
    set ={"id":"60"}
)

# COMMAND ----------

dtable.delete(
    condition="id=7"
)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from  delta.`/FileStore/tables/DeltaTables/tblrange` 

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY delta.`/FileStore/tables/DeltaTables/tblrange` 

# COMMAND ----------

