# Databricks notebook source
# DBTITLE 1,GroupBykey
#GroupBykey called on a dataset of (K, V) pairs, returns a dataset of (K, Iterable<V>) pairs.
rdd = spark.sparkContext.parallelize((("John",1),("Hary",3),("John",4),("Hary",2),("Mike",5),("Hary",6)))  
rdd_collect = rdd.collect()

# COMMAND ----------

rdd.groupByKey().collect()

# COMMAND ----------

rdd1=rdd.groupByKey().mapValues(sum)
rdd1.collect()

# COMMAND ----------

rdd.lookup("John")

# COMMAND ----------

# DBTITLE 1,ReduceByKey
#In ReduceByKey called on a dataset of (K, V) pairs, returns a dataset of (K, V) pairs where the values for each key are aggregated using the given reduce function func, which must be of type (V,V) => V. Like in groupByKey
data = sc.parallelize([("a", 1), ("b", 1), ("a", 2),("b",5),("c",9),("c",7)])
data.collect()

# COMMAND ----------

data.reduceByKey(lambda x,y:x+y).collect()

# COMMAND ----------

# DBTITLE 1,what is the difference between groupbykey and reducebykey?
#reduceByKey performs map side combine which reduces the amount of data sent over the network during shuffle and thereby also reduces the amount of data reduced.
#In GroupByKey the data is not combined or reduced on the map side, we transferred all elements over the network during shuffle.
#In GroupByKey elements are sent to the task performing the aggregate operation, the number of elements to be handled by the task will be more and could possibly result in an Out of Memory exception
#Data suffline in reduceByKey is less that's why preffered reduceByKey.

# COMMAND ----------

data.reduceByKey(max).collect()

# COMMAND ----------

data.reduceByKey(min).collect()

# COMMAND ----------

# DBTITLE 1,Sortbykey
#When called on a dataset of (K, V) pairs where K implements Ordered, returns a dataset of (K, V) pairs sorted by keys in ascending or descending orde
datas = sc.parallelize([("a", 1), ("b", 1), ("a", 2),("b",5),("c",9),("c",7)])

# COMMAND ----------

datas.sortByKey().collect()

# COMMAND ----------

# DBTITLE 1,Aggregate By Key
#In this case we can perform two different operation combinely like count and sum for this we will perform sequence operation and then follwed by combine operation
#it takes 3 argument intialize,sequence,combine operation and give output in the form of combining all

ipl=sc.parallelize([("csk", 1), ("mi", 1), ("csk", 2),("mi",5),("rcb",9),("csk",7)])
ipl.collect()

# COMMAND ----------

seqFunc = (lambda x, y: (x[0] + y, x[1] + 1))
combFunc = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
sorted(ipl.aggregateByKey((0, 0), seqFunc, combFunc).collect())

# COMMAND ----------


