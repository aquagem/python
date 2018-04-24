'''
Script name: searchTextCmd.py
Description: Script is used to search a text in in a delimited file
             It reads all the files in the specified folder, and searches for the value in the specified column
             It returns the total number of matches
'''

import os
import sys
import argparse

parser = argparse.ArgumentParser(description="Search value in files", epilog="Usage")
parser.add_argument('textTOSearch', help="enter the text to be searched",action="store_true")
parser.add_argument('folderPath', help="Path of the folder where the files are located",action="store_true")
parser.add_argument('delimiter', help="value of the delimiter in the files",action="store_true")
parser.add_argument('colNum', help="column number where the search has to be performed",action="store_true")
parser.add_argument('Sample Call', help='searchTxt_cmd.py 14 "C:\\Temp" "|" 0',action="store_true")

if len(sys.argv) != 5:
    parser.print_help()
    sys.exit(1)

searchTxt = sys.argv[1]
folderPath = sys.argv[2]
delimiter = sys.argv[3]
colNum = sys.argv[4]

match = 0
fileList = []

try:
    if os.listdir(folderPath) ==[]:
        print("This is an empty folder: " +folderPath)
    else:
        for fileName in os.listdir(folderPath):
            f = open(os.path.join(folderPath,fileName),'r')
            for line in f:
                fields = line.split(delimiter)
                if int(fields[int(colNum)]) == int(searchTxt):
                    match += 1
                    fileList.append(fileName)
        print('*'*50)
        print('Total records for transaction type {}: {}'.format(searchTxt,match))
        print('*'*50)
        f.close
except ValueError:
    print("Delimiter: {} or Column Number: {} does not exist or is invalid".format(delimiter,colNum))
except IOError:
    print("Folder path does not exist or is invalid: "+folderPath)
except IndexError:
    print("Invalid column value:"+colNum)
