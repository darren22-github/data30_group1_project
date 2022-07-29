import boto3
from pprint import pprint
import pandas as pd
# from app.Extract.s3_client import *
# from app.Extract.Check_for_data import list_bucket




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

#----------------------------------------------------------------
#Final Testing

def test_list_bucket():
    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket('data-eng-30-final-project-files')
    object_keys = []

    for i in bucket.objects.all():
        object_keys.append(i.key)

    assert len(object_keys) == 3305
    return object_keys

def test_list_talents():
    list_talents = []

    object_keys = test_list_bucket()
    talents = filter(lambda x: x.endswith('.json'), object_keys)
    for obj in talents:
        list_talents.append(obj)

    assert len(list_talents) ==3105
    return list_talents

def test_list_spartaday():
    list_spartaday = []

    object_keys = test_list_bucket()
    spartaDay = filter(lambda x: x.endswith('.txt'), object_keys)
    for obj in spartaDay:
        list_spartaday.append(obj)

    assert list_spartaday[1] == 'Talent/Sparta Day 1 May 2019.txt'
    assert len(list_spartaday) == 152
    return list_spartaday