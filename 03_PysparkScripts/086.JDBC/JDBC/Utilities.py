# Databricks notebook source
server_name = "jdbc:sqlserver://mytrainingsqlserver.database.windows.net"
database_name = "mytrainingsqldb"
jdbcurl = server_name + ";" + "databaseName=" + database_name + ";"

# COMMAND ----------

sqlusername = dbutils.secrets.get("adbdevscope","sqlusername")
sqlpassword = dbutils.secrets.get("adbdevscope","sqlpassword")

# COMMAND ----------
#In order to save time we use template to run and fetch db data and write data to db. we can use the below functions to read data from database and write data to database. we can also specify the write mode when we write data to database using the WriteDataframeToDatabaseMode function.
def ReadTableFromDatabase(Tablename):
    try:
        df = (spark.read.format("jdbc")
        .option("url",jdbcurl)
        .option("username",sqlusername)
        .option("password",sqlpassword)
        .option("dbtable",Tablename).load()
        )
    except Exception as e:
        raise Exception    
    return df

# COMMAND ----------

def QueryFromDatabase(sqlquery):
    df = (spark.read.format("jdbc")
    .option("url",jdbcurl)
    .option("username",sqlusername)
    .option("password",sqlpassword)
    .option("query",sqlquery).load()
    )
    return df


# COMMAND ----------

def WriteDataframeToDatabase(dfName,Tablename):
    (dfName.write
    .format("jdbc")
    .option("url", jdbcurl) 
    .option("dbtable", Tablename)
    .option("user", sqlusername) 
    .option("password", sqlpassword) 
    .save()
        )

# COMMAND ----------

def WriteDataframeToDatabaseOverwrite(dfName,Tablename):
    (dfName.write.format("jdbc")
        .option("url",jdbcurl)
        .option("username",sqlusername)
        .option("password",sqlpassword)
        .mode("overwrite")
        .option("dbtable",Tablename).save()
        )

# COMMAND ----------

def WriteDataframeToDatabaseMode(dfName,Tablename,writemode):
    (dfName.write.format("jdbc")
        .option("url",jdbcurl)
        .option("username",sqlusername)
        .option("password",sqlpassword)
        .mode(writemode)
        .option("dbtable",Tablename).save()
        )

# COMMAND ----------

