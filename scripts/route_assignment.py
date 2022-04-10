# Automatically assigning the routes of the first round trip to vehicles in route-file

import xml.etree.ElementTree as ET

xmlfile_1 = "mannheim_auto.rou.xml"
xmlfile_2 = "trips_test.xml"

tree_1 = ET.parse(xmlfile_1)
root_1 = tree_1.getroot()

tree_2 = ET.parse(xmlfile_2)
root_2 = tree_2.getroot()

trips1 = []
trips2 = []
i = 0
j = 0

# Get lane id from random trip generator and assign vehicle to source
for element1 in root_2.findall('./trip'):
    trips1.append(element1.attrib['from'])

for element2 in root_1.findall('./flow'):
    element2.set('from',trips1[i])
    i += 1

# Get lane id from random trip generator and assign vehicle to destination
for element3 in root_2.findall('./trip'):
    trips2.append(element3.attrib['to'])

for element4 in root_1.findall('./flow'):
    element4.set('to',trips2[j])
    j += 1

tree_1.write(xmlfile_1,encoding='UTF-8',xml_declaration=True) 

print('done')



