"""
The main purpose of this script is to check if every record from the csv file has been loaded successfully into the DB
Reads data from CSV file
Builds a sql query
executes the query and prints the query if no data is found in DB
"""

import csv
import pyodbc
import datetime

server = '<server>.database.windows.net'
database = '<database>'
username = '<username>'
password = '<password>'
driver = '{ODBC Driver 13 for SQL Server}'

cnxn = pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

with open("filename.csv", 'r') as f:
    csvfile = csv.reader(f, delimiter='|')
    next(csvfile)  # skip header
    
    # Get the required column values from CSV and build the sql
    for row in csvfile:
        query = "select col1, col2, col3, col4 from Table1 " \
                "where col1 = '" + row[0] + "' and" \
                " col2 = '" + row[1] + "' and" \
                " col3 = '" + row[2] + "' and" \
                " col4 = '" + row[24] + "'"
        # print(query)
        
        cursor.execute(query)
        row = cursor.fetchone()

        i += 1
        # Print the time for every 10K records. Useful when large file are processed
        if row:
            if i % 10000 == 0:
                print('{} : {}'.format(i, datetime.datetime.today()))
                # print(str(row[0]) + str(row[1]) + str(row[2]) + str(row[3]))   # Print the data that was retrieved from DB, Depends on how many
                # columns are returned
        else:
            print(query)    # in case of errors print the query that did not return any data

cursor.close()
