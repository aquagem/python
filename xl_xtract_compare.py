import sys
import os
import csv
from xlrd import open_workbook

glbl_cust = []
ntnl_Cust = []

glb_filePath = "u:\downloads\A.csv"
ntnl_filePath = "U:\downloads\B.xlsx"
finalFile = os.path.splitext(glb_filePath)[0] + '_final' + os.path.splitext(glb_filePath)[1]


def check_filexists(filename):
    if os.path.isfile(filename):
        return True


def check_fileext(filename, extension):
    if os.path.splitext(filename)[1] == extension:
        return True


def csvwrite(mydata,filename):
    ##print(','.join(mydata))
    #if filename == finalFile:
        #print(mydata)
        #print(''.join(mydata))
    with open(filename, 'a') as f1:
        # writer = csv.writer(f1,delimiter=',')
        f1.write(','.join(mydata))
        f1.write('\n')
        #for line in mydata:
            #print(line)
            # writer.writerow(line)
            #f1.write(line)


# glb_filePath = input("Global customers file path:")  # get the file path
'''Get the list of Global customers from the csv file  FILE A'''
if check_filexists(glb_filePath):
    if check_fileext(glb_filePath, ".csv"):  # check if the file exits and if the file is a csv file
        with open(glb_filePath, 'r') as csvFile:  # open file in read-only mode
            data = csvFile.readlines()
            '''for line in csvFile:
                field = line.split(",")
                glbl_cust.append(field[5])
                #print("Global Customers:" +str(glbl_cust))'''
    else:
        print("Invalid file type. Expected .csv; Actual: {}".format(os.path.splitext(glb_filePath)[1]))
        sys.exit(1)
else:
    print("File {} not found".format(glb_filePath))
    sys.exit(1)

# print global customers
'''for j in range(len(glbl_cust)):
    print("Global Customers:" +str(glbl_cust[j]))'''

'''Copy csv file (A) into a new file '''
newFile = os.path.splitext(glb_filePath)[0] + '_1' + os.path.splitext(glb_filePath)[1]
# shutil.copy(glb_filePath,newFile)

'''Get the list of national customers from the excel file  FILE B'''
# ntnl_filePath = input("National customers file path:")  # get the file path
if check_filexists(ntnl_filePath):
    if check_fileext(ntnl_filePath, ".xlsx"):
        xlFile = open_workbook(ntnl_filePath)
        xl_sheet = xlFile.sheet_by_index(0)  # Assuming that there is only one sheet in Excel file
        number_of_rows = xl_sheet.nrows
        for row in range(1, number_of_rows):
            ntnl_Cust.append(xl_sheet.cell(row, 0).value)
        '''for i in range(len(ntnl_Cust)):
            print("National Customers: " +str(ntnl_Cust[i]).split("-")[0]) # print national customers'''
    else:
        print("Invalid file type. Expected .xlsx; Actual: {}".format(os.path.splitext(ntnl_filePath)[1]))
        sys.exit(1)
else:
    print("File {} not found".format(ntnl_filePath))
    sys.exit(1)

'''Search every element of FILE B(ntnl_Cust) array in FILE A 
and if match found, insert that value in the end of the file'''
# get every line in file A:

for i in range(len(ntnl_Cust)):
    reader = csv.reader(data)
    # print(str(ntnl_Cust[i]).split("-")[0].strip())
    for row in reader:
        # print(str(row[5]))
        if str(ntnl_Cust[i]).split("-")[0].strip() == str(row[5]):
            #row.append("," + str(row[5]))
            print(row)
            csvwrite(row, newFile)
        #else:
            #row.append(",NA")
            #csvwrite(row)

# csvFile.close
xlFile.release_resources()

# Compare 2 csv files (original and new)
with open(glb_filePath, 'r') as t1, open(newFile, 'r') as t2:
    file1 = t1.readlines()
    file2 = t2.readlines()
    #print("A")

##finalFile = os.path.splitext(glb_filePath)[0] + '_final' + os.path.splitext(glb_filePath)[1]
with open(finalFile,'w') as outFile:
    for line in file1:  
        if line in file2:
            line = line.rstrip('\n').split(',')
            line.append(line[5])
            csvwrite(line, finalFile)
        else:
            line = line.rstrip('\n').split(',')
            line.append("NA")
            csvwrite(line, finalFile)
