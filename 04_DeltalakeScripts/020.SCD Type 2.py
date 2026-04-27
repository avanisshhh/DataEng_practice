# Databricks notebook source
customers_df = (spark.read.format("csv")
               .option("header",True)
               .option("inferSchema",True)
               .option("path","/FileStore/tables/CustomerInfo.csv").load()
               )
display(customers_df)

# COMMAND ----------

from pyspark.sql.functions import * 

# COMMAND ----------

enddate = lit('9999-12-31').cast("timestamp")
print(enddate)

# COMMAND ----------

customersSCD_df=(customers_df.withColumn("StartDate",lit('2024-08-10').cast("timestamp"))
.withColumn("EndDate",enddate)
.withColumn("IsActive",lit("Y"))
)
display(customersSCD_df)

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS Customers_SCD

# COMMAND ----------

customersSCD_df.write.saveAsTable("Customers_SCD")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM customers_scd

# COMMAND ----------

customerHash_df = customersSCD_df.withColumn("HashKey",xxhash64("EmailAddress","Phone"))
display(customerHash_df)

# COMMAND ----------

CustomerUpdate_df = (spark.read.format("csv")
               .option("header",True)
               .option("inferSchema",True)
               .option("path","/FileStore/tables/CustomerUpdates.csv").load()
               ).withColumnRenamed("CustomerKey","CustomerKey_Upd"
               ).withColumnRenamed("Fullname","Fullname_Upd"
               ).withColumnRenamed("EmailAddress","EmailAddress_Upd"
               ).withColumnRenamed("Phone","Phone_Upd"
               )

display(CustomerUpdate_df)

# COMMAND ----------

CustomerUpdateHash_df = CustomerUpdate_df.withColumn("HashKey_Upd",xxhash64("EmailAddress_Upd","Phone_Upd"))
display(CustomerUpdateHash_df)

# COMMAND ----------


joined_df = CustomerUpdateHash_df.join(customerHash_df,CustomerUpdateHash_df.HashKey_Upd
 == customerHash_df.HashKey
,"left")
#CustomerUpdateHash_df and customerHash_df b are joined on the hash key columns to identify the records that have changes in the email address or phone number. The left join is used to keep all records from the CustomerUpdateHash_df and only matching records from the customerHash_df. This allows us to identify which records in the CustomerUpdateHash_df have changes compared to the existing records in the customerHash_df.
display(joined_df)

# COMMAND ----------

from datetime import *

# COMMAND ----------

Startdate = lit(datetime.now() + timedelta(days=1)) 

staged_df = joined_df.filter(col("CustomerKey").isNull()).select(
    "CustomerKey_Upd",
    "Fullname_Upd",
    "EmailAddress_Upd",
    "Phone_Upd",
    "HashKey_Upd"
).withColumn("StartDate",Startdate
).withColumn("EndDate",enddate
)
display(staged_df)

# COMMAND ----------

from delta.tables import *

# COMMAND ----------

CustomerDeltaTable = DeltaTable.forName(spark,"Customers_SCD")

# COMMAND ----------

today = current_timestamp()
CustomerDeltaTable.alias("Target").merge(
    staged_df.alias("Source"),
    "Target.CustomerKey = Source.CustomerKey_Upd"
).whenMatchedUpdate(
    condition = "Target.IsActive = 'Y'",
    set = {
        "Target.IsActive" : lit("N"),
        "Target.EndDate":today
    }
).whenNotMatchedInsert(
  values = {
    "CustomerKey": "Source.CustomerKey_Upd",
    "Fullname": "Source.Fullname_Upd",
    "EmailAddress": "Source.EmailAddress_Upd",
    "Phone":"Source.Phone_Upd",
    "StartDate": "Source.StartDate",
    "EndDate": "Source.EndDate",
    "IsActive" : lit("Y")
  }
).execute()

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM customers_scd

# COMMAND ----------

customerInsert_df = staged_df.join(customers_df,staged_df.CustomerKey_Upd == customers_df.CustomerKey)
display(customerInsert_df)

# COMMAND ----------

customerInsertFinal_df =customerInsert_df.select(
    customerInsert_df.CustomerKey_Upd.alias("CustomerKey"),
    customerInsert_df.Fullname_Upd.alias("Fullname"),
    customerInsert_df.EmailAddress_Upd.alias("EmailAddress"),
    customerInsert_df.Phone_Upd.alias("Phone"),
    customerInsert_df.StartDate,
    customerInsert_df.EndDate
).withColumn("IsActive",lit("Y"))
display(customerInsertFinal_df)

# COMMAND ----------

customerInsertFinal_df.write.mode("append").saveAsTable("Customers_SCD")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM Customers_SCD

# COMMAND ----------

#important for interview 