import boto3
from pyspark.sql import SparkSession

# Initialize SparkSession with S3 configurations
spark = SparkSession.builder \
    .appName("Kaggle to S3") \
    .config("spark.hadoop.fs.s3a.access.key", "ASIAX5VOO2UPHVUZ6352") \
    .config("spark.hadoop.fs.s3a.secret.key", "sSb8F9Rbf0Va+1dEkNULzy/EnnhnUyOXpTzCKlcx") \
    .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
    .config("spark.hadoop.fs.s3a.connection.maximum", "100") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .getOrCreate()

# Define file path and S3 details
file_path = '/c/Users/shubhangi hande/my-data-project/dataset/games_dataset.csv'
s3_bucket = 'kaggle-shubh-data'
s3_output_path = "s3://kaggle-shubh-data/data/"

# Read the dataset into a PySpark DataFrame
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(file_path)

# Write the DataFrame to S3 in Parquet format
df.write.format("parquet").mode("overwrite").save(s3_output_path)

# Stop the Spark session
spark.stop()
