# Databricks notebook source
dbutils.widgets.help()

# COMMAND ----------

dbutils.widgets.text("txtcountry","")

# COMMAND ----------

dbutils.widgets.remove("txtcountry")

# COMMAND ----------

dbutils.widgets.text("txtcountry","India","Country")
#we have created a text widget with the name txtcountry and default value as India and label as Country. we can use this widget to get the input from the user and use it in our code.

# COMMAND ----------

country = dbutils.widgets.get("txtcountry")
print(country)

# COMMAND ----------

dbutils.widgets.combobox("cboCountry","",["india","uk","us"],"Country")
#we have created a combo box widget with the name cboCountry and default value as empty and values as india, uk and us and label as Country. we can use this widget to get the input from the user and use it in our code.

# COMMAND ----------

cnt = dbutils.widgets.get("cboCountry")
print(cnt)

# COMMAND ----------

dbutils.widgets.dropdown("dropCountry","india",["india","uk","us"],"Country2")
#we have created a dropdown widget with the name dropCountry and default value as india and values as india, uk and us and label as Country2. we can use this widget to get the input from the user and use it in our code.
#here we have to select one default value 

# COMMAND ----------

cnt = dbutils.widgets.get("dropCountry")
print(cnt)

# COMMAND ----------

dbutils.widgets.multiselect("multiCountry","india",["india","uk","us"],"Country3")
#we have created a multiselect widget with the name multiCountry and default value as india and values as india, uk and us and label as Country3. we can use this widget to get the input from the user and use it in our code. here we can select multiple values from the list and it will return the selected values as a comma separated string.
# COMMAND ----------

cnt = dbutils.widgets.get("multiCountry")
print(cnt)

# COMMAND ----------

dbutils.widgets.removeAll()

# COMMAND ----------


