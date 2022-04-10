# Automating assignment of charging stations into route-file

from lxml import etree as ET
import urllib

xmlfile_1 = "mannheim_test.rou.xml"

tree_1 = ET.parse(xmlfile_1)
root_1 = tree_1.getroot()

home = []
i = 1

# Get lane id from route-file
for element in root_1.findall('./flow'):
    home.append(element.attrib['from'])

root = ET.Element("additional")

# Based on lane id, generate charging station in additional-file
for cs in home:
    lane = str(cs) + "_0"
    id = "hh1_ev" + str(i) + "_home" #home #work #public
    ET.SubElement(root, "chargingStation", id=id, lane=lane, startPos="0", endPos="10", friendlyPos="1", power="7000", efficiency="1.0")
    i += 1

tree = ET.ElementTree(root)
tree.write("mannheim_test.add.xml", pretty_print=True)

print("done")

