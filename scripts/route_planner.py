# Automatically assigning the charging stops in the route-file 

import xml.etree.ElementTree as ET

xmlfile_1 = "auto_routes.xml"
xmlfile_2 = "trips_test.xml"
xmlfile_3 = "auto_public.xml"

tree_1 = ET.parse(xmlfile_1)
root_1 = tree_1.getroot()

tree_2 = ET.parse(xmlfile_2)
root_2 = tree_2.getroot()

tree_3 = ET.parse(xmlfile_3)
root_3 = tree_3.getroot()

trips1 = []
trips2 = []
trips3 = []

i = 0
j = 0

k = 1

# Get lane ids from trip file
for element1 in root_2.findall('./flow'):
    trips1.append(element1.attrib['from'])

for element2 in root_1.findall('./flow'):
    element2.set('to',trips1[i])
    i += 1

for element3 in root_2.findall('./flow'):
    trips2.append(element3.attrib['to'])

for element5 in root_3.findall('./chargingStation'):
    trips3.append(element5.attrib['lane'])

for element4 in root_1.findall('./flow'):
    element4.set('via', (trips2[j]) + " " + str(trips3[j])[:-2])
    j += 1

# Assign charging stops to vehicles in route-file
for item in root_1.findall('flow'):
    idplus = "hh16_ev" + str(k) + "_work"
    id = "hh16_ev" + str(k) + "_public"
    id2 = "hh16_ev" + str(k) + "_home"
    newplus = ET.SubElement(item, 'stop', chargingStation=idplus, until="1500")
    new = ET.SubElement(item, 'stop', chargingStation=id,until="2500")
    new2 = ET.SubElement(item, 'stop', parkingArea=id2)
    k += 1
    

tree_1.write(xmlfile_1,encoding='UTF-8',xml_declaration=True) 

print('done')