# Databricks notebook source
def printmessage(empname):
    print(empname)

# COMMAND ----------

printmessage("john")

# COMMAND ----------

def addnumbers(x,y):
    print(x+y)

# COMMAND ----------

addnumbers(10,20)

# COMMAND ----------

def EmpDetails(empid,empname,city="London"):
    print(empid)
    print(empname)
    print(city)


# COMMAND ----------

EmpDetails(1,"john")

# COMMAND ----------

EmpDetails(1,"john","nyc")

# COMMAND ----------

def EmpDetails2(city="London",empid,empname):
    print(empid)
    print(empname)
    print(city)
#Issue with above function is that default parameter should be at the end of the parameter list.

# COMMAND ----------

def add(*args):
    print(sum(args))
#*args is used to pass a variable number of non-keyword arguments to a function. It allows you to pass any number of arguments to the function, and they will be accessible as a tuple within the function.
# COMMAND ----------

def add(*a):
    print(sum(a))

# COMMAND ----------

add(10)

# COMMAND ----------

add(10,20)

# COMMAND ----------

add(20,303,40,30)

# COMMAND ----------

'''
👉 Function parameters order (*args, default args, **kwargs)
1. *args should be at the beginning of the parameter list.
2. Default parameters should be after *args.
3. **kwargs should be at the end of the parameter list.'''

def EmpDetails3(empname,city="London",*a):
    print(empname)
    print(city)
    print(sum(a))

# COMMAND ----------

EmpDetails3("john","delhi",10)

# COMMAND ----------

EmpDetails3("john","delhi",10,20)

# COMMAND ----------

EmpDetails3("john",,10)

# COMMAND ----------

def EmpDetails3(empname,*a,city="London"):
    print(empname)
    print(city)
    print(sum(a))

# COMMAND ----------

EmpDetails3("john",10,20)

# COMMAND ----------

EmpDetails3("john",10,20,city="nyc")

# COMMAND ----------

def EmpDetails4(**kwargs):
    print(kwargs)

# COMMAND ----------

EmpDetails4(empid = 1,empname="john",city="nyc")

# COMMAND ----------

def EmpDetails4(**kwargs):
    print(kwargs.values())

# COMMAND ----------

EmpDetails4(empid = 1,empname="john",city="nyc")

# COMMAND ----------

def EmpDetails(Empid,Empname,*args,city="nyc",**kwargs):
    print(Empid)
    print(Empname)
    print(sum(args))
    print(kwargs)
#**kwargs allows you to pass multiple key-value pairs 
# COMMAND ----------

EmpDetails(1,"john",10,30,city="delhi",salary=10000,contact=192929)

# COMMAND ----------

