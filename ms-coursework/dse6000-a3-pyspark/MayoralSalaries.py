import pyspark
from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setAppName("SalaryAnalysis")
sc = SparkContext(conf = conf)

# Detroit Open Data file located https://data.detroitmi.gov/Government/Mayoral-Appointee-Salaries/fwu6-4nb5
lines = sc.textFile("hdfs://cluster-b435-m/wsu/Mayoral_Appointee_Salaries.csv")

#lines.take(5)

# Get total no. of mayoral employees
lines.count()

# Get total no. of distinct titles
sc.textFile("hdfs://cluster-b435-m/wsu/rows.csv")\
  .map(lambda line: (line.split(',')[2], line.split(',')[2]))\
  .distinct()\
  .count()

# How many departments are there?
sc.textFile("hdfs://cluster-b435-m/wsu/rows.csv")\
  .map(lambda line: (line.split(',')[3], line.split(',')[3]))\
  .distinct()\
  .count()

# Sum total city salaries paid to employees
lines.map(lambda x: float(x[4])).reduce(lambda a, b: a+b)

# Employees with annual salary >= $200,000
filter1 = lines.filter(lambda x: x[4] >= 200000)
filter1.count()

# Employees with annual salary >= $150,000
filter2 = lines.filter(lambda x: x[4] >= 150000)
filter2.count()

# Average total salary for police department
filter3 = lines.filter(lambda x: x[3] == "Police")
filter3.reduce(lambda x, y: x + y, filter3[3]) / filter3.count()

# How many departments receive ADDITIONAL GRANT SUPPORT?
filter4 = lines.filter(lambda x: x[6] > 0).count()

# Highest and lowest city salaries
highSal = lines.map(lambda x: x[4]) \
	.max()
lowSal = lines.map(lambda x: x[4]) \
	.min()

salFilter = lines.filter(lambda x: x[4])

# List individual with highest salary
topSal = salFilter.filter(lambda x: x[1] == highSal) \
	.map(lambda x: x[0])
	.collect()

# List individual with lowest salary
bottomSal = salFilter.filter(lambda x: x[1] == lowSal) \
	.map(lambda x: x[0])
	.collect()

