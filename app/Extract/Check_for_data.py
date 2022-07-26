from pprint import pprint
from s3_client import *
import json
import pandas as pd
import csv

#   List the contents of the 'data-eng-30-final-project-files' bucket
def list_bucket():
    bucket = s3_resource.Bucket('data-eng-30-final-project-files')
    object_keys = []

    for i in bucket.objects.all():
        object_keys.append(i.key)

    return object_keys
    # List objects in a bucket given a path, returns each key in a list

    # AWS_BUCKET_PREFIX = 'Talent/Sparta'
    # bucket_contents = s3_client.list_objects(Bucket=bucket_name)
    # for file in bucket_contents["Contents"]:
    #     file_name = file["Key"]
    #     pprint(file_name)
    #
    # obj = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    # body = obj["Body"]
    # acad = pd.read_table(body)
    # pprint(acad)

def list_talents(prefix = ''):
    list_talents =[]

    object_keys = list_bucket()
    talents = filter(lambda x: x.endswith('.json'), object_keys)
    for obj in talents:
        list_talents.append(obj)

    # list_talents_extended = []
    # [list_talents_extended.extend(i) for i in list_talents]

    return list_talents


def list_spartaday(prefix=''):
    list_spartaday = []

    object_keys = list_bucket()
    spartaDay = filter(lambda x: x.endswith('.txt'), object_keys)
    for obj in spartaDay:
        list_spartaday.append(obj)

    return list_spartaday


def list_applicants():
    # get  a list of applicant per month from the bucket
    applicant_list=[]
    months =['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']

    for month in months:
        files = s3_client.list_objects(Bucket=bucket_name,Prefix= f"Talent/{month}")['Contents']
        applicant_list.append(files[0]['Key'])
    pprint(applicant_list)
    return applicant_list


# EXTRACT OBJECTS
def extract_object(key):
    obj = s3_client.get_object(Bucket=bucket_name,Key=key)
    return obj

# EXTRACT TALENT
def extract_talent(key):
    obj = extract_object(key)
    pprint(json.load(obj['Body']))
    #ADD RETURN

def extract_all_talent():

    for t in list_talents():
        extract_talent(t)

# EXTRACT APPLICANT
def extract_applicant(key):
    obj = extract_object(key)
    df = pd.read_csv(obj['Body'])

    return df

def extract_all_applicants():

    for a in list_applicants():
        print(extract_applicant(a))


def difference_files(list1, list2):
    # Get the difference between the two lists provided
    return len(list1) - len(list2)

# def Check_new_files():







#list_spartaday()
#list_applicants()
#extract_talent('Talent/10445.json')
#extract_all_talent()
#extract_all_applicants()





