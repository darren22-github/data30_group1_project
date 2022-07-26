import csv

file_to_read = 'Jan2019Applicants.csv'

class DataCleaner:

    def __init__(self, rows=None):
        self.rows = rows

    def find_column_number(self, row, data):
        return row.index(data)

    def empty_to_null(self, data):
        data = None

    def check_if_empty(self, data):
        if len(data) == 0:
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

            if self.check_if_empty(data):  #If there is no value

                print("empty")

                cleaned_data = self.empty_to_null(data)
                cleaned_row.append(cleaned_data)

            else:

                print("not empty")

                column_number = self.find_column_number(row, data)

def read_csv(filename):

    first_row = 1

    with open(filename) as f: 
 
        csv_file = csv.reader(f, delimiter=',')
        rows = list(csv_file)

        dc = DataCleaner(rows)

        rows_to_read = 10  #CHANGE TO len(rows) to clean the entire table

        for i in range(first_row, rows_to_read):
            #print(rows[i])
            dc.clean_row(rows[i])

 
    f.close()


read_csv(file_to_read)


