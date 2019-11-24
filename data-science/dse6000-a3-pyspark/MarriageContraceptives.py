import pyspark
from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setAppName("MarriageAgeContraceptiveUse")
sc = SparkContext(conf = conf)

marriageLines = sc.textFile("hdfs://cluster-b435-m/wsu/age_of_marriage_flip.csv")
contraLines = sc.textFile("hdfs://cluster-b435-m/wsu/contraceptive_prevalence_flip.csv")

#marriageLines.take(5)
#contraLines.take(5)

#join the two datasets
rdd_marriage = sc.parallelize(marriageLines)
rdd_contra = sc.parallelize(contraLines)
#rdd_marriage.join(rdd_contra) (doesn't work)
#Pair RDD - both have years in column[0]
rdd_marriage2 = rdd_marriage.map(lambda line: (line.split(',')[0], line.split(',')[1]))
rdd_contra2 = rdd_contra.map(lambda line: (line.split(',')[0], line.split(',')[1]))
rdd_marriage2.join(rdd_contra2)

# Average age at marriage across all years in the US
filter1 = marriageLines.filter(lambda x: x[174] > 0)
filter1.reduce(lambda x, y: x + y, filter1[174]) / filter1.count()

# Average contraceptive prevalence (use) across all years in the US
filter2 = contraLines.filter(lambda x: x[174] > 0)
filter2.reduce(lambda x, y: x + y, filter2[174]) / filter2.count()

# Max age at marriage across all years in the US
maxagemarriage = filter1.map(lambda x: x[1]) \
	.max()

# Max contraceptive prevalence across all years in the US
maxcontra = filter2.map(lambda x: x[1]) \
	.max()

# Min age at marriage across all years in the US
minagemarriage = filter1.map(lambda x: x[1]) \
	.min()

# Min contraceptive prevalence across all years in the US
mincontra = filter2.map(lambda x: x[1])\
	.min()

# List years with highest age at marriage in the US
topyearsmarriage = filter1.filter(lambda x: x[1] == maxagemarriage) \
	.map(lambda x: x[0])
	.collect()

# List years with lowest age at marriage in the US
bottomyearsmarriage = filter1.filter(lambda x: x[1] == minagemarriage) \
	.map(lambda x: x[0])
	.collect()

# Country with highest age at marriage in the most recent year (2005)
marriageLines2005 = sc.textFile("hdfs://cluster-b435-m/wsu/age_of_marriage_2005.csv")
#marriageLines2005.take(5)
maxmarriage2005 = marriageLines2005.map(lambda x: x[1]) \
	.max()
topcountrymarriage2005 = marriageLines2005.filter(lambda x: x[1] == maxmarriage2005) \
	.map(lambda x: x[0])
	.collect()

# Country with highest contraceptive prevalence in the most recent year (2005)
contraLines2005 = sc.textFile("hdfs://cluster-b435-m/wsu/contraceptive_prevalence_2005.csv")
#contraLines2005.take(5)
maxcontra2005 = contraLines2005.map(lambda x: x[1]) \
	.max()
topcountrycontra2005 = contraLines2005.filter(lambda x: x[1] == maxcontra2005) \
	.map(lambda x: x[0])
	.collect()

