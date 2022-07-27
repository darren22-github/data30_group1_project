import csv

file_to_read = 'Jan2019Applicants.csv'

class DataCleaner:

    def __init__(self, rows=None):
        self.rows = rows


    def call_cleaning_function(self, column_number, data):

        if column_number in [1, 13]:
            return self.clean_name(data) 

        elif column_number in [8]:
            return self.clean_phone_number(data)

        elif column_number in [11]:
            return self.clean_invite_day(data)
        
        elif column_number in [12]:
            return self.clean_invite_day(data)

        else:
            return data

        

    def find_column_number(self, row, data):
        return row.index(data)

    def empty_to_null(self, data):
        data = 'null'
        return data

    def check_if_empty(self, data):
        if len(data) == 0:
            return True
        return False

    def clean_name(self, data):
        return data.title()

    def capitalise_string(self, data):
        return data.capitalize()

    def clean_phone_number(self, data):
        data = data.replace("-", "")
        data = data.replace("+44", "0")
        data = data.replace(" (", "")
        data = data.replace(") ", "")
        data = ''.join(data.split())

        return data

    def clean_degree(self, data):
        pass

    def clean_invite_day(self, data):
        cleaned_day = data.lstrip('0')
        return cleaned_day

    def clean_row(self, row):

        cleaned_row = []
        
        for data in row:

            if self.check_if_empty(data):  #If there is no value

                cleaned_data = self.empty_to_null(data)
                cleaned_row.append(cleaned_data)

            else:

                column_number = self.find_column_number(row, data)
                cleaned_data = self.call_cleaning_function(column_number, data)
                cleaned_row.append(cleaned_data)

def read_csv(filename):

    first_row = 1

    with open(filename) as f: 
 
        csv_file = csv.reader(f, delimiter=',')
        rows = list(csv_file)

        dc = DataCleaner(rows)

        rows_to_read = len(rows)  #CHANGE TO len(rows) to clean the entire table

        for i in range(first_row, rows_to_read):
            dc.clean_row(rows[i])

 
    f.close()


read_csv(file_to_read)


