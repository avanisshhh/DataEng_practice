# Databricks notebook source
rdd1 = sc.parallelize([1,2,3,4,5,6,7,8,9,10])
rdd1.collect()

rdd1.getNumPartitions()




rdd1.glom().collect()

#
help(rdd1.coalesce)
#coalesce()  used to reduce the number of partitions in an RDD and it takes the number of partitions as an argument and it returns a new RDD with the specified number of partitions

#
rdd2=rdd1.coalesce(4)


#
rdd2.collect()

#
rdd2.glom().collect()

#
[[1], [2], [3], [4, 5], [6], [7], [8], [9, 10]]

#
rdd3=rdd1.coalesce(10)
#
rdd3.glom().collect()

#
help(rdd1.repartition)
#repartition() function is used to increase or decrease the number of partitions in an RDD and it takes the number of partitions as an argument and it returns a new RDD with the specified number of partitions and 

# it shuffles the data in the RDD to redistribute the data in the new partitions

#
rdd4 = rdd1.repartition(4)
rdd4.collect()

#
rdd4.glom().collect()

#
rdd5=rdd1.repartition(16)
rdd5.collect()

#
rdd5.glom().collect()

#
