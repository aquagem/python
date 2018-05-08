# Script to read multiple csv files in a folder and place them into one Excel sheet 
# Every csv file is under a new tab in excel sheet

import csv
import xlsxwriter
import sys
import os
import glob
from xlrd import open_workbook

# csvfolder = input("Provide the folder where csv files are located:")
# ntnl_filePath = input("National customers file path:")
csvfolder = "U:\Downloads\\temp1"
ntnl_filePath = "U:\Downloads\B.xlsx"

xl_workbook = csvfolder +"\mergedXL.xlsx"
temp_folder = csvfolder +"\\temp"

csvfiles = []
ntnl_Cust = []

# Get only csv files in the specified folder
def get_csvfiles(infolder):
    if os.path.isdir(infolder):
        os.chdir(infolder)
        ext = 'csv'
        global csvfiles 
        csvfiles = [f1 for f1 in glob.glob('*.{}'.format(ext))]
        return csvfiles
    else:
        sys.exit("Folder {} does not exist".format(infolder))

def csvwrite(mydata, filename, folderName=temp_folder):
    if not os.path.isdir(folderName):
        os.makedirs(folderName)
    with open(os.path.join(folderName,filename), 'a') as f1:
        f1.write(','.join(mydata))
        f1.write('\n')


# Get the list of national customers from the excel file  FILE B
def getNationalCustomers():
    global ntnl_Cust
    if os.path.isfile(ntnl_filePath):
        if os.path.splitext(ntnl_filePath)[1] == ".xlsx":
            xlFile = open_workbook(ntnl_filePath)
            xl_sheet = xlFile.sheet_by_index(0)  # Assuming that there is only one sheet in Excel file
            number_of_rows = xl_sheet.nrows
            for row in range(1, number_of_rows):
                ntnl_Cust.append(xl_sheet.cell(row, 0).value)  # place the contents of the row in a list
        else:
            sys.exit("Invalid file type. Expected .xlsx; Actual: {}".format(os.path.splitext(ntnl_filePath)[1]))
    else:
        sys.exit("File {} not found".format(ntnl_filePath))

    xlFile.release_resources()  # Close the Excel File



########FUNCTION CALLS########
getNationalCustomers()

if len(get_csvfiles(csvfolder)) > 0:
    for f in csvfiles:
        with open(f, 'r') as csvFile:  # open file in read-only mode
            data = csvFile.readlines()
        for i in range(len(ntnl_Cust)):  # loop through every element of list of Natioanl Customers
            reader = csv.reader(data)
            for row in reader:  # if the row value of file B matches 5th column of file A then write it into a new file
                if str(ntnl_Cust[i]).split("-")[0].strip() == str(row[5]):
                    row.append(str(row[5]))
                    #csvwrite(row, os.path.splitext(f)[0] + '_temp' + os.path.splitext(f)[1], temp_folder)
                    csvwrite(row, f, csvfolder)
else:
    sys.exit("There are no csv files in this directory: {} ".format(csvfolder))

print(len(data))

#for tempfile in os.listdir(temp_folder):
#    print(tempfile)




#####################################################################
'''
def write2XL():
    wb = xlsxwriter.Workbook(xl_workbook)
    for cfile in csvfiles:
        ws = wb.add_worksheet(cfile[:-4])
        #Read contents of every csv file and place it in worksheet
        with open(csvfolder +'\\'+ cfile) as fname:
            reader = csv.reader(fname)
            i = 0
            for row in reader:
                for j, each in enumerate(row):
                    ws.write(i,j,each)
                i +=1
    wb.close
    



if len(get_csvfiles()) > 0:
    write2XL()
else:
    print("There are no csv files in this directory: {} ".format(csvfolder))'''
#####################################################################
