# Databricks notebook source
nums = [1,2,3,4,5]
print(nums)

# COMMAND ----------

dblnums = []
for i in nums:
    dblnums.append(i*2)
dblnums

# COMMAND ----------

nums2 = [i for i in nums]
print(nums2)

# COMMAND ----------

nums2 = [i*2 for i in nums]
print(nums2)

# COMMAND ----------

sqnums = [i*i for i in nums]
print(sqnums)

# COMMAND ----------

countries = ["india","uk","us"]
print(countries)

# COMMAND ----------

cnt2 = [j.upper() for j in countries]
print(cnt2)
#OP: ['INDIA', 'UK', 'US']
# COMMAND ----------

dblst = [i for i in [1,2,3,4]]
print(dblst)

# COMMAND ----------

dblst = [i*2 for i in range(0,10)]
print(dblst)
#OP: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# COMMAND ----------

dblst = [i*2 for i in range(0,10) if i<6]
print(dblst)
#OP: [0, 2, 4, 6, 8, 10]
# COMMAND ----------

dblst = [i*2 for i in range(0,10) if i>=6 and i<=8]
print(dblst)
#OP: [12, 14, 16]
# COMMAND ----------

x = "hello"
print(x)

# COMMAND ----------

y = [i for i in x]
print(y)

# COMMAND ----------

a = "1a2b3cd"
print(a)

# COMMAND ----------

numbers = [int(i) for i in a if i.isnumeric()]
print(numbers)
#OP: [1, 2, 3]
# COMMAND ----------

numbers = [i for i in a if i.isnumeric()]
numsonly = int("".join(numbers))
print(numsonly)
type(numsonly)
#OP: 123
#--we can use the join() method to concatenate the list of numeric characters into a single string, and then convert that string to an integer using the int() function

# COMMAND ----------

alphas = [i for i in a if i.isalpha()]
print(alphas)

# COMMAND ----------

alphas = [i for i in a if i.isalpha()]
aphasonly = "".join(alphas)
print(aphasonly)
#OP: "abcd"
# COMMAND ----------

alphas = [i for i in a if i.isalpha()]
aphasonly = "-".join(alphas)
print(aphasonly)
#OP: "a-b-c-d"

# COMMAND ----------

