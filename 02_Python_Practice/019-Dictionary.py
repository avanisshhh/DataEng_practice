# Databricks notebook source
empdt = {"id":1,"name":"John","Salary":10000}


# COMMAND ----------

print(empdt)
#OP: {'id': 1, 'name': 'John', 'Salary': 10000}
# COMMAND ----------

type(empdt)
#OP: dict
# COMMAND ----------

empdt['id']
#OP: 1
# COMMAND ----------

empdt['name']
#OP: 'John'
# COMMAND ----------

empdt['salary'] =20000
#OP: KeyError: 'salary'
# COMMAND ----------

print(empdt)

# COMMAND ----------

empdt['Salary'] =20000
#OP: {'id': 1, 'name': 'John', 'Salary': 20000}
# COMMAND ----------

print(empdt)

# COMMAND ----------

empdt['city'] = "nyc"
#OP: {'id': 1, 'name': 'John', 'Salary': 20000, 'city': 'nyc'}
# COMMAND ----------

print(empdt)

# COMMAND ----------

"city" in empdt
#OP: True
# COMMAND ----------

"txt" in empdt
#OP: False

# COMMAND ----------

for i in empdt:
    print(i)
#OP: id, name, Salary, city
# COMMAND ----------

for i in empdt.values():
    print(i)
#OP: 1, 'John', 20000, 'nyc'
# COMMAND ----------

for i in empdt.keys():
    print(i)
#
# COMMAND ----------

for i,j in empdt.items():
    print(i,j)
#OP: id 1, name John, Salary 20000, city nyc
# COMMAND ----------

[]
{}
()
{k:v}

# COMMAND ----------

lst = list((1,2,3,4))
print(lst)

# COMMAND ----------

myset = set((1,2,3,4))
print(myset)

# COMMAND ----------

mytup=tuple((1,'john',100))
print(mytup)

# COMMAND ----------

mydt = dict({"id":1,"name":"john"})
print(mydt)

# COMMAND ----------

