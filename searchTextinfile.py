import os

def search_text(searchTxt, folderPath, delimiter):
    '''
        This function searches for the text in a delimited text files first column for every line
        If a match is found, the prints the file name
        searchTxt: value to be searched
        folderPath: path where the files are located
        delimiter: how the records in the files are separated
    '''
    match = 0
    fileList = []

    for fileName in os.listdir(folderPath):
        f = open(os.path.join(folderPath,fileName),'r')
        for line in f:
            fields = line.split(delimiter)
            if int(fields[0]) == searchTxt:
                match += 1
                fileList.append(fileName)
    print('*'*100)
    print('Total records for transaction type {}: {}'.format(str(searchTxt),match))
    print('*'*100)
    f.close
