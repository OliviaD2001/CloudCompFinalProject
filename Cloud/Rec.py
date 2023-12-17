from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("movielens").getOrCreate()

# dataset shows userID, movieID, rating & timestamp
data = spark.read.csv("/Users/oliviaduong/Downloads/Cloud/ml-latest-small/ratings.csv", inferSchema = True, header = True)

data.head()

# shows count of ratings: 100836
# shows userIDs: : 100836
data.describe().show()

(training, test) = data.randomSplit([0.8, 0.2])

# Build the recommendation model using ALS on the training data
als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating")
model = als.fit(training)

predictions = model.transform(test)

predictions.show()

evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print("Root-mean-square error = " + str(rmse))

single_user = test.filter(test['userId']==11).select(['movieId','userId','rating'])
single_user.show()

recommendations = model.transform(single_user)
recommendations.orderBy('prediction',ascending=False).show()