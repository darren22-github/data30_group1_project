import boto3
from pprint import pprint


def get_all_csv():
    s3_client = boto3.client('s3')
    bucket_name = 'data-eng-30-final-project-files'

    academy_file = s3_client.list_objects(Bucket=bucket_name, Prefix='Academy/')

    pprint(academy_file)

get_all_csv()