import csv  # Importing csv file
from io import StringIO

import pandas as pd

file_to_read = 'Jan2019Applicants.csv'  # Name of the sample csv to clean


# Function that takes in a row (as a list) and data (elements within the row) and returns the index of the element
# depending on the index, the method 'call_cleaning function' will carry out the appropriate transformation
def find_column_number(row, data):
    return row.index(data)


class DataCleaner:  # Class that takes in each row of a csv file and clean it

    # Initilisation method that takes in a list of rows as an argument
    def __init__(self, rows=None):
        self.rows = rows


    # Call cleaning function that cleans data according to its index (column_number).
    # Each column number corresponds to a column title, and the data is cleaned by calling
    # the appropriate functions located within the class
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

    # Method that changes empty values(data argument) to the string null
    def empty_to_null(self, data):
        data = 'null'
        return data

    # Method that checks if there are empty values(data)
    def check_if_empty(self, data):
        if len(data) == 0:
            return True
        return False

    # Method that cleans values(data) in the name (column_number = 1) and invited_by (column_number = 3) columns
    def clean_name(self, data):
        return data.title()

    def capitalise_string(self, data):
        return data.capitalize()

    # Method that cleans values in the phone_number column (column_number = 8)
    def clean_phone_number(self, data):
        data = data.replace("-", "")
        data = data.replace("+44", "0")
        data = data.replace(" (", "")
        data = data.replace(") ", "")
        data = ''.join(data.split())

        return data


    def clean_degree(self, data):
        pass

    # Method that cleans values in the invited_day column (column_number = 11)
    def clean_invite_day(self, data):
        cleaned_day = data.lstrip('0')
        return cleaned_day

    # Method that takes in a row from the list of rows, iterates through each element (data) within the row.

    def clean_row(self, row):

        cleaned_row = []

        for data in row:
            # First, the code checks if the element is empty by calling the 'check_if_empty' function.
            if self.check_if_empty(data):  # If there is no value
                # If it is empty, the data is changed to the string 'null' by calling the 'empty_to_null' function and
                # appended into list 'cleaned_row'
                column_num = find_column_number(row, data)
                cleaned_data = self.empty_to_null(data,column_num)
                cleaned_row.append(cleaned_data)

            else:
                # If the element is not empty, the appropriate cleaning function is applied by finding the
                # column_number value and calling the appropriate cleaning function. Once the cleaning is complete,
                # the cleaned data is appended into list 'cleaned_row'
                column_number = find_column_number(row, data)
                cleaned_data = self.call_cleaning_function(column_number, data)
                cleaned_row.append(cleaned_data)

        return cleaned_row


def df_output(data, filename):
    data.to_csv(f"Data/{filename}", sep=',')


# Function that takes in filename (a csv file) as an argument
def read_csv(filename):
    first_row = 0  # The index from the list of rows this code block will iterate from. As the first
    # element from the list of rows is the column headers, it doesn't require cleaning

    # code block that opens the csv file and creates a list of rows called 'rows' that will be input into
    # the DataCleaner class
    # csv_file = csv.reader(f, delimiter=',')
    cleaned_df = pd.DataFrame(
        columns=['name', 'gender', 'dob', 'email', 'city', 'address', 'postcode', 'phone', 'uni', 'degree',
                 'invited_day', 'month', 'invited_by'])
    cleaned_list = []
    csv_file = pd.read_csv(StringIO(filename)).applymap(str)
    rows = csv_file.values.tolist()
    dataCleaner = DataCleaner(rows)
    rows_to_read = len(rows)
    # rows = list(csv_file)
    # dc = DataCleaner(rows)  # Instance called 'dc' created that takes in the list of rows created earlier

    # rows_to_read = len(rows)  # rows_to_read is set to len(rows), the number of rows in the list of rows created

    # for loop that iterates through the list of rows from 1 to the number of rows, and calls the
    # clean_row method in the DataCleaner class to return a new list consisting of cleaned rows
    for i in range(first_row, rows_to_read):
        # print(rows[i])
        cleaned_df.loc[i] = [dataCleaner.clean_row(rows[i])[1], dataCleaner.clean_row(rows[i])[2],
                             dataCleaner.clean_row(rows[i])[3],
                             dataCleaner.clean_row(rows[i])[4], dataCleaner.clean_row(rows[i])[5],
                             dataCleaner.clean_row(rows[i])[6],
                             dataCleaner.clean_row(rows[i])[7],
                             dataCleaner.clean_row(rows[i])[8], dataCleaner.clean_row(rows[i])[9],
                             dataCleaner.clean_row(rows[i])[10],
                             dataCleaner.clean_row(rows[i])[11],
                             dataCleaner.clean_row(rows[i])[12], dataCleaner.clean_row(rows[i])[13]]

    return cleaned_df
    # f.close()

# read_csv(file_to_read)
