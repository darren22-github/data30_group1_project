
import csv
from tkinter.tix import Tree

from sqlalchemy import null
file_to_read = 'Jan2019Applicants.csv'

class DataCleaner:

    def find_column_number(self, row, data):
        return row.index(data)

    def __init__(self, rows=None):
        self.rows = rows

    def empty_to_null(self, data):
        data = None

    def check_if_empty(self, data):
        if data == "":
            return True
        return False

    def clean_name(self, data):
        pass

    def clean_phone_number(self, data):
        pass

    def clean_degree(self, data):
        pass

    def clean_invite_date(self, day, month):
        pass

    def clean_row(self, row):

        cleaned_row = []
        
        for data in row:

            if self.check_if_empty:  #If there is no value
                cleaned_data = self.empty_to_null(data)
                cleaned_row.append(cleaned_data)

            else:
                self.find_column_number(row, data)


def read_csv(filename):

    first_row = 1

    with open(filename) as f: 
 
        csv_file = csv.reader(f, delimiter=',')
        rows = list(csv_file)

        dc = DataCleaner(rows)

        rows_to_read = 10  #CHANGE TO len(rows) to clean the entire table

        for i in range(first_row, rows_to_read):
            dc.clean_row(rows[i])

 
    f.close()


read_csv(file_to_read)


