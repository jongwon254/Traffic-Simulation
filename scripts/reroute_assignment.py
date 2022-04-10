# Automatically assigning the reroute-commands in the python main program

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

i = 0
j = 0

k = 1

# Get lane ids from trip-file 
for element1 in root_2.findall('./flow'):
    trips1.append(element1.attrib['from'])

for element3 in root_2.findall('./flow'):
    trips2.append(element3.attrib['to'])

for element3 in root_3.findall('./chargingStation'):
    trips2.append(element3.attrib['lane'])

# ex) second rountrip to public and home for household 16
with open('readme.txt', 'w') as f:
    for i in range(0,136):
        f.write('traci.vehicle.resume("HH_16_EV_' + str(i+1) + '.0")' + "\n")
        f.write('traci.vehicle.changeTarget("HH_16_EV_' + str(i+1) + '.0", "' + str(trips2[i])[:-2] + '")' + "\n")
        f.write('traci.vehicle.setChargingStationStop("HH_16_EV_' + str(i+1) + '.0", "hh16_ev' + str(i+1) + '_public", flags=32)' + "\n")
        f.write("\n")

    f.write('---------------------------------------------------------')
    f.write('')

    for j in range(0,136):
        f.write('traci.vehicle.resume("HH_16_EV_' + str(j+1) + '.0")' + "\n")
        f.write('traci.vehicle.changeTarget("HH_16_EV_' + str(j+1) + '.0", "' + trips1[j] + '")' + "\n")
        f.write('traci.vehicle.setParkingAreaStop("HH_16_EV_' + str(j+1) + '.0", "hh16_ev' + str(j+1) + '_home", flags=32)' + "\n")
        f.write("\n")

print("done")
