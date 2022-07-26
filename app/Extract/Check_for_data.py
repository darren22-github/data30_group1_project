from pprint import pprint
from s3_client import *

# def get_all_csv():
#     s3_client = boto3.client('s3')
#     bucket_name = 'data-eng-30-final-project-files'
#
#     academy_file = s3_client.list_objects(Bucket=bucket_name, Prefix='Academy/')
#
#     #pprint(academy_file)


def list_bucket(prefix = ""):
    # List objects in a bucket given a path, returns each key in a list

    objects = s3_client.list_objects(
        Bucket=bucket_name,
        Prefix=prefix
    )['Contents']

    return[i['Key'] for i in objects]

def list_talents(prefix = ''):

    list_talents =[]

    files = s3_client.list_objects_v2(Bucket=bucket_name,Prefix=prefix)['Contents']
    talent = filter(lambda x: x['Key'].endswith('.json'), files)
    for obj in talent:
        list_talents.append(obj['Key'])

    return talent

def list_applicants():
    # get  a list of applicant per month from the bucket
    applicant_list=[]
    months =['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']

    for month in months:
        files = s3_client.list_objects(Bucket=bucket_name,Prefix= f"Talent/{month}")['Contents']
        applicant_list.append(files[0]['Key'])

    pprint(applicant_list)
    return applicant_list


def difference_files(list1,list2):
    # Get the difference between the two lists provided
    return len(list1) - len(list2)

# def Check_new_files():

#list_applicants()
list_talents()
# get_all_csv()
# pprint(list_bucket())

