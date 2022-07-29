import csv
import pandas as pd

file_to_read1 = 'Jan2019Applicants.csv' #This is the file that gets cleaned

class DataCleaner:

    def __init__(self, rows=None):
        self.rows = rows

    def call_cleaning_function(self, column_number, data):

        if column_number in [1, 13]:
            return self.clean_name(data) 

        elif column_number in [3]:
            return self.clean_dob(data)

        elif column_number in [8]:
            return self.clean_phone_number(data)

        elif column_number in [11]:
            return self.clean_invite_day(data)
        
        elif column_number in [12]:
            return self.clean_invite_month(data)

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

        if len(data) < 15:
            return 'null'

        data = data.replace("-", "")
        data = data.replace("+44", "0")
        data = data.replace(" (", "")
        data = data.replace(") ", "")
        data = ''.join(data.split())

        return data

    def clean_invite_day(self, data):
        if len(data) == 1:
            data = "0" + str(data)
        return data

    def clean_invite_month(self, month):
        month_dict = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        month_name = month[:3]
        year = month[3:]
        month_name = month_dict[month_name]
        cleaned_month = month_name + year
        return cleaned_month

    def merge_invite_date(self, day, month):
        if day == "null" or month == "null":
            return "null"
        return day + "-" + month

    def clean_dob(self, data):
        return data.replace("/", "-")

    def convert_date_to_correct_format(self, date): #converts dd/mm/yy to YYYY/MM/DD

        if date == 'null':
            return 'null'

        split_date = date.split("-")
        if len(split_date[2]) == 2:
            split_date[2] = "20" + split_date[2]
            
        correct_format_date = split_date[2] + '-' + split_date[1] + '-' + split_date[0]
        return correct_format_date

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

        return cleaned_row

def read_csv(filename):

    cleaned_table = []

    first_row = 1

    with open(filename) as f: 
 
        csv_file = csv.reader(f, delimiter=',')
        rows = list(csv_file)

        dc = DataCleaner(rows)

        rows_to_read = len(rows)

        for i in range(first_row, rows_to_read):
            cleaned_row = dc.clean_row(rows[i])
            cleaned_table.append(cleaned_row)

    for row in cleaned_table: #The date is merged and cleaned in this for loop
        merged_date = dc.merge_invite_date(row[11], row[12])
        del row[11]
        del row[11]
        row.insert(11, merged_date)

        row[3] = dc.convert_date_to_correct_format(row[3])
        row[11] = dc.convert_date_to_correct_format(row[11])

    f.close()
    return cleaned_table

def convert_lists_to_df(data):
    
    df = pd.DataFrame(data, columns=["id", "name", "gender", "dob", "email", "city", "address", "postcode", 
    "phone_number", "uni", "degree", "invited_date", "invited_by"])

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    return df


cleaned_data = read_csv(file_to_read1)
df = convert_lists_to_df(cleaned_data)

df.to_csv('Jan2019ApplicantsCleaned.csv', index=False)


