#3. Shuffle Hash Join: This strategy is used when both tables in the join are large and cannot fit in memory. In this strategy, the data from both tables is shuffled across the network based on the join keys, and the join is performed on the shuffled data. This can be less efficient than broadcast join, as it involves shuffling data across the network, but it can handle larger datasets.


'''
A Shuffle Hash Join is a join where:

Both DataFrames are shuffled on the join key
One side is converted into a hash table
Other side is used to probe that hash table

🔹 How it works internally
Step by step:
1. Shuffle
Spark redistributes both DataFrames based on join key
Same keys go to same partition
2. Build Phase (Important ⚠️)
Spark picks one side (usually smaller)
Creates an in-memory hash table
3. Probe Phase
Other DataFrame rows are scanned
For each row:
Spark checks hash table
Finds match quickly (O(1))



👉 This ensures matching rows land on same executor

Spark uses SHJ when:
✔ spark.sql.join.preferSortMergeJoin = false
✔ One side is small enough to fit in memory (but not broadcast)
✔ Join keys are suitable


'''


spark.conf.set("spark.sql.join.preferSortMergeJoin", "false")

df.join(df2, "id")