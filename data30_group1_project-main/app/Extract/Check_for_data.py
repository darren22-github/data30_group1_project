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


def list_talents(prefix=''):
    list_talents = []

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
    applicant_list = []
    months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

    for month in months:
        files = s3_client.list_objects(Bucket=bucket_name, Prefix=f"Talent/{month}")['Contents']
        applicant_list.append(files[0]['Key'])
    #pprint(applicant_list)
    return applicant_list


def list_courses():
    courses_list = []
    # courses = ['Business','Data','Engineering']

    object_keys = list_bucket()
    c_list = filter(lambda x: x.startswith('Academy/'), object_keys)
    for obj in c_list:
        courses_list.append(obj)
    #pprint(courses_list)
    return courses_list


# EXTRACT OBJECTS
def extract_object(key):
    obj = s3_client.get_object(Bucket=bucket_name, Key=key)
    return obj


# EXTRACT TALENT
def extract_talent(key):
    obj = extract_object(key)
    return json.load(obj['Body'])



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
        extract_applicant(a)


# EXTRACT SPARTA DAY
def extract_sparta_day(key):
    obj = extract_object(key)
    obj_sparta_day = []
    # obj = obj['Body'].read()
    for line in obj['Body'].iter_lines():
        obj_sparta_day.append(line.decode('utf-8'))

    return obj_sparta_day


def extract_all_sparta_day():
    for a in list_spartaday():
        extract_sparta_day(a)


# EXTRACT ACADEMY
def extract_course(key):
    obj = extract_object(key)
    df = pd.read_csv(obj['Body'])

    return df


def extract_all_courses():
    for a in list_courses():
        extract_course(a)


def difference_files(list1, list2):
    # Get the difference between the two lists provided
    return len(list1) - len(list2)


# def Check_new_files():
#   Use the last modified attribute to add new files?
# my_bucket = s3_resource.Bucket('data-eng-30-final-project-files')
# for i in my_bucket.objects.all():
#     print(str(i.last_modified)[:16])



##########
## Alex & Darren Testing ##
##########
# list_spartaday()
# list_applicants()
# extract_talent('Talent/10445.json')
# extract_all_talent()
# extract_all_applicants()

# list_courses()
# pprint(extract_course('Academy/Business_20_2019-02-11.csv'))
# extract_all_sparta_day()
# extract_all_courses()
#extract_all_courses()
