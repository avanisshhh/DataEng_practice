# Databricks notebook source
from pyspark.sql.types import * 

# COMMAND ----------

schema = StructType([ 
    StructField("EnglishProductName",StringType(),True), 
    StructField("Color", ArrayType(StringType()), True),
    StructField("Description",MapType(StringType(),StringType()),True)
  ])
#True → Column can contain NULL values

# COMMAND ----------

data= [
('LL Crankarm',	['Red','Green','Blue']	,{'Active':'Yes','Price':1289,'Qty':10}),
('ML Crankarm',	['Red','Blue'],	{'Active':'Yes','Price':1879,'Qty':29}),
('HL Crankarm',	['Red','Green','Blue']	,{'Active':'Yes','Price':2289,'Qty':100}),
('Chainring Bolts',	['Red','Green'],	{'Active':'No','Price':1299,'Qty':20}),
('Chainring Nut',	None,	{'Active':'Yes','Price':1889,'Qty':70}),
('Chainring',	['Red','Green','Blue'],	{'Active':'Yes','Price':289,'Qty':20}),
('Freewheel',	['Yellow','Green','Blue'],	{'Active':'No','Price':373,'Qty':30}),
('Front Derailleur Cage',	['Red','Silver','Blue']	,{'Active':'Yes','Price':199,'Qty':100}),
('Front Derailleur Linkage',	['Black','Green','Blue'],None)
]


# COMMAND ----------

df = spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

from pyspark.sql.functions import * 

# COMMAND ----------
'''
explode (and explode_outer) is used when you have a column containing arrays or maps, and you want to convert each element into a separate row.
'''
df2=df.select("EnglishProductName",explode("Color").alias("Color"))
display(df2)
#It breaks array elements into multiple rows
# COMMAND ----------

df2=df.select("EnglishProductName",explode_outer("Color").alias("Color"))
#explode_outer is used to keep rows even if the array is null here we are keeping the rows with null values in color column in the specified dataframe
display(df2)

# COMMAND ----------

df3=df.select("EnglishProductName",explode("Description"))
display(df3)          

# COMMAND ----------

df3=df.select("EnglishProductName",explode_outer("Description"))
#Keeps rows even if array is null
display(df3)          

# COMMAND ----------

df2=df.select("EnglishProductName",posexplode("Color"))
display(df2)
#It not only splits the array into rows, but also gives the index (position) of each element.

# COMMAND ----------

df2=df.select("EnglishProductName",posexplode("Description"))
display(df2)

# COMMAND ----------

df2=df.select("EnglishProductName",posexplode_outer("Color"))
display(df2)
'''
Adds position (index) (like posexplode)
Keeps rows even if array is NULL (like explode_outer)
#pos like 0 1 2 , 0 1, Null like that

'''

# COMMAND ----------

