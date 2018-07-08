'''
Script reads the xml file and returns the values from the tags specified
in here it returns all the author name and their books
'''

import xml.etree.ElementTree as ET
import re

xmlfilePath = '<path of the Sample_xml_file.xml>'

tree = ET.parse(xmlfilePath)
root = tree.getroot()

print(root.tag)
print(root.attrib)

#for child in root:
#   print(child.tag, child.attrib)
   
# Specific children can be accessed by index : print(root[0][0].text)

# Get the list of all the authors and their books
for elem in root.findall('book'):
    author = elem.find('author').text
    title = elem.find('title').text
    print("{} --> {}".format(author, title))




