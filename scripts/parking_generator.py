# Automating assignment of parking areas into route-file

from lxml import etree as ET
import urllib

xmlfile_1 = "mannheim_test.rou.xml"

tree_1 = ET.parse(xmlfile_1)
root_1 = tree_1.getroot()

home = []
i = 1

# Get lane id from route-file
for element in root_1.findall('./flow'):
    home.append(element.attrib['from']) #from #to #via

root = ET.Element("additional")

# Based on lane id, generate parking area in additional-file
for edge in home:
    lane = str(edge) + "_0"
    id = "hh14_ev" + str(i) + "_home" #home #work #public
    ET.SubElement(root, "parkingArea", id=id, lane=lane, startPos="0", endPos="10", roadsideCapacity="1", friendlyPos="1", width="5.00", length="10", angle="30.00")
    i += 1

tree = ET.ElementTree(root)
tree.write("mannheim_test_parking.add.xml", pretty_print=True)

print("done")