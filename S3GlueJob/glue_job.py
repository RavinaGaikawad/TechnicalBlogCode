import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

def main():
    job = Job(glueContext)
    job.init(args['JOB_NAME'], args)
    
    # path/to/your/file.csv
    csv_file_s3_uri = "s3://user-locations/users.csv"
    # read the parquet file into a dataframe
    csv_df = spark.read.csv(csv_file_s3_uri, header=True, inferSchema=True)
    # Show the DataFrame
    csv_df.show()
    
    
    # path/to/your/file.parquet
    parquet_file_s3_uri = "s3://user-locations/users.parquet"
    # read the parquet file into a dataframe
    parquet_df = spark.read.parquet(parquet_file_s3_uri)
    # Show the DataFrame
    parquet_df.show()
    
    job.commit()

if __name__ == "__main__":
    main()
    