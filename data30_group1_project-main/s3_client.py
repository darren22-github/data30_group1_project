import boto3

bucket_name = 'data-eng-30-final-project-files'
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')