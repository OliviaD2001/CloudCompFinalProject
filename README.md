# Entertainment Recommendation System: Personalized Movie Engine Powered by Apache Spark 
### Cloud Computing & Big Data Fall 2023

## Dataset
MovieLens: https://grouplens.org/datasets/movielens/
<br>
Small: 100,000 ratings and 3,600 tag applications applied to 9,000 movies by 600 users. Last updated 9/2018.

## Collaborative Filtering | Movie Rating Prediction
Collaborative filtering is based on combo of relevant user’s and other users’ behaviors to make predictions.

## Directory Path
Ensure to change directory in line 9 of Rec.py to your dataset path. 
<br>
It is currently set to 
  data = spark.read.csv("/Users/oliviaduong/Downloads/Cloud/ml-latest-small/ratings.csv", inferSchema = True, header = True).

## Execute Code
python Rec.py
