'''
This script will read a json file and writes every element into a tab separated text file
Also find if there are duplicates and writes them into the duplicates file
'''

import json
from pprint import pprint

#https://stackoverflow.com/questions/19483351/converting-json-string-to-dictionary-not-list?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

json_file = "<path of samplejsonfile.json>"
posvals = []
resultfile = "<path to results.txt>"
duplicatefile = "<path to duplicates.txt>"

def writetofile(filename, content):
    with open(filename, 'w') as f1:
        for item in content:
            f1.write("%s\n" % item)

with open(json_file, 'r') as f:
    jsonstr = f.read()
    json_data = json.loads(jsonstr)[0]
    datapoints = json_data['Item1']
    for i in range(len(datapoints)):
        positemId = json_data['Item1'][i]['ChildItem1']
        name = json_data['Item1'][i]['ChildItem2']
        desc = json_data['Item1'][i]['ChildItem3']
        posvals.append(positemId + '|' + name + '|'+ desc)

writetofile(resultfile,posvals)

dupes = [x for n, x in enumerate(posvals) if x in posvals[:n]]
writetofile(duplicatefile,dupes)
