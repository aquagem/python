import os

fileName = "E:\\Misc\\SampleExtract.txt"
# productline = []

looplines = []


def getlines():
    global looplines
    with open(fileName, 'r') as fr:
        for i, line in enumerate(fr):
            if line and line[0:7] == 'Product':
                looplines.append(i)
            '''product = line[9:22]
            desc = line[30:67]
            proddesc = product.strip() + ' : ' + desc.strip()
            productline.append(proddesc)
'''


def getdata():
    with open(fileName, 'r') as fr1:
        for i, line in enumerate(fr1):
            if i in looplines:
                print(i)


getlines()
# getdata()
# print(looplines)
for items in looplines[0:2]:
    print(items)
