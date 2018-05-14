# Read every file in specified folder (delimited files)
# searhces for the specified value in the 0th index(1st column)
# If match is found prints out the filename and how many records are there in that file that match
# Writes this into a csv file (csvwrite function)
# Prints out the total record

import os

temp_folder = "U:\\temp1"

def csvwrite(mydata, filename, folderName=temp_folder):
    if not os.path.isdir(folderName):
        os.makedirs(folderName)
    with open(os.path.join(folderName,filename), 'a') as f1:
        #f1.write(','.join(mydata))
        f1.write(mydata)
        f1.write('\n')

def search_text(searchTxt, folderPath, delimiter):
    '''
        This function searches for the text in a delimited text files first column for every line
        If a match is found, the prints the file name
        searchTxt: value to be searched
        folderPath: path where the files are located
        delimiter: how the records in the files are separated
    '''
    match = 0
    filematch = 0
    fileList = []

    for fileName in os.listdir(folderPath):
        f = open(os.path.join(folderPath,fileName),'r')
        for line in f:
            fields = line.split(delimiter)
            if int(fields[0]) == searchTxt:
                match += 1
                fileList.append(fileName)
        combinedtxt= fileName + ',' + str(filematch)
        csvwrite(combinedtxt, "a.csv","U:\\temp1")
    print('*'*100)
    print('Total records for transaction type {}: {}'.format(str(searchTxt),match))
    print('*'*100)
    f.close
