# Databricks notebook source
salesdf = (spark.read.format("csv")
.option("path","/FileStore/tables/Sales.csv")
.option("header",True)
.option("inferSchema",True)
.load())
display(salesdf)

# COMMAND ----------

productsdf = (spark.read.format("csv")
.option("path","/FileStore/tables/ProductsNew.csv")
.option("header",True)
.option("inferSchema",True)
.load())
display(productsdf)

# COMMAND ----------

help(salesdf.join)

# COMMAND ----------

joindf = salesdf.join(productsdf) #cross join by default

display(joindf)

# COMMAND ----------

joindf2 = salesdf.join(productsdf,salesdf.ProductKey == productsdf.ProductKey)
#Type of join here is inner join by default when we specify the join condition explicitly using the join method and it will return only the rows which have matching values in both dataframes based on the condition specified in the join method. here we are joining sales dataframe and products dataframe based on the condition that ProductKey in sales dataframe should be equal to ProductKey in products dataframe and it will return only the rows which have matching values in both dataframes. when we do not specify the join condition explicitly using the join method and it will return the cartesian product of both dataframes which means it will return all the possible combinations of rows from both dataframes

#we can also specify the join condition explicitly using the join method and it will return the same result as the default join. here we are joining sales dataframe and products dataframe based on the condition that ProductKey in sales dataframe should be equal to ProductKey in products dataframe and it will return only the rows which have matching values in both dataframes.
display(joindf2)

# COMMAND ----------

joindf3 = salesdf.join(productsdf,salesdf.ProductKey == productsdf.ProductKey,"inner")
display(joindf3)

# COMMAND ----------

joindf3 = salesdf.join(productsdf,salesdf.ProductKey == productsdf.ProductKey,"left")
display(joindf3)

# COMMAND ----------

joindf3 = salesdf.join(productsdf,salesdf.ProductKey == productsdf.ProductKey,"right")
display(joindf3)

# COMMAND ----------

joindf3 = salesdf.join(productsdf,salesdf.ProductKey == productsdf.ProductKey,"leftanti")
#leftanti join is used to get the rows from left dataframe which do not have matching values in right dataframe here we are getting the rows from sales dataframe which do not have matching values in products dataframe based on ProductKey column
display(joindf3)

# COMMAND ----------

joindf3 = salesdf.join(productsdf,salesdf.ProductKey == productsdf.ProductKey,"leftsemi")
#leftsemi join is used to get the rows from left dataframe which have matching values in right dataframe here we are getting the rows from sales dataframe which have matching values in products dataframe based on ProductKey column
display(joindf3)

# COMMAND ----------

customerdf = (spark.read.format("csv")
.option("path","/FileStore/tables/Customers.csv")
.option("header",True)
.option("inferSchema",True)
.load())
display(customerdf)

# COMMAND ----------

joindf3 = salesdf.join(productsdf,salesdf.ProductKey == productsdf.ProductKey,"inner").join(customerdf,salesdf.CustomerKey == customerdf.CustomerKey,"inner")
display(joindf3)

# COMMAND ----------

joindf3 = salesdf.join(productsdf,salesdf.ProductKey == productsdf.ProductKey,"left").drop(productsdf['ProductKey'])
#drop() method is used to drop the column from the dataframe here we are dropping the ProductKey column from products dataframe after joining it with sales dataframe based on ProductKey column and left join is used to get all the rows from left dataframe and matching rows from right dataframe here we are getting all the rows from sales dataframe and matching rows from products dataframe based on ProductKey column
display(joindf3)

# COMMAND ----------

salesmultidf = (spark.read.format("csv")
.option("path","/FileStore/tables/SalesMulti.csv")
.option("header",True)
.option("inferSchema",True)
.load())
display(salesmultidf)

# COMMAND ----------

productsmultidf = (spark.read.format("csv")
.option("path","/FileStore/tables/ProductsMulti.csv")
.option("header",True)
.option("inferSchema",True)
.load())
display(productsmultidf)

# COMMAND ----------

joindfmulti = salesmultidf.join(productsmultidf,["ProductId","Country"],"inner")
#when we have multiple columns in the join condition we can pass the list of columns in the join method and it will return the same result as the default join. here we are joining salesmultidf dataframe and productsmultidf dataframe based on the condition that ProductId and Country in salesmultidf dataframe should be equal to ProductId and Country in productsmultidf dataframe and it will return only the rows which have matching values in both dataframes based on ProductId and Country columns
display(joindfmulti)

# COMMAND ----------

productsmultidf2= productsmultidf.withColumnRenamed("ProductId","ProductKey")
#Renames the column ProductId → ProductKey
display(productsmultidf2)

# COMMAND ----------

joindfmulti = salesmultidf.join(productsmultidf2,(salesmultidf.ProductId == productsmultidf2.ProductKey) & (salesmultidf.Country == productsmultidf2.Country),"inner")
display(joindfmulti)

# COMMAND ----------

joindfmulti = salesmultidf.join(productsmultidf2,(salesmultidf.ProductId == productsmultidf2.ProductKey) & (salesmultidf.Country == productsmultidf2.Country),"inner").drop("ProductKey",productsmultidf2['Country'])
display(joindfmulti)

# COMMAND ----------


