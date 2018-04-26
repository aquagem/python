import sys
import os
from xlrd import open_workbook

glbl_cust = []
ntnl_Cust = []

glb_filePath ="u:\downloads\A.csv"
ntnl_filePath = "U:\downloads\B.xlsx"

def check_filexists(fileName):
    '''
    Function to check if the file exists
    '''
    if os.path.isfile(fileName):
        return True

def check_fileExt(fileName,extension):
    '''
    Function to check the file extension
    '''
    if os.path.splitext(fileName)[1] == extension:
        return True


#glb_filePath = input("Global customers file path:")  # get the file path
'''Get the list of Global customers from the csv file '''
if check_filexists(glb_filePath):
    if check_fileExt(glb_filePath,".csv"):   #check if the file exits and if the file is a csv file
        csvFile = open(glb_filePath,'r')     # open file in read-only mode
        for line in csvFile:
            field = line.split(",")
            glbl_cust.append(field[5])
            #print("Global Customers:" +str(glbl_cust))
    else:
        print("Invalid file type. Expected .csv; Actual: {}".format(os.path.splitext(glb_filePath)[1]))
        sys.exit(1)
else:
    print("File {} not found" .format(glb_filePath))
    sys.exit(1)

for j in range(len(glbl_cust)):
    print("Global Customers:" +str(glbl_cust[j]))


'''Get the list of national customers from the excel file '''
#ntnl_filePath = input("National customers file path:")  # get the file path
if check_filexists(ntnl_filePath):
    if check_fileExt(ntnl_filePath,".xlsx"):
        xlFile = open_workbook(ntnl_filePath)
        xl_sheet = xlFile.sheet_by_index(0)  # Assuming that there is only one sheet in Excel file
        number_of_rows = xl_sheet.nrows
        for row in range(1,number_of_rows):
            ntnl_Cust.append(xl_sheet.cell(row,0).value)
        for i in range(len(ntnl_Cust)):
            print("National Customers: " +str(ntnl_Cust[i]).split("-")[0])
    else:
        print("Invalid file type. Expected .xlsx; Actual: {}".format(os.path.splitext(ntnl_filePath)[1]))
        sys.exit(1)
else:
    print("File {} not found" .format(ntnl_filePath))
    sys.exit(1)

csvFile.close
xlFile.release_resources()
