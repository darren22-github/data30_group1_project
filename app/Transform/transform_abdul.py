from tempfile import NamedTemporaryFile
import shutil
import csv
import pandas as pd

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

filename = 'Aug2019Applicants.csv'
tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

with open(filename, 'r', newline='') as csvFile, tempfile:
    reader = csv.reader(csvFile, delimiter=',', quotechar='"')
    headers = next(reader, None)
    writer = csv.writer(tempfile, delimiter=',', quotechar='"')

    if headers:
        writer.writerow(headers)

    for row in reader:  # capitalises first letter of first and last name
        row[1] = row[1].title()
        writer.writerow(row)

    for row in reader:  # converts number to UK format
        row[8] = row[8].replace("-", "")
        row[8] = row[8].replace("+44", "0")
        row[8] = row[8].replace(" (", "")
        row[8] = row[8].replace(") ", "")
        row[8] = ''.join(row[8].split())
        writer.writerow(row)

    for row in reader:  # removes leading zero from invited_date column
        row[11] = row[11].lstrip('0')
        writer.writerow(row)

    for row in reader: # capitalizes first letter from month column
        row[12] = row[12].capitalize()
        writer.writerow(row)

    for row in reader: # ensures first words of first and last names are capitalized
        row[13] = row[1].title()
        writer.writerow(row)

shutil.move(tempfile.name, filename)

# df = pd.read_csv(filename)
# df = df.drop('month', 1)
# df.to_csv('clean_data.csv')
