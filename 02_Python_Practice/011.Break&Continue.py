# Databricks notebook source
for i in range(1,11):
    if i <6:
        print(i)

# COMMAND ----------

for i in range(1,11):
    print(f"Loop: {i}")
    if i <6:
        print(i)
        
# Loop: 1
# 1
# Loop: 2
# 2
# Loop: 3
# 3
# Loop: 4
# 4
# Loop: 5
# 5
# Loop: 6
# Loop: 7
# Loop: 8
# Loop: 9
# Loop: 10
                 
# COMMAND ----------

for i in range(1,11):
    
    if i <=5:
        print(i)
    else:
        break   
    print(f"Loop: {i}") 

# COMMAND ----------

for i in range(1,11):
    print(f"Loop: {i}") 
    if i <=5:
        print(i)
        continue
    else:
        break   
    

# COMMAND ----------

i = 0

while i < 10:
    i += 1
    if i < 6:
        print(i)
    else:
        break

# COMMAND ----------

