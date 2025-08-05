import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# This tells Glue which arguments to expect, JOB_NAME is required
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Your ETL code starts here
# For example, a simple print statement
print("Hello from AWS Glue job!")

# Commit the job to let Glue know it finished successfully
job.commit()