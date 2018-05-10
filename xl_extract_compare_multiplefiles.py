# This script will get the list of records from a Excel file  (File B data)
# Go through every csv file in the folder specified and check if the File B records exist
# If a match occurs, then append that matched string to that line
# Then convert all the csv files into individual excel files
# and place the contents of the csv files into one excel sheet with every csv file in one tab

import csv
import xlsxwriter
import sys
import os
import glob
from xlrd import open_workbook
from xlsxwriter.workbook import Workbook
import shutil

csvfolder = input("Provide the folder where csv files are located:")
ntnl_filePath = input("NCs file path:")
# csvfolder = "U:\Downloads\\temp1"
# ntnl_filePath = "U:\Downloads\B.xlsx"

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


# Get the list of NCs from the excel file  FILE B
def getNCs():
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


########FUNCTION CALLS########
getNCs()
ntnl_Cust = [str(ntnl_Cust[i]).split("-")[0].strip() for i in range(len(ntnl_Cust))]

if len(get_csvfiles(csvfolder)) > 0:
    for f in csvfiles:
        temp_file = os.path.splitext(f)[0] + '_temp' + os.path.splitext(f)[1]
        with open(f, 'r') as infile, open(temp_file,'w') as ofile:
            reader = csv.reader(infile.readlines())
            writer = csv.writer(ofile)
            for line in reader:
                if line[7] in ntnl_Cust:
                    line.append(line[7])
                    writer.writerow(line)
                    #break
                else:
                    writer.writerow(line)
        with open(temp_file, "r") as fin, open(os.path.splitext(f)[0] + '_temp_1' + os.path.splitext(f)[1], "w") as fout:
            for line in fin:
                if not line.strip():
                    continue
                fout.write(line)
        shutil.move(fout.name,temp_file)
        shutil.move(temp_file, f)
else:
    sys.exit("There are no csv files in this directory: {} ".format(csvfolder))



#####################################################################
if len(get_csvfiles(csvfolder)) > 0:
    write2XL()
else:
    print("There are no csv files in this directory: {} ".format(csvfolder))
#####################################################################

# Individual Excel Files:
os.chdir(csvfolder)
for csvfile in glob.glob(os.path.join('.', '*.csv')):  # this picks every .csv file
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    #print(csvfile[:-4])
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:  # open every csv file, rt: read-only in text mode
        reader = csv.reader(f)  # reads every file line by line
        for r, row in enumerate(reader):  # enumerate adds the index to every line
            #print('r--: '+str(r)) # counts the row
            for c, col in enumerate(row):  # counts columns
                #print('c--:{}  col:{}'.format(str(c),col))
                worksheet.write(r, c, col)
    workbook.close()
