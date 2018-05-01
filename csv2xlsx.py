import os
import glob
import csv
from xlsxwriter.workbook import Workbook

# glob is a python library that searches for the pathnames
# glob.glob(os.path.join('.', '*.csv'))  --
# this will search for all the files with extension .csv directory where python script is running from
# It returns a list (like arrays)
# print(os.path.join('.', '*.csv'))
# print(glob.glob(os.path.join('.', '*.csv')))

for csvfile in glob.glob(os.path.join('.', '*.csv')):  # this picks every .csv file
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    # print(csvfile[:-4])
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:  # open every csv file, rt: read-only in text mode
        reader = csv.reader(f)  # reads every file line by line
        for r, row in enumerate(reader):  # enumerate adds the index to every line
            # print('r--: '+str(r)) # counts the row
            for c, col in enumerate(row):  # counts columns
                # print('c--:{}  col:{}'.format(str(c),col))
                worksheet.write(r, c, col)
    workbook.close()
