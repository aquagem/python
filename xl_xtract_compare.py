import sys
import os
import csv
from xlrd import open_workbook
from xlsxwriter.workbook import Workbook


glbl_cust = []
ntnl_Cust = []

glb_filePath = "E:\Misc\A.csv"
ntnl_filePath = "E:\Misc\B.xlsx"

# ntnl_filePath = input("National customers file path:")
# glb_filePath = input("Global customers file path:")

newFile = os.path.splitext(glb_filePath)[0] + '_temp' + os.path.splitext(glb_filePath)[1]
finalFile = os.path.splitext(glb_filePath)[0] + '_final' + os.path.splitext(glb_filePath)[1]


def check_filexists(filename):
    if os.path.isfile(filename):
        return True


def check_fileext(filename, extension):
    if os.path.splitext(filename)[1] == extension:
        return True


def csvwrite(mydata, filename):
    with open(filename, 'a') as f1:
        f1.write(','.join(mydata))
        f1.write('\n')


# Get the list of Global customers from the csv file  FILE A
if check_filexists(glb_filePath):
    if check_fileext(glb_filePath, ".csv"):  # check if the file exits and if the file is a csv file
        with open(glb_filePath, 'r') as csvFile:  # open file in read-only mode
            data = csvFile.readlines()
    else:
        print("Invalid file type. Expected .csv; Actual: {}".format(os.path.splitext(glb_filePath)[1]))
        sys.exit(1)
else:
    print("File {} not found".format(glb_filePath))
    sys.exit(1)

# Get the list of national customers from the excel file  FILE B
if check_filexists(ntnl_filePath):
    if check_fileext(ntnl_filePath, ".xlsx"):
        xlFile = open_workbook(ntnl_filePath)
        xl_sheet = xlFile.sheet_by_index(0)  # Assuming that there is only one sheet in Excel file
        number_of_rows = xl_sheet.nrows
        for row in range(1, number_of_rows):
            ntnl_Cust.append(xl_sheet.cell(row, 0).value)  # place the contents of the row in a list
    else:
        print("Invalid file type. Expected .xlsx; Actual: {}".format(os.path.splitext(ntnl_filePath)[1]))
        sys.exit(1)
else:
    print("File {} not found".format(ntnl_filePath))
    sys.exit(1)

xlFile.release_resources()  # Close the Excel File

# Search every element of FILE B(ntnl_Cust) list in FILE A
# and if match found, insert that value in the end of the file
for i in range(len(ntnl_Cust)):  # loop through every element of list of Natioanl Customers
    reader = csv.reader(data)
    for row in reader:  # if the row value of file B matches 5th column of file A then write it into a new file
        if str(ntnl_Cust[i]).split("-")[0].strip() == str(row[5]):
            csvwrite(row, newFile)

# Compare 2 csv files (original(file B) and newfile created above)

# DEBUG START
print("GLBL FILE {} exists: {}".format(glb_filePath, check_filexists(glb_filePath)))
print("NEW FILE {} exists: {}".format(newFile, check_filexists(glb_filePath)))
# DEBUG END

with open(glb_filePath, 'r') as t1, open(newFile, 'r') as t2:
    file1 = t1.readlines()
    file2 = t2.readlines()

with open(finalFile, 'w') as outFile:
    for line in file1:
        if line in file2:
            line = line.rstrip('\n').split(',')
            line.append(line[5])
            csvwrite(line, finalFile)
        else:
            line = line.rstrip('\n').split(',')
            line.append('NA')
            csvwrite(line, finalFile)
# #####################################################################
# convert the final csv file into a xlsx file
workbook = Workbook(finalFile[:-4] + '.xlsx')
worksheet = workbook.add_worksheet()
with open(finalFile, 'rt', encoding='utf8') as f:  # open every csv file, rt: read-only in text mode
    reader = csv.reader(f)  # reads every file line by line
    for r, row in enumerate(reader):  # enumerate adds the index to every line
        for c, col in enumerate(row):  # counts columns
            worksheet.write(r, c, col)
    workbook.close()
