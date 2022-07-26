import boto3
from pprint import pprint
import pandas as pd

def test_get_all_csv():
    s3_client = boto3.client('s3')
    bucket_name = 'data-eng-30-final-project-files'

    academy_file = s3_client.list_objects(Bucket=bucket_name, Prefix='Academy/')['Contents']

    pprint(academy_file)


def test_get_all_files():
    s3_client = boto3.client('s3')
    bucket_name = 'data-eng-30-final-project-files'

    talent_file = s3_client.list_objects(Bucket=bucket_name, Prefix='Talent/')['Contents']

    pprint(talent_file)


def test_read_csv():

    s3_client = boto3.client('s3')
    bucket_name = 'data-eng-30-final-project-files'

    academy_file = s3_client.get_object(
        Bucket=bucket_name,
        Key='Academy/Business_20_2019-02-11.csv'
    )['Body']

    convert_to_csv = pd.read_csv(academy_file)

    pprint(type(convert_to_csv))


def test_s3_connection():
    s3_client = boto3.client('s3')
    bucket_name = 'data-eng-30-final-project-files'

    status = s3_client.get_object(
        Bucket=bucket_name,
        Key='Academy/Business_20_2019-02-11.csv'
    )['ResponseMetadata']['HTTPStatusCode']

    assert status == 200


test_get_all_files()
test_get_all_csv()
test_read_csv()
test_s3_connection()