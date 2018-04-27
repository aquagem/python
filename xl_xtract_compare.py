import sys
import os
import shutil
import csv
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

def csvwrite(mydata):
    print(','.join(mydata))

    with open(newFile,'a') as f1:
        #writer = csv.writer(f1,delimiter=',')
        for line in mydata:
            #print(line)
            #writer.writerow(line)
            f1.write(line)
    


#glb_filePath = input("Global customers file path:")  # get the file path
'''Get the list of Global customers from the csv file  FILE A'''
if check_filexists(glb_filePath):
    if check_fileExt(glb_filePath,".csv"):   #check if the file exits and if the file is a csv file        
        with open(glb_filePath,'r') as csvFile:   # open file in read-only mode
            data = csvFile.readlines()
            '''for line in csvFile:
                field = line.split(",")
                glbl_cust.append(field[5])
                #print("Global Customers:" +str(glbl_cust))'''
    else:
        print("Invalid file type. Expected .csv; Actual: {}".format(os.path.splitext(glb_filePath)[1]))
        sys.exit(1)
else:
    print("File {} not found" .format(glb_filePath))
    sys.exit(1)

#print global customers
'''for j in range(len(glbl_cust)):
    print("Global Customers:" +str(glbl_cust[j]))'''

'''Copy csv file (A) into a new file '''
newFile = os.path.splitext(glb_filePath)[0]+'_1'+os.path.splitext(glb_filePath)[1]
#shutil.copy(glb_filePath,newFile)

'''Get the list of national customers from the excel file  FILE B'''
#ntnl_filePath = input("National customers file path:")  # get the file path
if check_filexists(ntnl_filePath):
    if check_fileExt(ntnl_filePath,".xlsx"):
        xlFile = open_workbook(ntnl_filePath)
        xl_sheet = xlFile.sheet_by_index(0)  # Assuming that there is only one sheet in Excel file
        number_of_rows = xl_sheet.nrows
        for row in range(1,number_of_rows):
            ntnl_Cust.append(xl_sheet.cell(row,0).value)
        '''for i in range(len(ntnl_Cust)):
            print("National Customers: " +str(ntnl_Cust[i]).split("-")[0]) # print national customers'''
    else:
        print("Invalid file type. Expected .xlsx; Actual: {}".format(os.path.splitext(ntnl_filePath)[1]))
        sys.exit(1)
else:
    print("File {} not found" .format(ntnl_filePath))
    sys.exit(1)


'''Search every element of FILE B(ntnl_Cust) array in FILE A and if match found, insert that value in the end of the file'''
# get every line in file A:

for i in range(len(ntnl_Cust)):
    reader = csv.reader(data)
    #print(str(ntnl_Cust[i]).split("-")[0].strip())
    for row in reader:
        #print(str(row[5]))
        if str(ntnl_Cust[i]).split("-")[0].strip() == str(row[5]):
            row.append(","+str(row[5]))
            csvwrite(row)
        else:
            row.append(",NA")
            csvwrite(row)




#csvFile.close
xlFile.release_resources()
