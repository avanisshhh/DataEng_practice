spark.conf.get("spark.sql.join.preferSortMergeJoin")

'''
➡️ Spark will prefer Sort Merge Join (SMJ) for large joins
➡️ Even if other joins (like shuffle hash join) are possible

🔹 What is Sort Merge Join (SMJ)?

Sort Merge Join works like this:

Shuffle both DataFrames based on join key
Sort both sides
Merge them like merge step in merge sort



How it relates to Broadcast Join
If table is small → Spark uses Broadcast Join
If tables are large → Spark uses Sort Merge Join (because this config = true)


'''




spark.conf.set("spark.sql.join.preferSortMergeJoin", "false")


'''
👉 Now Spark may choose:
Shuffle Hash Join
Instead of Sort Merge Join (if conditions fit)


How Spark decides join strategy?”

Check broadcast threshold
If not broadcast:
If preferSortMergeJoin = true → SMJ
Else → Shuffle Hash Join (if possible)
'''