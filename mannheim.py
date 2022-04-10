# Main Program, run this file to start the simulation
# Input: sumo-gui.exe and mannheim.sumocfg (or different sumocfg for scenario 1/2)

import os, sys
import csv

# The SUMO simulation has to be installed and the path environment varibale has to be set correctly on the computer

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

# Path to the exe-file of SUMO and the input configuration file .sumocfg
sumoBinary = "../sumo-win64-1.8.0/sumo-1.8.0/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "mannheim.sumocfg"] # change sumocfg-files for different scenarios

# importing TraCI and setting variables
import traci
traci.start(sumoCmd)
step = 0
totalEnergy = 0

# Generating csv-file for power profile output file
f = open('charging_scenario2.csv', 'w', newline='')
writer = csv.writer(f, delimiter = ';')
writer.writerow(['step', 'charging_station', 'status', 'EV', 'watt_charged', 'current_battery', 'max_battery'])

# List of all charging stations to loop through in next while-loop
with open("cs_id.txt", "r") as reader:
	cslist = reader.read().splitlines()

print("Simulation started")

# Main while loop of the simulation, starts at 0 seconds and ends at 86,400 seconds
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

    # Every 600 seconds/10minutes, loop through all charging stations, get information regarding charging, and write into output csv-file
    if step % 600 == 0:
        for cs in cslist:
            if traci.chargingstation.getVehicleCount(cs) == 1 and not (traci.vehicle.getParameter(traci.chargingstation.getVehicleIDs(cs)[0], "device.battery.actualBatteryCapacity") == traci.vehicle.getParameter(traci.chargingstation.getVehicleIDs(cs)[0], "device.battery.maximumBatteryCapacity")):
                writer.writerow([step, cs,'charging',traci.chargingstation.getVehicleIDs(cs)[0],traci.vehicle.getParameter(traci.chargingstation.getVehicleIDs(cs)[0], "device.battery.energyCharged"), traci.vehicle.getParameter(traci.chargingstation.getVehicleIDs(cs)[0], "device.battery.actualBatteryCapacity"), traci.vehicle.getParameter(traci.chargingstation.getVehicleIDs(cs)[0], "device.battery.maximumBatteryCapacity")])
            else:
                writer.writerow([step, cs,'not charging'])

    # Reroute assignments for households that arrive home and start a new trip (second round trip cannot be implemented in the route-file)
    # Make vehicle resume from previous stop, assign new destination, and assign new charging stop at destination

    # HH5 second round trip route assignment to public
    if step == 24600:
        try:
            traci.vehicle.resume("HH_5_EV_1.0")
        except:
            print("Resume Error HH5")
        traci.vehicle.changeTarget("HH_5_EV_1.0", "-162356042#2")
        traci.vehicle.setChargingStationStop("HH_5_EV_1.0", "hh5_ev1_public", flags=32)

        try:
            traci.vehicle.resume("HH_5_EV_2.0")
        except:
            print("Resume Error HH5")
        traci.vehicle.changeTarget("HH_5_EV_2.0", "-14889780#0")
        traci.vehicle.setChargingStationStop("HH_5_EV_2.0", "hh5_ev2_public", flags=32)

        try:
            traci.vehicle.resume("HH_5_EV_3.0")
        except:
            print("Resume Error HH5")
        traci.vehicle.changeTarget("HH_5_EV_3.0", "26300053#6")
        traci.vehicle.setChargingStationStop("HH_5_EV_3.0", "hh5_ev3_public", flags=32)

        try:
            traci.vehicle.resume("HH_5_EV_4.0")
        except:
            print("Resume Error HH5")
        traci.vehicle.changeTarget("HH_5_EV_4.0", "215118939#6")
        traci.vehicle.setChargingStationStop("HH_5_EV_4.0", "hh5_ev4_public", flags=32)

        try:
            traci.vehicle.resume("HH_5_EV_5.0")
        except:
            print("Resume Error HH5")
        traci.vehicle.changeTarget("HH_5_EV_5.0", "152929335#1")
        traci.vehicle.setChargingStationStop("HH_5_EV_5.0", "hh5_ev5_public", flags=32)

        try:
            traci.vehicle.resume("HH_5_EV_6.0")
        except:
            print("Resume Error HH5")
        traci.vehicle.changeTarget("HH_5_EV_6.0", "-128106364#3")
        traci.vehicle.setChargingStationStop("HH_5_EV_6.0", "hh5_ev6_public", flags=32)

        try:
            traci.vehicle.resume("HH_5_EV_7.0")
        except:
            print("Resume Error HH5")
        traci.vehicle.changeTarget("HH_5_EV_7.0", "-27283179#1")
        traci.vehicle.setChargingStationStop("HH_5_EV_7.0", "hh5_ev7_public", flags=32)

        # try:
        #     traci.vehicle.resume("HH_5_EV_8.0")
        # except:
        #     print("Resume Error HH5")
        traci.vehicle.changeTarget("HH_5_EV_8.0", "-346620630#2")
        traci.vehicle.setChargingStationStop("HH_5_EV_8.0", "hh5_ev8_public", flags=32)

        try:
            traci.vehicle.resume("HH_5_EV_9.0")
        except:
            print("Resume Error HH5")
        traci.vehicle.changeTarget("HH_5_EV_9.0", "9702613")
        traci.vehicle.setChargingStationStop("HH_5_EV_9.0", "hh5_ev9_public", flags=32)

        try:
            traci.vehicle.resume("HH_5_EV_10.0")
        except:
            print("Resume Error HH5")
        traci.vehicle.changeTarget("HH_5_EV_10.0", "252808326#1")
        traci.vehicle.setChargingStationStop("HH_5_EV_10.0", "hh5_ev10_public", flags=32)

        try:
            traci.vehicle.resume("HH_5_EV_11.0")
        except:
            print("Resume Error HH5")
        traci.vehicle.changeTarget("HH_5_EV_11.0", "152535296#1")
        traci.vehicle.setChargingStationStop("HH_5_EV_11.0", "hh5_ev11_public", flags=32)


    # HH5 second round trip route assignment to home
    if step == 34800:
        traci.vehicle.resume("HH_5_EV_1.0")
        traci.vehicle.changeTarget("HH_5_EV_1.0", "4492383#0")
        traci.vehicle.setParkingAreaStop("HH_5_EV_1.0", "hh5_ev1_home", flags=32)

        traci.vehicle.resume("HH_5_EV_2.0")
        traci.vehicle.changeTarget("HH_5_EV_2.0", "460974067#0")
        traci.vehicle.setParkingAreaStop("HH_5_EV_2.0", "hh5_ev2_home", flags=32)

        traci.vehicle.resume("HH_5_EV_3.0")
        traci.vehicle.changeTarget("HH_5_EV_3.0", "-219005868")
        traci.vehicle.setChargingStationStop("HH_5_EV_3.0", "hh5_ev3_homecs", flags=32)

        traci.vehicle.resume("HH_5_EV_4.0")
        traci.vehicle.changeTarget("HH_5_EV_4.0", "37629343#1")
        traci.vehicle.setChargingStationStop("HH_5_EV_4.0", "hh5_ev4_homecs", flags=32)

        traci.vehicle.resume("HH_5_EV_5.0")
        traci.vehicle.changeTarget("HH_5_EV_5.0", "231285503#0")
        traci.vehicle.setChargingStationStop("HH_5_EV_5.0", "hh5_ev5_homecs", flags=32)

        traci.vehicle.resume("HH_5_EV_6.0")
        traci.vehicle.changeTarget("HH_5_EV_6.0", "372512041#1")
        traci.vehicle.setChargingStationStop("HH_5_EV_6.0", "hh5_ev6_homecs", flags=32)

        traci.vehicle.resume("HH_5_EV_7.0")
        traci.vehicle.changeTarget("HH_5_EV_7.0", "-41875767#0")
        traci.vehicle.setParkingAreaStop("HH_5_EV_7.0", "hh5_ev7_home", flags=32)

        traci.vehicle.resume("HH_5_EV_8.0")
        traci.vehicle.changeTarget("HH_5_EV_8.0", "-39273150#1")
        traci.vehicle.setChargingStationStop("HH_5_EV_8.0", "hh5_ev8_homecs", flags=32)

        traci.vehicle.resume("HH_5_EV_9.0")
        traci.vehicle.changeTarget("HH_5_EV_9.0", "-383597639#5")
        traci.vehicle.setParkingAreaStop("HH_5_EV_9.0", "hh5_ev9_home", flags=32)

        traci.vehicle.resume("HH_5_EV_10.0")
        traci.vehicle.changeTarget("HH_5_EV_10.0", "-413439173#1")
        traci.vehicle.setChargingStationStop("HH_5_EV_10.0", "hh5_ev10_homecs", flags=32)

        traci.vehicle.resume("HH_5_EV_11.0")
        traci.vehicle.changeTarget("HH_5_EV_11.0", "189764669#0")
        traci.vehicle.setParkingAreaStop("HH_5_EV_11.0", "hh5_ev11_home", flags=32)

        # HH7 second round trip route assignment to public
    if step == 30000:
        traci.vehicle.resume("HH_7_EV_1.0")
        traci.vehicle.changeTarget("HH_7_EV_1.0", "184552213")
        traci.vehicle.setChargingStationStop("HH_7_EV_1.0", "hh7_ev1_public", flags=32)

        traci.vehicle.resume("HH_7_EV_2.0")
        traci.vehicle.changeTarget("HH_7_EV_2.0", "-5199695#3")
        traci.vehicle.setChargingStationStop("HH_7_EV_2.0", "hh7_ev2_public", flags=32)

        traci.vehicle.resume("HH_7_EV_3.0")
        traci.vehicle.changeTarget("HH_7_EV_3.0", "34774347#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_3.0", "hh7_ev3_public", flags=32)

        traci.vehicle.resume("HH_7_EV_4.0")
        traci.vehicle.changeTarget("HH_7_EV_4.0", "161509227#1")
        traci.vehicle.setChargingStationStop("HH_7_EV_4.0", "hh7_ev4_public", flags=32)

        traci.vehicle.resume("HH_7_EV_5.0")
        traci.vehicle.changeTarget("HH_7_EV_5.0", "164298019#2")
        traci.vehicle.setChargingStationStop("HH_7_EV_5.0", "hh7_ev5_public", flags=32)

        traci.vehicle.resume("HH_7_EV_6.0")
        traci.vehicle.changeTarget("HH_7_EV_6.0", "89042181")
        traci.vehicle.setChargingStationStop("HH_7_EV_6.0", "hh7_ev6_public", flags=32)

        traci.vehicle.resume("HH_7_EV_7.0")
        traci.vehicle.changeTarget("HH_7_EV_7.0", "-253534632")
        traci.vehicle.setChargingStationStop("HH_7_EV_7.0", "hh7_ev7_public", flags=32)

        traci.vehicle.resume("HH_7_EV_8.0")
        traci.vehicle.changeTarget("HH_7_EV_8.0", "-24532348#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_8.0", "hh7_ev8_public", flags=32)

        traci.vehicle.resume("HH_7_EV_9.0")
        traci.vehicle.changeTarget("HH_7_EV_9.0", "9702671")
        traci.vehicle.setChargingStationStop("HH_7_EV_9.0", "hh7_ev9_public", flags=32)

        traci.vehicle.resume("HH_7_EV_10.0")
        traci.vehicle.changeTarget("HH_7_EV_10.0", "918744851#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_10.0", "hh7_ev10_public", flags=32)

        traci.vehicle.resume("HH_7_EV_11.0")
        traci.vehicle.changeTarget("HH_7_EV_11.0", "360785921#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_11.0", "hh7_ev11_public", flags=32)

        traci.vehicle.resume("HH_7_EV_12.0")
        traci.vehicle.changeTarget("HH_7_EV_12.0", "-215971171#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_12.0", "hh7_ev12_public", flags=32)

        traci.vehicle.resume("HH_7_EV_13.0")
        traci.vehicle.changeTarget("HH_7_EV_13.0", "246431581#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_13.0", "hh7_ev13_public", flags=32)

        traci.vehicle.resume("HH_7_EV_14.0")
        traci.vehicle.changeTarget("HH_7_EV_14.0", "-340072808#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_14.0", "hh7_ev14_public", flags=32)

        traci.vehicle.resume("HH_7_EV_15.0")
        traci.vehicle.changeTarget("HH_7_EV_15.0", "-502813345#6")
        traci.vehicle.setChargingStationStop("HH_7_EV_15.0", "hh7_ev15_public", flags=32)

        traci.vehicle.resume("HH_7_EV_16.0")
        traci.vehicle.changeTarget("HH_7_EV_16.0", "-223668941#1")
        traci.vehicle.setChargingStationStop("HH_7_EV_16.0", "hh7_ev16_public", flags=32)

        traci.vehicle.resume("HH_7_EV_17.0")
        traci.vehicle.changeTarget("HH_7_EV_17.0", "225534634#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_17.0", "hh7_ev17_public", flags=32)

        traci.vehicle.resume("HH_7_EV_18.0")
        traci.vehicle.changeTarget("HH_7_EV_18.0", "-248560676#1")
        traci.vehicle.setChargingStationStop("HH_7_EV_18.0", "hh7_ev18_public", flags=32)

        traci.vehicle.resume("HH_7_EV_19.0")
        traci.vehicle.changeTarget("HH_7_EV_19.0", "13548585#12")
        traci.vehicle.setChargingStationStop("HH_7_EV_19.0", "hh7_ev19_public", flags=32)

        traci.vehicle.resume("HH_7_EV_20.0")
        traci.vehicle.changeTarget("HH_7_EV_20.0", "-292456704")
        traci.vehicle.setChargingStationStop("HH_7_EV_20.0", "hh7_ev20_public", flags=32)

        traci.vehicle.resume("HH_7_EV_21.0")
        traci.vehicle.changeTarget("HH_7_EV_21.0", "32622556#2")
        traci.vehicle.setChargingStationStop("HH_7_EV_21.0", "hh7_ev21_public", flags=32)

        traci.vehicle.resume("HH_7_EV_22.0")
        traci.vehicle.changeTarget("HH_7_EV_22.0", "360248206#1")
        traci.vehicle.setChargingStationStop("HH_7_EV_22.0", "hh7_ev22_public", flags=32)

        traci.vehicle.resume("HH_7_EV_23.0")
        traci.vehicle.changeTarget("HH_7_EV_23.0", "-163632029#4")
        traci.vehicle.setChargingStationStop("HH_7_EV_23.0", "hh7_ev23_public", flags=32)

        traci.vehicle.resume("HH_7_EV_24.0")
        traci.vehicle.changeTarget("HH_7_EV_24.0", "41269910#1")
        traci.vehicle.setChargingStationStop("HH_7_EV_24.0", "hh7_ev24_public", flags=32)

        traci.vehicle.resume("HH_7_EV_25.0")
        traci.vehicle.changeTarget("HH_7_EV_25.0", "-245795106#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_25.0", "hh7_ev25_public", flags=32)

        traci.vehicle.resume("HH_7_EV_26.0")
        traci.vehicle.changeTarget("HH_7_EV_26.0", "-25873411")
        traci.vehicle.setChargingStationStop("HH_7_EV_26.0", "hh7_ev26_public", flags=32)

        traci.vehicle.resume("HH_7_EV_27.0")
        traci.vehicle.changeTarget("HH_7_EV_27.0", "497514538#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_27.0", "hh7_ev27_public", flags=32)

        traci.vehicle.resume("HH_7_EV_28.0")
        traci.vehicle.changeTarget("HH_7_EV_28.0", "25596040")
        traci.vehicle.setChargingStationStop("HH_7_EV_28.0", "hh7_ev28_public", flags=32)

        traci.vehicle.resume("HH_7_EV_29.0")
        traci.vehicle.changeTarget("HH_7_EV_29.0", "203060224#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_29.0", "hh7_ev29_public", flags=32)

        traci.vehicle.resume("HH_7_EV_30.0")
        traci.vehicle.changeTarget("HH_7_EV_30.0", "-246432091#9")
        traci.vehicle.setChargingStationStop("HH_7_EV_30.0", "hh7_ev30_public", flags=32)

        traci.vehicle.resume("HH_7_EV_31.0")
        traci.vehicle.changeTarget("HH_7_EV_31.0", "-266128538#1")
        traci.vehicle.setChargingStationStop("HH_7_EV_31.0", "hh7_ev31_public", flags=32)

        traci.vehicle.resume("HH_7_EV_32.0")
        traci.vehicle.changeTarget("HH_7_EV_32.0", "-461170673")
        traci.vehicle.setChargingStationStop("HH_7_EV_32.0", "hh7_ev32_public", flags=32)

        traci.vehicle.resume("HH_7_EV_33.0")
        traci.vehicle.changeTarget("HH_7_EV_33.0", "15536634#5")
        traci.vehicle.setChargingStationStop("HH_7_EV_33.0", "hh7_ev33_public", flags=32)

        traci.vehicle.resume("HH_7_EV_34.0")
        traci.vehicle.changeTarget("HH_7_EV_34.0", "15514336#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_34.0", "hh7_ev34_public", flags=32)

        traci.vehicle.resume("HH_7_EV_35.0")
        traci.vehicle.changeTarget("HH_7_EV_35.0", "-443340950#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_35.0", "hh7_ev35_public", flags=32)

        traci.vehicle.resume("HH_7_EV_36.0")
        traci.vehicle.changeTarget("HH_7_EV_36.0", "-197147470#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_36.0", "hh7_ev36_public", flags=32)

        traci.vehicle.resume("HH_7_EV_37.0")
        traci.vehicle.changeTarget("HH_7_EV_37.0", "36787410#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_37.0", "hh7_ev37_public", flags=32)

        traci.vehicle.resume("HH_7_EV_38.0")
        traci.vehicle.changeTarget("HH_7_EV_38.0", "161299459#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_38.0", "hh7_ev38_public", flags=32)

        traci.vehicle.resume("HH_7_EV_39.0")
        traci.vehicle.changeTarget("HH_7_EV_39.0", "-4742868#8")
        traci.vehicle.setChargingStationStop("HH_7_EV_39.0", "hh7_ev39_public", flags=32)

        traci.vehicle.resume("HH_7_EV_40.0")
        traci.vehicle.changeTarget("HH_7_EV_40.0", "118901898#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_40.0", "hh7_ev40_public", flags=32)

        traci.vehicle.resume("HH_7_EV_41.0")
        traci.vehicle.changeTarget("HH_7_EV_41.0", "-190462985")
        traci.vehicle.setChargingStationStop("HH_7_EV_41.0", "hh7_ev41_public", flags=32)

        traci.vehicle.resume("HH_7_EV_42.0")
        traci.vehicle.changeTarget("HH_7_EV_42.0", "267411695")
        traci.vehicle.setChargingStationStop("HH_7_EV_42.0", "hh7_ev42_public", flags=32)

    # HH7 second round trip route assignment to home
    if step == 37200:
        traci.vehicle.resume("HH_7_EV_1.0")
        traci.vehicle.changeTarget("HH_7_EV_1.0", "-10373108#4")
        traci.vehicle.setChargingStationStop("HH_7_EV_1.0", "hh7_ev1_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_2.0")
        traci.vehicle.changeTarget("HH_7_EV_2.0", "-162786681#1")
        traci.vehicle.setParkingAreaStop("HH_7_EV_2.0", "hh7_ev2_home", flags=32)

        traci.vehicle.resume("HH_7_EV_3.0")
        traci.vehicle.changeTarget("HH_7_EV_3.0", "205103380#2")
        traci.vehicle.setParkingAreaStop("HH_7_EV_3.0", "hh7_ev3_home", flags=32)

        traci.vehicle.resume("HH_7_EV_4.0")
        traci.vehicle.changeTarget("HH_7_EV_4.0", "-241893042")
        traci.vehicle.setParkingAreaStop("HH_7_EV_4.0", "hh7_ev4_home", flags=32)

        traci.vehicle.resume("HH_7_EV_5.0")
        traci.vehicle.changeTarget("HH_7_EV_5.0", "251102624#2")
        traci.vehicle.setParkingAreaStop("HH_7_EV_5.0", "hh7_ev5_home", flags=32)

        traci.vehicle.resume("HH_7_EV_6.0")
        traci.vehicle.changeTarget("HH_7_EV_6.0", "-600516727#5")
        traci.vehicle.setParkingAreaStop("HH_7_EV_6.0", "hh7_ev6_home", flags=32)

        traci.vehicle.resume("HH_7_EV_7.0")
        traci.vehicle.changeTarget("HH_7_EV_7.0", "27268712#16")
        traci.vehicle.setParkingAreaStop("HH_7_EV_7.0", "hh7_ev7_home", flags=32)

        traci.vehicle.resume("HH_7_EV_8.0")
        traci.vehicle.changeTarget("HH_7_EV_8.0", "-352929582#5")
        traci.vehicle.setParkingAreaStop("HH_7_EV_8.0", "hh7_ev8_home", flags=32)

        traci.vehicle.resume("HH_7_EV_9.0")
        traci.vehicle.changeTarget("HH_7_EV_9.0", "-37736900")
        traci.vehicle.setChargingStationStop("HH_7_EV_9.0", "hh7_ev9_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_10.0")
        traci.vehicle.changeTarget("HH_7_EV_10.0", "390565776")
        traci.vehicle.setChargingStationStop("HH_7_EV_10.0", "hh7_ev10_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_11.0")
        traci.vehicle.changeTarget("HH_7_EV_11.0", "253498071")
        traci.vehicle.setChargingStationStop("HH_7_EV_11.0", "hh7_ev11_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_12.0")
        traci.vehicle.changeTarget("HH_7_EV_12.0", "55503083#1")
        traci.vehicle.setParkingAreaStop("HH_7_EV_12.0", "hh7_ev12_home", flags=32)

        traci.vehicle.resume("HH_7_EV_13.0")
        traci.vehicle.changeTarget("HH_7_EV_13.0", "685123146")
        traci.vehicle.setParkingAreaStop("HH_7_EV_13.0", "hh7_ev13_home", flags=32)

        traci.vehicle.resume("HH_7_EV_14.0")
        traci.vehicle.changeTarget("HH_7_EV_14.0", "173090898#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_14.0", "hh7_ev14_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_15.0")
        traci.vehicle.changeTarget("HH_7_EV_15.0", "-366630584#2")
        traci.vehicle.setParkingAreaStop("HH_7_EV_15.0", "hh7_ev15_home", flags=32)

        traci.vehicle.resume("HH_7_EV_16.0")
        traci.vehicle.changeTarget("HH_7_EV_16.0", "310396738")
        traci.vehicle.setParkingAreaStop("HH_7_EV_16.0", "hh7_ev16_home", flags=32)

        traci.vehicle.resume("HH_7_EV_17.0")
        traci.vehicle.changeTarget("HH_7_EV_17.0", "94586280#3")
        traci.vehicle.setChargingStationStop("HH_7_EV_17.0", "hh7_ev17_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_18.0")
        traci.vehicle.changeTarget("HH_7_EV_18.0", "387015255#1")
        traci.vehicle.setParkingAreaStop("HH_7_EV_18.0", "hh7_ev18_home", flags=32)

        traci.vehicle.resume("HH_7_EV_19.0")
        traci.vehicle.changeTarget("HH_7_EV_19.0", "181332523#2")
        traci.vehicle.setChargingStationStop("HH_7_EV_19.0", "hh7_ev19_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_20.0")
        traci.vehicle.changeTarget("HH_7_EV_20.0", "-33117536#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_20.0", "hh7_ev20_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_21.0")
        traci.vehicle.changeTarget("HH_7_EV_21.0", "13548399#6")
        traci.vehicle.setParkingAreaStop("HH_7_EV_21.0", "hh7_ev21_home", flags=32)

        traci.vehicle.resume("HH_7_EV_22.0")
        traci.vehicle.changeTarget("HH_7_EV_22.0", "-42731194#1")
        traci.vehicle.setParkingAreaStop("HH_7_EV_22.0", "hh7_ev22_home", flags=32)

        traci.vehicle.resume("HH_7_EV_23.0")
        traci.vehicle.changeTarget("HH_7_EV_23.0", "144375757")
        traci.vehicle.setParkingAreaStop("HH_7_EV_23.0", "hh7_ev23_home", flags=32)

        traci.vehicle.resume("HH_7_EV_24.0")
        traci.vehicle.changeTarget("HH_7_EV_24.0", "189575384#9")
        traci.vehicle.setChargingStationStop("HH_7_EV_24.0", "hh7_ev24_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_25.0")
        traci.vehicle.changeTarget("HH_7_EV_25.0", "5199695#1")
        traci.vehicle.setChargingStationStop("HH_7_EV_25.0", "hh7_ev25_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_26.0")
        traci.vehicle.changeTarget("HH_7_EV_26.0", "204526316#0")
        traci.vehicle.setChargingStationStop("HH_7_EV_26.0", "hh7_ev26_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_27.0")
        traci.vehicle.changeTarget("HH_7_EV_27.0", "14890208#0")
        traci.vehicle.setParkingAreaStop("HH_7_EV_27.0", "hh7_ev27_home", flags=32)

        traci.vehicle.resume("HH_7_EV_28.0")
        traci.vehicle.changeTarget("HH_7_EV_28.0", "-383043275#12")
        traci.vehicle.setParkingAreaStop("HH_7_EV_28.0", "hh7_ev28_home", flags=32)

        traci.vehicle.resume("HH_7_EV_29.0")
        traci.vehicle.changeTarget("HH_7_EV_29.0", "377853509#0")
        traci.vehicle.setParkingAreaStop("HH_7_EV_29.0", "hh7_ev29_home", flags=32)

        traci.vehicle.resume("HH_7_EV_30.0")
        traci.vehicle.changeTarget("HH_7_EV_30.0", "-134394675#3")
        traci.vehicle.setChargingStationStop("HH_7_EV_30.0", "hh7_ev30_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_31.0")
        traci.vehicle.changeTarget("HH_7_EV_31.0", "379469415")
        traci.vehicle.setChargingStationStop("HH_7_EV_31.0", "hh7_ev31_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_32.0")
        traci.vehicle.changeTarget("HH_7_EV_32.0", "620270246#1")
        traci.vehicle.setChargingStationStop("HH_7_EV_32.0", "hh7_ev32_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_33.0")
        traci.vehicle.changeTarget("HH_7_EV_33.0", "101624753")
        traci.vehicle.setParkingAreaStop("HH_7_EV_33.0", "hh7_ev33_home", flags=32)

        traci.vehicle.resume("HH_7_EV_34.0")
        traci.vehicle.changeTarget("HH_7_EV_34.0", "23090192#4")
        traci.vehicle.setParkingAreaStop("HH_7_EV_34.0", "hh7_ev34_home", flags=32)

        traci.vehicle.resume("HH_7_EV_35.0")
        traci.vehicle.changeTarget("HH_7_EV_35.0", "-7976605#11")
        traci.vehicle.setChargingStationStop("HH_7_EV_35.0", "hh7_ev35_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_36.0")
        traci.vehicle.changeTarget("HH_7_EV_36.0", "283999571")
        traci.vehicle.setChargingStationStop("HH_7_EV_36.0", "hh7_ev36_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_37.0")
        traci.vehicle.changeTarget("HH_7_EV_37.0", "-25777951#1")
        traci.vehicle.setChargingStationStop("HH_7_EV_37.0", "hh7_ev37_homecs", flags=32)

        traci.vehicle.resume("HH_7_EV_38.0")
        traci.vehicle.changeTarget("HH_7_EV_38.0", "4087195")
        traci.vehicle.setParkingAreaStop("HH_7_EV_38.0", "hh7_ev38_home", flags=32)

        traci.vehicle.resume("HH_7_EV_39.0")
        traci.vehicle.changeTarget("HH_7_EV_39.0", "-740526378#1")
        traci.vehicle.setParkingAreaStop("HH_7_EV_39.0", "hh7_ev39_home", flags=32)

        traci.vehicle.resume("HH_7_EV_40.0")
        traci.vehicle.changeTarget("HH_7_EV_40.0", "-159227363#0")
        traci.vehicle.setParkingAreaStop("HH_7_EV_40.0", "hh7_ev40_home", flags=32)

        traci.vehicle.resume("HH_7_EV_41.0")
        traci.vehicle.changeTarget("HH_7_EV_41.0", "251531260#3")
        traci.vehicle.setParkingAreaStop("HH_7_EV_41.0", "hh7_ev41_home", flags=32)

        traci.vehicle.resume("HH_7_EV_42.0")
        traci.vehicle.changeTarget("HH_7_EV_42.0", "32860134#4")
        traci.vehicle.setParkingAreaStop("HH_7_EV_42.0", "hh7_ev42_home", flags=32)

    # HH15 second round trip route assignment to public
    if step == 21600:
        #traci.vehicle.resume("HH_15_EV_1.0")
        traci.vehicle.changeTarget("HH_15_EV_1.0", "24600599#0")
        traci.vehicle.setChargingStationStop("HH_15_EV_1.0", "hh15_ev1_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_2.0")
        traci.vehicle.changeTarget("HH_15_EV_2.0", "180358741")
        traci.vehicle.setChargingStationStop("HH_15_EV_2.0", "hh15_ev2_public", flags=32)

        # traci.vehicle.resume("HH_15_EV_3.0")
        traci.vehicle.changeTarget("HH_15_EV_3.0", "-33117536#1")
        traci.vehicle.setChargingStationStop("HH_15_EV_3.0", "hh15_ev3_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_4.0")
        traci.vehicle.changeTarget("HH_15_EV_4.0", "-33359866#3")
        traci.vehicle.setChargingStationStop("HH_15_EV_4.0", "hh15_ev4_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_5.0")
        traci.vehicle.changeTarget("HH_15_EV_5.0", "-144572453#2")
        traci.vehicle.setChargingStationStop("HH_15_EV_5.0", "hh15_ev5_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_6.0")
        traci.vehicle.changeTarget("HH_15_EV_6.0", "178375257#6")
        traci.vehicle.setChargingStationStop("HH_15_EV_6.0", "hh15_ev6_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_7.0")
        traci.vehicle.changeTarget("HH_15_EV_7.0", "48804464#1")
        traci.vehicle.setChargingStationStop("HH_15_EV_7.0", "hh15_ev7_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_8.0")
        traci.vehicle.changeTarget("HH_15_EV_8.0", "30633396#4")
        traci.vehicle.setChargingStationStop("HH_15_EV_8.0", "hh15_ev8_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_9.0")
        traci.vehicle.changeTarget("HH_15_EV_9.0", "-251916658#31")
        traci.vehicle.setChargingStationStop("HH_15_EV_9.0", "hh15_ev9_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_10.0")
        traci.vehicle.changeTarget("HH_15_EV_10.0", "154524779#3")
        traci.vehicle.setChargingStationStop("HH_15_EV_10.0", "hh15_ev10_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_11.0")
        traci.vehicle.changeTarget("HH_15_EV_11.0", "96747828#0")
        traci.vehicle.setChargingStationStop("HH_15_EV_11.0", "hh15_ev11_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_12.0")
        traci.vehicle.changeTarget("HH_15_EV_12.0", "-31976896#5")
        traci.vehicle.setChargingStationStop("HH_15_EV_12.0", "hh15_ev12_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_13.0")
        traci.vehicle.changeTarget("HH_15_EV_13.0", "9702573#1")
        traci.vehicle.setChargingStationStop("HH_15_EV_13.0", "hh15_ev13_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_14.0")
        traci.vehicle.changeTarget("HH_15_EV_14.0", "151390183")
        traci.vehicle.setChargingStationStop("HH_15_EV_14.0", "hh15_ev14_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_15.0")
        traci.vehicle.changeTarget("HH_15_EV_15.0", "148357183#1")
        traci.vehicle.setChargingStationStop("HH_15_EV_15.0", "hh15_ev15_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_16.0")
        traci.vehicle.changeTarget("HH_15_EV_16.0", "-484888712#1")
        traci.vehicle.setChargingStationStop("HH_15_EV_16.0", "hh15_ev16_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_17.0")
        traci.vehicle.changeTarget("HH_15_EV_17.0", "285116007#1")
        traci.vehicle.setChargingStationStop("HH_15_EV_17.0", "hh15_ev17_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_18.0")
        traci.vehicle.changeTarget("HH_15_EV_18.0", "-151116449#1")
        traci.vehicle.setChargingStationStop("HH_15_EV_18.0", "hh15_ev18_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_19.0")
        traci.vehicle.changeTarget("HH_15_EV_19.0", "163979338#16")
        traci.vehicle.setChargingStationStop("HH_15_EV_19.0", "hh15_ev19_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_20.0")
        traci.vehicle.changeTarget("HH_15_EV_20.0", "403467276")
        traci.vehicle.setChargingStationStop("HH_15_EV_20.0", "hh15_ev20_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_21.0")
        traci.vehicle.changeTarget("HH_15_EV_21.0", "-41875770#7")
        traci.vehicle.setChargingStationStop("HH_15_EV_21.0", "hh15_ev21_public", flags=32)

        #traci.vehicle.resume("HH_15_EV_22.0")
        traci.vehicle.changeTarget("HH_15_EV_22.0", "-9675502#9")
        traci.vehicle.setChargingStationStop("HH_15_EV_22.0", "hh15_ev22_public", flags=32)

    # HH15 second round trip route assignment to home
    if step == 37200:
        traci.vehicle.resume("HH_15_EV_1.0")
        traci.vehicle.changeTarget("HH_15_EV_1.0", "-26969367")
        traci.vehicle.setChargingStationStop("HH_15_EV_1.0", "hh15_ev1_homecs", flags=32)

        traci.vehicle.resume("HH_15_EV_2.0")
        traci.vehicle.changeTarget("HH_15_EV_2.0", "-24661460#7")
        traci.vehicle.setParkingAreaStop("HH_15_EV_2.0", "hh15_ev2_home", flags=32)

        traci.vehicle.resume("HH_15_EV_3.0")
        traci.vehicle.changeTarget("HH_15_EV_3.0", "-33173460#0")
        traci.vehicle.setParkingAreaStop("HH_15_EV_3.0", "hh15_ev3_home", flags=32)

        traci.vehicle.resume("HH_15_EV_4.0")
        traci.vehicle.changeTarget("HH_15_EV_4.0", "740526380#1")
        traci.vehicle.setChargingStationStop("HH_15_EV_4.0", "hh15_ev4_homecs", flags=32)

        traci.vehicle.resume("HH_15_EV_5.0")
        traci.vehicle.changeTarget("HH_15_EV_5.0", "30163590#2")
        traci.vehicle.setChargingStationStop("HH_15_EV_5.0", "hh15_ev5_homecs", flags=32)

        traci.vehicle.resume("HH_15_EV_6.0")
        traci.vehicle.changeTarget("HH_15_EV_6.0", "-267411692")
        traci.vehicle.setChargingStationStop("HH_15_EV_6.0", "hh15_ev6_homecs", flags=32)

        traci.vehicle.resume("HH_15_EV_7.0")
        traci.vehicle.changeTarget("HH_15_EV_7.0", "27429629#1")
        traci.vehicle.setParkingAreaStop("HH_15_EV_7.0", "hh15_ev7_home", flags=32)

        traci.vehicle.resume("HH_15_EV_8.0")
        traci.vehicle.changeTarget("HH_15_EV_8.0", "-352929582#4")
        traci.vehicle.setChargingStationStop("HH_15_EV_8.0", "hh15_ev8_homecs", flags=32)

        traci.vehicle.resume("HH_15_EV_9.0")
        traci.vehicle.changeTarget("HH_15_EV_9.0", "-226872065#6")
        traci.vehicle.setParkingAreaStop("HH_15_EV_9.0", "hh15_ev9_home", flags=32)

        traci.vehicle.resume("HH_15_EV_10.0")
        traci.vehicle.changeTarget("HH_15_EV_10.0", "-201973431#3")
        traci.vehicle.setChargingStationStop("HH_15_EV_10.0", "hh15_ev10_homecs", flags=32)

        traci.vehicle.resume("HH_15_EV_11.0")
        traci.vehicle.changeTarget("HH_15_EV_11.0", "-14890193#6")
        traci.vehicle.setChargingStationStop("HH_15_EV_11.0", "hh15_ev11_homecs", flags=32)

        traci.vehicle.resume("HH_15_EV_12.0")
        traci.vehicle.changeTarget("HH_15_EV_12.0", "190340310#0")
        traci.vehicle.setParkingAreaStop("HH_15_EV_12.0", "hh15_ev12_home", flags=32)

        traci.vehicle.resume("HH_15_EV_13.0")
        traci.vehicle.changeTarget("HH_15_EV_13.0", "-39273953#2")
        traci.vehicle.setParkingAreaStop("HH_15_EV_13.0", "hh15_ev13_home", flags=32)

        traci.vehicle.resume("HH_15_EV_14.0")
        traci.vehicle.changeTarget("HH_15_EV_14.0", "183853910#0")
        traci.vehicle.setParkingAreaStop("HH_15_EV_14.0", "hh15_ev14_home", flags=32)

        traci.vehicle.resume("HH_15_EV_15.0")
        traci.vehicle.changeTarget("HH_15_EV_15.0", "163193342#4")
        traci.vehicle.setChargingStationStop("HH_15_EV_15.0", "hh15_ev15_homecs", flags=32)

        traci.vehicle.resume("HH_15_EV_16.0")
        traci.vehicle.changeTarget("HH_15_EV_16.0", "173090455")
        traci.vehicle.setChargingStationStop("HH_15_EV_16.0", "hh15_ev16_homecs", flags=32)

        traci.vehicle.resume("HH_15_EV_17.0")
        traci.vehicle.changeTarget("HH_15_EV_17.0", "-196223594#3")
        traci.vehicle.setParkingAreaStop("HH_15_EV_17.0", "hh15_ev17_home", flags=32)

        traci.vehicle.resume("HH_15_EV_18.0")
        traci.vehicle.changeTarget("HH_15_EV_18.0", "-133781281#0")
        traci.vehicle.setParkingAreaStop("HH_15_EV_18.0", "hh15_ev18_home", flags=32)

        traci.vehicle.resume("HH_15_EV_19.0")
        traci.vehicle.changeTarget("HH_15_EV_19.0", "-149951200#2")
        traci.vehicle.setChargingStationStop("HH_15_EV_19.0", "hh15_ev19_homecs", flags=32)

        traci.vehicle.resume("HH_15_EV_20.0")
        traci.vehicle.changeTarget("HH_15_EV_20.0", "84677514")
        traci.vehicle.setParkingAreaStop("HH_15_EV_20.0", "hh15_ev20_home", flags=32)

        traci.vehicle.resume("HH_15_EV_21.0")
        traci.vehicle.changeTarget("HH_15_EV_21.0", "225775907#0")
        traci.vehicle.setParkingAreaStop("HH_15_EV_21.0", "hh15_ev21_home", flags=32)

        traci.vehicle.resume("HH_15_EV_22.0")
        traci.vehicle.changeTarget("HH_15_EV_22.0", "-4777171#14")
        traci.vehicle.setChargingStationStop("HH_15_EV_22.0", "hh15_ev22_homecs", flags=32)

    # HH8 second round trip route assignment to public
    if step == 34200:
        traci.vehicle.resume("HH_8_EV_1.0")
        traci.vehicle.changeTarget("HH_8_EV_1.0", "-163870254#6")
        traci.vehicle.setChargingStationStop("HH_8_EV_1.0", "hh8_ev1_public", flags=32)

        traci.vehicle.resume("HH_8_EV_2.0")
        traci.vehicle.changeTarget("HH_8_EV_2.0", "122049943#8")
        traci.vehicle.setChargingStationStop("HH_8_EV_2.0", "hh8_ev2_public", flags=32)

        traci.vehicle.resume("HH_8_EV_3.0")
        traci.vehicle.changeTarget("HH_8_EV_3.0", "25851105#4")
        traci.vehicle.setChargingStationStop("HH_8_EV_3.0", "hh8_ev3_public", flags=32)

        traci.vehicle.resume("HH_8_EV_4.0")
        traci.vehicle.changeTarget("HH_8_EV_4.0", "-251916658#11")
        traci.vehicle.setChargingStationStop("HH_8_EV_4.0", "hh8_ev4_public", flags=32)

        traci.vehicle.resume("HH_8_EV_5.0")
        traci.vehicle.changeTarget("HH_8_EV_5.0", "255552313#15")
        traci.vehicle.setChargingStationStop("HH_8_EV_5.0", "hh8_ev5_public", flags=32)

        traci.vehicle.resume("HH_8_EV_6.0")
        traci.vehicle.changeTarget("HH_8_EV_6.0", "-386460303#2")
        traci.vehicle.setChargingStationStop("HH_8_EV_6.0", "hh8_ev6_public", flags=32)

        traci.vehicle.resume("HH_8_EV_7.0")
        traci.vehicle.changeTarget("HH_8_EV_7.0", "24549608")
        traci.vehicle.setChargingStationStop("HH_8_EV_7.0", "hh8_ev7_public", flags=32)

        traci.vehicle.resume("HH_8_EV_8.0")
        traci.vehicle.changeTarget("HH_8_EV_8.0", "328870092")
        traci.vehicle.setChargingStationStop("HH_8_EV_8.0", "hh8_ev8_public", flags=32)

        traci.vehicle.resume("HH_8_EV_9.0")
        traci.vehicle.changeTarget("HH_8_EV_9.0", "5199950#3")
        traci.vehicle.setChargingStationStop("HH_8_EV_9.0", "hh8_ev9_public", flags=32)

        traci.vehicle.resume("HH_8_EV_10.0")
        traci.vehicle.changeTarget("HH_8_EV_10.0", "-172304426")
        traci.vehicle.setChargingStationStop("HH_8_EV_10.0", "hh8_ev10_public", flags=32)

        traci.vehicle.resume("HH_8_EV_11.0")
        traci.vehicle.changeTarget("HH_8_EV_11.0", "-19880821#2")
        traci.vehicle.setChargingStationStop("HH_8_EV_11.0", "hh8_ev11_public", flags=32)

        traci.vehicle.resume("HH_8_EV_12.0")
        traci.vehicle.changeTarget("HH_8_EV_12.0", "13548585#17")
        traci.vehicle.setChargingStationStop("HH_8_EV_12.0", "hh8_ev12_public", flags=32)

        traci.vehicle.resume("HH_8_EV_13.0")
        traci.vehicle.changeTarget("HH_8_EV_13.0", "-218025840")
        traci.vehicle.setChargingStationStop("HH_8_EV_13.0", "hh8_ev13_public", flags=32)

        traci.vehicle.resume("HH_8_EV_14.0")
        traci.vehicle.changeTarget("HH_8_EV_14.0", "225092383#2")
        traci.vehicle.setChargingStationStop("HH_8_EV_14.0", "hh8_ev14_public", flags=32)

        traci.vehicle.resume("HH_8_EV_15.0")
        traci.vehicle.changeTarget("HH_8_EV_15.0", "-24519184#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_15.0", "hh8_ev15_public", flags=32)

        traci.vehicle.resume("HH_8_EV_16.0")
        traci.vehicle.changeTarget("HH_8_EV_16.0", "-233043149#1")
        traci.vehicle.setChargingStationStop("HH_8_EV_16.0", "hh8_ev16_public", flags=32)

        traci.vehicle.resume("HH_8_EV_17.0")
        traci.vehicle.changeTarget("HH_8_EV_17.0", "9675540#1")
        traci.vehicle.setChargingStationStop("HH_8_EV_17.0", "hh8_ev17_public", flags=32)

        traci.vehicle.resume("HH_8_EV_18.0")
        traci.vehicle.changeTarget("HH_8_EV_18.0", "-182457033#2")
        traci.vehicle.setChargingStationStop("HH_8_EV_18.0", "hh8_ev18_public", flags=32)

        traci.vehicle.resume("HH_8_EV_19.0")
        traci.vehicle.changeTarget("HH_8_EV_19.0", "40389027#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_19.0", "hh8_ev19_public", flags=32)

        traci.vehicle.resume("HH_8_EV_20.0")
        traci.vehicle.changeTarget("HH_8_EV_20.0", "-449456918#1")
        traci.vehicle.setChargingStationStop("HH_8_EV_20.0", "hh8_ev20_public", flags=32)

        traci.vehicle.resume("HH_8_EV_21.0")
        traci.vehicle.changeTarget("HH_8_EV_21.0", "14619319#2")
        traci.vehicle.setChargingStationStop("HH_8_EV_21.0", "hh8_ev21_public", flags=32)

        traci.vehicle.resume("HH_8_EV_22.0")
        traci.vehicle.changeTarget("HH_8_EV_22.0", "561432930#4")
        traci.vehicle.setChargingStationStop("HH_8_EV_22.0", "hh8_ev22_public", flags=32)

        traci.vehicle.resume("HH_8_EV_23.0")
        traci.vehicle.changeTarget("HH_8_EV_23.0", "252807529#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_23.0", "hh8_ev23_public", flags=32)

        traci.vehicle.resume("HH_8_EV_24.0")
        traci.vehicle.changeTarget("HH_8_EV_24.0", "644551168#3")
        traci.vehicle.setChargingStationStop("HH_8_EV_24.0", "hh8_ev24_public", flags=32)

        traci.vehicle.resume("HH_8_EV_25.0")
        traci.vehicle.changeTarget("HH_8_EV_25.0", "391897043")
        traci.vehicle.setChargingStationStop("HH_8_EV_25.0", "hh8_ev25_public", flags=32)

        traci.vehicle.resume("HH_8_EV_26.0")
        traci.vehicle.changeTarget("HH_8_EV_26.0", "-344598862")
        traci.vehicle.setChargingStationStop("HH_8_EV_26.0", "hh8_ev26_public", flags=32)

        traci.vehicle.resume("HH_8_EV_27.0")
        traci.vehicle.changeTarget("HH_8_EV_27.0", "-155822524#7")
        traci.vehicle.setChargingStationStop("HH_8_EV_27.0", "hh8_ev27_public", flags=32)

        traci.vehicle.resume("HH_8_EV_28.0")
        traci.vehicle.changeTarget("HH_8_EV_28.0", "10770551#3")
        traci.vehicle.setChargingStationStop("HH_8_EV_28.0", "hh8_ev28_public", flags=32)

        traci.vehicle.resume("HH_8_EV_29.0")
        traci.vehicle.changeTarget("HH_8_EV_29.0", "-32300938#3")
        traci.vehicle.setChargingStationStop("HH_8_EV_29.0", "hh8_ev29_public", flags=32)

        traci.vehicle.resume("HH_8_EV_30.0")
        traci.vehicle.changeTarget("HH_8_EV_30.0", "186668535#1")
        traci.vehicle.setChargingStationStop("HH_8_EV_30.0", "hh8_ev30_public", flags=32)

        traci.vehicle.resume("HH_8_EV_31.0")
        traci.vehicle.changeTarget("HH_8_EV_31.0", "14333498#1")
        traci.vehicle.setChargingStationStop("HH_8_EV_31.0", "hh8_ev31_public", flags=32)

        traci.vehicle.resume("HH_8_EV_32.0")
        traci.vehicle.changeTarget("HH_8_EV_32.0", "-867954114#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_32.0", "hh8_ev32_public", flags=32)

        traci.vehicle.resume("HH_8_EV_33.0")
        traci.vehicle.changeTarget("HH_8_EV_33.0", "39403873")
        traci.vehicle.setChargingStationStop("HH_8_EV_33.0", "hh8_ev33_public", flags=32)

        traci.vehicle.resume("HH_8_EV_34.0")
        traci.vehicle.changeTarget("HH_8_EV_34.0", "18844065#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_34.0", "hh8_ev34_public", flags=32)

        traci.vehicle.resume("HH_8_EV_35.0")
        traci.vehicle.changeTarget("HH_8_EV_35.0", "-190061812#2")
        traci.vehicle.setChargingStationStop("HH_8_EV_35.0", "hh8_ev35_public", flags=32)

        traci.vehicle.resume("HH_8_EV_36.0")
        traci.vehicle.changeTarget("HH_8_EV_36.0", "237278282#3")
        traci.vehicle.setChargingStationStop("HH_8_EV_36.0", "hh8_ev36_public", flags=32)

        traci.vehicle.resume("HH_8_EV_37.0")
        traci.vehicle.changeTarget("HH_8_EV_37.0", "-33440864")
        traci.vehicle.setChargingStationStop("HH_8_EV_37.0", "hh8_ev37_public", flags=32)

        traci.vehicle.resume("HH_8_EV_38.0")
        traci.vehicle.changeTarget("HH_8_EV_38.0", "27153810#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_38.0", "hh8_ev38_public", flags=32)

        #traci.vehicle.resume("HH_8_EV_39.0")
        traci.vehicle.changeTarget("HH_8_EV_39.0", "150743092")
        traci.vehicle.setChargingStationStop("HH_8_EV_39.0", "hh8_ev39_public", flags=32)

        traci.vehicle.resume("HH_8_EV_40.0")
        traci.vehicle.changeTarget("HH_8_EV_40.0", "-346620630#4")
        traci.vehicle.setChargingStationStop("HH_8_EV_40.0", "hh8_ev40_public", flags=32)

        traci.vehicle.resume("HH_8_EV_41.0")
        traci.vehicle.changeTarget("HH_8_EV_41.0", "-12517188#3")
        traci.vehicle.setChargingStationStop("HH_8_EV_41.0", "hh8_ev41_public", flags=32)

        traci.vehicle.resume("HH_8_EV_42.0")
        traci.vehicle.changeTarget("HH_8_EV_42.0", "-204125651#6")
        traci.vehicle.setChargingStationStop("HH_8_EV_42.0", "hh8_ev42_public", flags=32)

        traci.vehicle.resume("HH_8_EV_43.0")
        traci.vehicle.changeTarget("HH_8_EV_43.0", "19354456")
        traci.vehicle.setChargingStationStop("HH_8_EV_43.0", "hh8_ev43_public", flags=32)

        traci.vehicle.resume("HH_8_EV_44.0")
        traci.vehicle.changeTarget("HH_8_EV_44.0", "429104329")
        traci.vehicle.setChargingStationStop("HH_8_EV_44.0", "hh8_ev44_public", flags=32)

        traci.vehicle.resume("HH_8_EV_45.0")
        traci.vehicle.changeTarget("HH_8_EV_45.0", "29494919#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_45.0", "hh8_ev45_public", flags=32)

        traci.vehicle.resume("HH_8_EV_46.0")
        traci.vehicle.changeTarget("HH_8_EV_46.0", "-28725385#4")
        traci.vehicle.setChargingStationStop("HH_8_EV_46.0", "hh8_ev46_public", flags=32)

        traci.vehicle.resume("HH_8_EV_47.0")
        traci.vehicle.changeTarget("HH_8_EV_47.0", "-148727312#1")
        traci.vehicle.setChargingStationStop("HH_8_EV_47.0", "hh8_ev47_public", flags=32)

        traci.vehicle.resume("HH_8_EV_48.0")
        traci.vehicle.changeTarget("HH_8_EV_48.0", "328005193#2")
        traci.vehicle.setChargingStationStop("HH_8_EV_48.0", "hh8_ev48_public", flags=32)

        traci.vehicle.resume("HH_8_EV_49.0")
        traci.vehicle.changeTarget("HH_8_EV_49.0", "190443686")
        traci.vehicle.setChargingStationStop("HH_8_EV_49.0", "hh8_ev49_public", flags=32)

        traci.vehicle.resume("HH_8_EV_50.0")
        traci.vehicle.changeTarget("HH_8_EV_50.0", "749296219#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_50.0", "hh8_ev50_public", flags=32)

        traci.vehicle.resume("HH_8_EV_51.0")
        traci.vehicle.changeTarget("HH_8_EV_51.0", "26195766#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_51.0", "hh8_ev51_public", flags=32)

        traci.vehicle.resume("HH_8_EV_52.0")
        traci.vehicle.changeTarget("HH_8_EV_52.0", "175632257#6")
        traci.vehicle.setChargingStationStop("HH_8_EV_52.0", "hh8_ev52_public", flags=32)

        traci.vehicle.resume("HH_8_EV_53.0")
        traci.vehicle.changeTarget("HH_8_EV_53.0", "-30617718#1")
        traci.vehicle.setChargingStationStop("HH_8_EV_53.0", "hh8_ev53_public", flags=32)

        traci.vehicle.resume("HH_8_EV_54.0")
        traci.vehicle.changeTarget("HH_8_EV_54.0", "-29504037")
        traci.vehicle.setChargingStationStop("HH_8_EV_54.0", "hh8_ev54_public", flags=32)

        traci.vehicle.resume("HH_8_EV_55.0")
        traci.vehicle.changeTarget("HH_8_EV_55.0", "317929536")
        traci.vehicle.setChargingStationStop("HH_8_EV_55.0", "hh8_ev55_public", flags=32)

        traci.vehicle.resume("HH_8_EV_56.0")
        traci.vehicle.changeTarget("HH_8_EV_56.0", "-121102974#1")
        traci.vehicle.setChargingStationStop("HH_8_EV_56.0", "hh8_ev56_public", flags=32)

        traci.vehicle.resume("HH_8_EV_57.0")
        traci.vehicle.changeTarget("HH_8_EV_57.0", "-150857994#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_57.0", "hh8_ev57_public", flags=32)

        traci.vehicle.resume("HH_8_EV_58.0")
        traci.vehicle.changeTarget("HH_8_EV_58.0", "749288424#2")
        traci.vehicle.setChargingStationStop("HH_8_EV_58.0", "hh8_ev58_public", flags=32)

        traci.vehicle.resume("HH_8_EV_59.0")
        traci.vehicle.changeTarget("HH_8_EV_59.0", "161299879#3")
        traci.vehicle.setChargingStationStop("HH_8_EV_59.0", "hh8_ev59_public", flags=32)

        traci.vehicle.resume("HH_8_EV_60.0")
        traci.vehicle.changeTarget("HH_8_EV_60.0", "-555550047")
        traci.vehicle.setChargingStationStop("HH_8_EV_60.0", "hh8_ev60_public", flags=32)

        traci.vehicle.resume("HH_8_EV_61.0")
        traci.vehicle.changeTarget("HH_8_EV_61.0", "169827537")
        traci.vehicle.setChargingStationStop("HH_8_EV_61.0", "hh8_ev61_public", flags=32)

        traci.vehicle.resume("HH_8_EV_62.0")
        traci.vehicle.changeTarget("HH_8_EV_62.0", "208424711#2")
        traci.vehicle.setChargingStationStop("HH_8_EV_62.0", "hh8_ev62_public", flags=32)

        traci.vehicle.resume("HH_8_EV_63.0")
        traci.vehicle.changeTarget("HH_8_EV_63.0", "-157458262#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_63.0", "hh8_ev63_public", flags=32)

        traci.vehicle.resume("HH_8_EV_64.0")
        traci.vehicle.changeTarget("HH_8_EV_64.0", "40104609#7")
        traci.vehicle.setChargingStationStop("HH_8_EV_64.0", "hh8_ev64_public", flags=32)

        traci.vehicle.resume("HH_8_EV_65.0")
        traci.vehicle.changeTarget("HH_8_EV_65.0", "251850519#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_65.0", "hh8_ev65_public", flags=32)

        traci.vehicle.resume("HH_8_EV_66.0")
        traci.vehicle.changeTarget("HH_8_EV_66.0", "-337329718#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_66.0", "hh8_ev66_public", flags=32)

        traci.vehicle.resume("HH_8_EV_67.0")
        traci.vehicle.changeTarget("HH_8_EV_67.0", "161116616#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_67.0", "hh8_ev67_public", flags=32)

        traci.vehicle.resume("HH_8_EV_68.0")
        traci.vehicle.changeTarget("HH_8_EV_68.0", "40822187#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_68.0", "hh8_ev68_public", flags=32)

        traci.vehicle.resume("HH_8_EV_69.0")
        traci.vehicle.changeTarget("HH_8_EV_69.0", "-40711855#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_69.0", "hh8_ev69_public", flags=32)

        traci.vehicle.resume("HH_8_EV_70.0")
        traci.vehicle.changeTarget("HH_8_EV_70.0", "-189575384#8")
        traci.vehicle.setChargingStationStop("HH_8_EV_70.0", "hh8_ev70_public", flags=32)

        traci.vehicle.resume("HH_8_EV_71.0")
        traci.vehicle.changeTarget("HH_8_EV_71.0", "-295678416#0")
        traci.vehicle.setChargingStationStop("HH_8_EV_71.0", "hh8_ev71_public", flags=32)

        traci.vehicle.resume("HH_8_EV_72.0")
        traci.vehicle.changeTarget("HH_8_EV_72.0", "383597641#6")
        traci.vehicle.setChargingStationStop("HH_8_EV_72.0", "hh8_ev72_public", flags=32)

        traci.vehicle.resume("HH_8_EV_73.0")
        traci.vehicle.changeTarget("HH_8_EV_73.0", "178238209#4")
        traci.vehicle.setChargingStationStop("HH_8_EV_73.0", "hh8_ev73_public", flags=32)

    # HH8 second round trip route assignment to home
    if step == 41400:
        traci.vehicle.resume("HH_8_EV_1.0")
        traci.vehicle.changeTarget("HH_8_EV_1.0", "-39273150#1")
        traci.vehicle.setParkingAreaStop("HH_8_EV_1.0", "hh8_ev1_home", flags=32)

        traci.vehicle.resume("HH_8_EV_2.0")
        traci.vehicle.changeTarget("HH_8_EV_2.0", "223859973")
        traci.vehicle.setParkingAreaStop("HH_8_EV_2.0", "hh8_ev2_home", flags=32)

        traci.vehicle.resume("HH_8_EV_3.0")
        traci.vehicle.changeTarget("HH_8_EV_3.0", "-119057970#1")
        traci.vehicle.setParkingAreaStop("HH_8_EV_3.0", "hh8_ev3_home", flags=32)

        traci.vehicle.resume("HH_8_EV_4.0")
        traci.vehicle.changeTarget("HH_8_EV_4.0", "-39649667")
        traci.vehicle.setParkingAreaStop("HH_8_EV_4.0", "hh8_ev4_home", flags=32)

        traci.vehicle.resume("HH_8_EV_5.0")
        traci.vehicle.changeTarget("HH_8_EV_5.0", "4914448#3")
        traci.vehicle.setParkingAreaStop("HH_8_EV_5.0", "hh8_ev5_home", flags=32)

        traci.vehicle.resume("HH_8_EV_6.0")
        traci.vehicle.changeTarget("HH_8_EV_6.0", "-170720179#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_6.0", "hh8_ev6_home", flags=32)

        traci.vehicle.resume("HH_8_EV_7.0")
        traci.vehicle.changeTarget("HH_8_EV_7.0", "371970668")
        traci.vehicle.setParkingAreaStop("HH_8_EV_7.0", "hh8_ev7_home", flags=32)

        traci.vehicle.resume("HH_8_EV_8.0")
        traci.vehicle.changeTarget("HH_8_EV_8.0", "357343725#3")
        traci.vehicle.setParkingAreaStop("HH_8_EV_8.0", "hh8_ev8_home", flags=32)

        traci.vehicle.resume("HH_8_EV_9.0")
        traci.vehicle.changeTarget("HH_8_EV_9.0", "156144197#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_9.0", "hh8_ev9_home", flags=32)

        traci.vehicle.resume("HH_8_EV_10.0")
        traci.vehicle.changeTarget("HH_8_EV_10.0", "204207296#10")
        traci.vehicle.setParkingAreaStop("HH_8_EV_10.0", "hh8_ev10_home", flags=32)

        traci.vehicle.resume("HH_8_EV_11.0")
        traci.vehicle.changeTarget("HH_8_EV_11.0", "14308534#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_11.0", "hh8_ev11_home", flags=32)

        traci.vehicle.resume("HH_8_EV_12.0")
        traci.vehicle.changeTarget("HH_8_EV_12.0", "216879571")
        traci.vehicle.setParkingAreaStop("HH_8_EV_12.0", "hh8_ev12_home", flags=32)

        traci.vehicle.resume("HH_8_EV_13.0")
        traci.vehicle.changeTarget("HH_8_EV_13.0", "-25950529#10")
        traci.vehicle.setParkingAreaStop("HH_8_EV_13.0", "hh8_ev13_home", flags=32)

        traci.vehicle.resume("HH_8_EV_14.0")
        traci.vehicle.changeTarget("HH_8_EV_14.0", "-31097396")
        traci.vehicle.setParkingAreaStop("HH_8_EV_14.0", "hh8_ev14_home", flags=32)

        traci.vehicle.resume("HH_8_EV_15.0")
        traci.vehicle.changeTarget("HH_8_EV_15.0", "-27330922#9")
        traci.vehicle.setParkingAreaStop("HH_8_EV_15.0", "hh8_ev15_home", flags=32)

        traci.vehicle.resume("HH_8_EV_16.0")
        traci.vehicle.changeTarget("HH_8_EV_16.0", "-195003520#2")
        traci.vehicle.setParkingAreaStop("HH_8_EV_16.0", "hh8_ev16_home", flags=32)

        traci.vehicle.resume("HH_8_EV_17.0")
        traci.vehicle.changeTarget("HH_8_EV_17.0", "27706046#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_17.0", "hh8_ev17_home", flags=32)

        traci.vehicle.resume("HH_8_EV_18.0")
        traci.vehicle.changeTarget("HH_8_EV_18.0", "-126924211#1")
        traci.vehicle.setParkingAreaStop("HH_8_EV_18.0", "hh8_ev18_home", flags=32)

        traci.vehicle.resume("HH_8_EV_19.0")
        traci.vehicle.changeTarget("HH_8_EV_19.0", "-41267858#4")
        traci.vehicle.setParkingAreaStop("HH_8_EV_19.0", "hh8_ev19_home", flags=32)

        traci.vehicle.resume("HH_8_EV_20.0")
        traci.vehicle.changeTarget("HH_8_EV_20.0", "8616276#3")
        traci.vehicle.setParkingAreaStop("HH_8_EV_20.0", "hh8_ev20_home", flags=32)

        traci.vehicle.resume("HH_8_EV_21.0")
        traci.vehicle.changeTarget("HH_8_EV_21.0", "-26264132#5")
        traci.vehicle.setParkingAreaStop("HH_8_EV_21.0", "hh8_ev21_home", flags=32)

        traci.vehicle.resume("HH_8_EV_22.0")
        traci.vehicle.changeTarget("HH_8_EV_22.0", "-245656508")
        traci.vehicle.setParkingAreaStop("HH_8_EV_22.0", "hh8_ev22_home", flags=32)

        traci.vehicle.resume("HH_8_EV_23.0")
        traci.vehicle.changeTarget("HH_8_EV_23.0", "32958043#3")
        traci.vehicle.setParkingAreaStop("HH_8_EV_23.0", "hh8_ev23_home", flags=32)

        traci.vehicle.resume("HH_8_EV_24.0")
        traci.vehicle.changeTarget("HH_8_EV_24.0", "28725380#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_24.0", "hh8_ev24_home", flags=32)

        traci.vehicle.resume("HH_8_EV_25.0")
        traci.vehicle.changeTarget("HH_8_EV_25.0", "81663335#2")
        traci.vehicle.setParkingAreaStop("HH_8_EV_25.0", "hh8_ev25_home", flags=32)

        traci.vehicle.resume("HH_8_EV_26.0")
        traci.vehicle.changeTarget("HH_8_EV_26.0", "-187987511#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_26.0", "hh8_ev26_home", flags=32)

        traci.vehicle.resume("HH_8_EV_27.0")
        traci.vehicle.changeTarget("HH_8_EV_27.0", "7976600#1")
        traci.vehicle.setParkingAreaStop("HH_8_EV_27.0", "hh8_ev27_home", flags=32)

        traci.vehicle.resume("HH_8_EV_28.0")
        traci.vehicle.changeTarget("HH_8_EV_28.0", "48467262#7")
        traci.vehicle.setParkingAreaStop("HH_8_EV_28.0", "hh8_ev28_home", flags=32)

        traci.vehicle.resume("HH_8_EV_29.0")
        traci.vehicle.changeTarget("HH_8_EV_29.0", "-159226914#8")
        traci.vehicle.setParkingAreaStop("HH_8_EV_29.0", "hh8_ev29_home", flags=32)

        traci.vehicle.resume("HH_8_EV_30.0")
        traci.vehicle.changeTarget("HH_8_EV_30.0", "-14307948#2")
        traci.vehicle.setParkingAreaStop("HH_8_EV_30.0", "hh8_ev30_home", flags=32)

        traci.vehicle.resume("HH_8_EV_31.0")
        traci.vehicle.changeTarget("HH_8_EV_31.0", "-542719233")
        traci.vehicle.setParkingAreaStop("HH_8_EV_31.0", "hh8_ev31_home", flags=32)

        traci.vehicle.resume("HH_8_EV_32.0")
        traci.vehicle.changeTarget("HH_8_EV_32.0", "379098550#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_32.0", "hh8_ev32_home", flags=32)

        traci.vehicle.resume("HH_8_EV_33.0")
        traci.vehicle.changeTarget("HH_8_EV_33.0", "-28655996")
        traci.vehicle.setParkingAreaStop("HH_8_EV_33.0", "hh8_ev33_home", flags=32)

        traci.vehicle.resume("HH_8_EV_34.0")
        traci.vehicle.changeTarget("HH_8_EV_34.0", "4235269#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_34.0", "hh8_ev34_home", flags=32)

        traci.vehicle.resume("HH_8_EV_35.0")
        traci.vehicle.changeTarget("HH_8_EV_35.0", "-31976919#12")
        traci.vehicle.setParkingAreaStop("HH_8_EV_35.0", "hh8_ev35_home", flags=32)

        traci.vehicle.resume("HH_8_EV_36.0")
        traci.vehicle.changeTarget("HH_8_EV_36.0", "684446735#4")
        traci.vehicle.setParkingAreaStop("HH_8_EV_36.0", "hh8_ev36_home", flags=32)

        traci.vehicle.resume("HH_8_EV_37.0")
        traci.vehicle.changeTarget("HH_8_EV_37.0", "136819324#1")
        traci.vehicle.setParkingAreaStop("HH_8_EV_37.0", "hh8_ev37_home", flags=32)

        traci.vehicle.resume("HH_8_EV_38.0")
        traci.vehicle.changeTarget("HH_8_EV_38.0", "15569569#4")
        traci.vehicle.setParkingAreaStop("HH_8_EV_38.0", "hh8_ev38_home", flags=32)

        try:
            traci.vehicle.resume("HH_8_EV_39.0")
        except:
            print("Resume Error HH8")
        traci.vehicle.changeTarget("HH_8_EV_39.0", "-17479197#17")
        traci.vehicle.setParkingAreaStop("HH_8_EV_39.0", "hh8_ev39_home", flags=32)

        traci.vehicle.resume("HH_8_EV_40.0")
        traci.vehicle.changeTarget("HH_8_EV_40.0", "-175543490")
        traci.vehicle.setParkingAreaStop("HH_8_EV_40.0", "hh8_ev40_home", flags=32)

        traci.vehicle.resume("HH_8_EV_41.0")
        traci.vehicle.changeTarget("HH_8_EV_41.0", "-238870176#2")
        traci.vehicle.setParkingAreaStop("HH_8_EV_41.0", "hh8_ev41_home", flags=32)

        traci.vehicle.resume("HH_8_EV_42.0")
        traci.vehicle.changeTarget("HH_8_EV_42.0", "126924211#5")
        traci.vehicle.setParkingAreaStop("HH_8_EV_42.0", "hh8_ev42_home", flags=32)

        traci.vehicle.resume("HH_8_EV_43.0")
        traci.vehicle.changeTarget("HH_8_EV_43.0", "161116087#1")
        traci.vehicle.setParkingAreaStop("HH_8_EV_43.0", "hh8_ev43_home", flags=32)

        traci.vehicle.resume("HH_8_EV_44.0")
        traci.vehicle.changeTarget("HH_8_EV_44.0", "-163193342#3")
        traci.vehicle.setParkingAreaStop("HH_8_EV_44.0", "hh8_ev44_home", flags=32)

        traci.vehicle.resume("HH_8_EV_45.0")
        traci.vehicle.changeTarget("HH_8_EV_45.0", "5488391#3")
        traci.vehicle.setParkingAreaStop("HH_8_EV_45.0", "hh8_ev45_home", flags=32)

        traci.vehicle.resume("HH_8_EV_46.0")
        traci.vehicle.changeTarget("HH_8_EV_46.0", "-27435074#8")
        traci.vehicle.setParkingAreaStop("HH_8_EV_46.0", "hh8_ev46_home", flags=32)

        traci.vehicle.resume("HH_8_EV_47.0")
        traci.vehicle.changeTarget("HH_8_EV_47.0", "-24532138#3")
        traci.vehicle.setParkingAreaStop("HH_8_EV_47.0", "hh8_ev47_home", flags=32)

        traci.vehicle.resume("HH_8_EV_48.0")
        traci.vehicle.changeTarget("HH_8_EV_48.0", "-35014371#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_48.0", "hh8_ev48_home", flags=32)

        traci.vehicle.resume("HH_8_EV_49.0")
        traci.vehicle.changeTarget("HH_8_EV_49.0", "-12517187#3")
        traci.vehicle.setParkingAreaStop("HH_8_EV_49.0", "hh8_ev49_home", flags=32)

        traci.vehicle.resume("HH_8_EV_50.0")
        traci.vehicle.changeTarget("HH_8_EV_50.0", "-43688837#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_50.0", "hh8_ev50_home", flags=32)

        traci.vehicle.resume("HH_8_EV_51.0")
        traci.vehicle.changeTarget("HH_8_EV_51.0", "175552323#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_51.0", "hh8_ev51_home", flags=32)

        traci.vehicle.resume("HH_8_EV_52.0")
        traci.vehicle.changeTarget("HH_8_EV_52.0", "-181332523#2")
        traci.vehicle.setParkingAreaStop("HH_8_EV_52.0", "hh8_ev52_home", flags=32)

        traci.vehicle.resume("HH_8_EV_53.0")
        traci.vehicle.changeTarget("HH_8_EV_53.0", "28825901#4")
        traci.vehicle.setParkingAreaStop("HH_8_EV_53.0", "hh8_ev53_home", flags=32)

        traci.vehicle.resume("HH_8_EV_54.0")
        traci.vehicle.changeTarget("HH_8_EV_54.0", "-4777395#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_54.0", "hh8_ev54_home", flags=32)

        traci.vehicle.resume("HH_8_EV_55.0")
        traci.vehicle.changeTarget("HH_8_EV_55.0", "-32445778#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_55.0", "hh8_ev55_home", flags=32)

        traci.vehicle.resume("HH_8_EV_56.0")
        traci.vehicle.changeTarget("HH_8_EV_56.0", "30059413#2")
        traci.vehicle.setParkingAreaStop("HH_8_EV_56.0", "hh8_ev56_home", flags=32)

        traci.vehicle.resume("HH_8_EV_57.0")
        traci.vehicle.changeTarget("HH_8_EV_57.0", "401549270#1")
        traci.vehicle.setParkingAreaStop("HH_8_EV_57.0", "hh8_ev57_home", flags=32)

        traci.vehicle.resume("HH_8_EV_58.0")
        traci.vehicle.changeTarget("HH_8_EV_58.0", "-28725385#11")
        traci.vehicle.setParkingAreaStop("HH_8_EV_58.0", "hh8_ev58_home", flags=32)

        traci.vehicle.resume("HH_8_EV_59.0")
        traci.vehicle.changeTarget("HH_8_EV_59.0", "-205190519")
        traci.vehicle.setParkingAreaStop("HH_8_EV_59.0", "hh8_ev59_home", flags=32)

        traci.vehicle.resume("HH_8_EV_60.0")
        traci.vehicle.changeTarget("HH_8_EV_60.0", "-149951202#1")
        traci.vehicle.setParkingAreaStop("HH_8_EV_60.0", "hh8_ev60_home", flags=32)

        traci.vehicle.resume("HH_8_EV_61.0")
        traci.vehicle.changeTarget("HH_8_EV_61.0", "33439898#3")
        traci.vehicle.setParkingAreaStop("HH_8_EV_61.0", "hh8_ev61_home", flags=32)

        traci.vehicle.resume("HH_8_EV_62.0")
        traci.vehicle.changeTarget("HH_8_EV_62.0", "89042181")
        traci.vehicle.setParkingAreaStop("HH_8_EV_62.0", "hh8_ev62_home", flags=32)

        traci.vehicle.resume("HH_8_EV_63.0")
        traci.vehicle.changeTarget("HH_8_EV_63.0", "386261792")
        traci.vehicle.setParkingAreaStop("HH_8_EV_63.0", "hh8_ev63_home", flags=32)

        traci.vehicle.resume("HH_8_EV_64.0")
        traci.vehicle.changeTarget("HH_8_EV_64.0", "52461311#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_64.0", "hh8_ev64_home", flags=32)

        traci.vehicle.resume("HH_8_EV_65.0")
        traci.vehicle.changeTarget("HH_8_EV_65.0", "-35951655#2")
        traci.vehicle.setParkingAreaStop("HH_8_EV_65.0", "hh8_ev65_home", flags=32)

        traci.vehicle.resume("HH_8_EV_66.0")
        traci.vehicle.changeTarget("HH_8_EV_66.0", "-32384270#5")
        traci.vehicle.setParkingAreaStop("HH_8_EV_66.0", "hh8_ev66_home", flags=32)

        traci.vehicle.resume("HH_8_EV_67.0")
        traci.vehicle.changeTarget("HH_8_EV_67.0", "-28218608#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_67.0", "hh8_ev67_home", flags=32)

        traci.vehicle.resume("HH_8_EV_68.0")
        traci.vehicle.changeTarget("HH_8_EV_68.0", "187998964")
        traci.vehicle.setParkingAreaStop("HH_8_EV_68.0", "hh8_ev68_home", flags=32)

        traci.vehicle.resume("HH_8_EV_69.0")
        traci.vehicle.changeTarget("HH_8_EV_69.0", "25556710#4")
        traci.vehicle.setParkingAreaStop("HH_8_EV_69.0", "hh8_ev69_home", flags=32)

        traci.vehicle.resume("HH_8_EV_70.0")
        traci.vehicle.changeTarget("HH_8_EV_70.0", "-32762556#5")
        traci.vehicle.setParkingAreaStop("HH_8_EV_70.0", "hh8_ev70_home", flags=32)

        traci.vehicle.resume("HH_8_EV_71.0")
        traci.vehicle.changeTarget("HH_8_EV_71.0", "-24554176#2")
        traci.vehicle.setParkingAreaStop("HH_8_EV_71.0", "hh8_ev71_home", flags=32)

        traci.vehicle.resume("HH_8_EV_72.0")
        traci.vehicle.changeTarget("HH_8_EV_72.0", "258979205#0")
        traci.vehicle.setParkingAreaStop("HH_8_EV_72.0", "hh8_ev72_home", flags=32)

        traci.vehicle.resume("HH_8_EV_73.0")
        traci.vehicle.changeTarget("HH_8_EV_73.0", "-142322446#2")
        traci.vehicle.setParkingAreaStop("HH_8_EV_73.0", "hh8_ev73_home", flags=32)

    # HH16 second round trip route assignment to public
    if step == 37200:
        traci.vehicle.resume("HH_16_EV_1.0")
        traci.vehicle.changeTarget("HH_16_EV_1.0", "15237395#6")
        traci.vehicle.setChargingStationStop("HH_16_EV_1.0", "hh16_ev1_public", flags=32)

        traci.vehicle.resume("HH_16_EV_2.0")
        traci.vehicle.changeTarget("HH_16_EV_2.0", "-27124649#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_2.0", "hh16_ev2_public", flags=32)

        traci.vehicle.resume("HH_16_EV_3.0")
        traci.vehicle.changeTarget("HH_16_EV_3.0", "-9675502#11")
        traci.vehicle.setChargingStationStop("HH_16_EV_3.0", "hh16_ev3_public", flags=32)

        traci.vehicle.resume("HH_16_EV_4.0")
        traci.vehicle.changeTarget("HH_16_EV_4.0", "84677514")
        traci.vehicle.setChargingStationStop("HH_16_EV_4.0", "hh16_ev4_public", flags=32)

        traci.vehicle.resume("HH_16_EV_5.0")
        traci.vehicle.changeTarget("HH_16_EV_5.0", "204207296#9")
        traci.vehicle.setChargingStationStop("HH_16_EV_5.0", "hh16_ev5_public", flags=32)

        traci.vehicle.resume("HH_16_EV_6.0")
        traci.vehicle.changeTarget("HH_16_EV_6.0", "34961876#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_6.0", "hh16_ev6_public", flags=32)

        traci.vehicle.resume("HH_16_EV_7.0")
        traci.vehicle.changeTarget("HH_16_EV_7.0", "-182896775#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_7.0", "hh16_ev7_public", flags=32)

        traci.vehicle.resume("HH_16_EV_8.0")
        traci.vehicle.changeTarget("HH_16_EV_8.0", "-32448174#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_8.0", "hh16_ev8_public", flags=32)

        traci.vehicle.resume("HH_16_EV_9.0")
        traci.vehicle.changeTarget("HH_16_EV_9.0", "-32622580#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_9.0", "hh16_ev9_public", flags=32)

        traci.vehicle.resume("HH_16_EV_10.0")
        traci.vehicle.changeTarget("HH_16_EV_10.0", "121966831#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_10.0", "hh16_ev10_public", flags=32)

        traci.vehicle.resume("HH_16_EV_11.0")
        traci.vehicle.changeTarget("HH_16_EV_11.0", "267967582")
        traci.vehicle.setChargingStationStop("HH_16_EV_11.0", "hh16_ev11_public", flags=32)

        traci.vehicle.resume("HH_16_EV_12.0")
        traci.vehicle.changeTarget("HH_16_EV_12.0", "52374136#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_12.0", "hh16_ev12_public", flags=32)

        traci.vehicle.resume("HH_16_EV_13.0")
        traci.vehicle.changeTarget("HH_16_EV_13.0", "200355059#5")
        traci.vehicle.setChargingStationStop("HH_16_EV_13.0", "hh16_ev13_public", flags=32)

        traci.vehicle.resume("HH_16_EV_14.0")
        traci.vehicle.changeTarget("HH_16_EV_14.0", "121817376#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_14.0", "hh16_ev14_public", flags=32)

        traci.vehicle.resume("HH_16_EV_15.0")
        traci.vehicle.changeTarget("HH_16_EV_15.0", "18671875#4")
        traci.vehicle.setChargingStationStop("HH_16_EV_15.0", "hh16_ev15_public", flags=32)

        traci.vehicle.resume("HH_16_EV_16.0")
        traci.vehicle.changeTarget("HH_16_EV_16.0", "38913732#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_16.0", "hh16_ev16_public", flags=32)

        traci.vehicle.resume("HH_16_EV_17.0")
        traci.vehicle.changeTarget("HH_16_EV_17.0", "-442545005")
        traci.vehicle.setChargingStationStop("HH_16_EV_17.0", "hh16_ev17_public", flags=32)

        traci.vehicle.resume("HH_16_EV_18.0")
        traci.vehicle.changeTarget("HH_16_EV_18.0", "9702544#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_18.0", "hh16_ev18_public", flags=32)

        traci.vehicle.resume("HH_16_EV_19.0")
        traci.vehicle.changeTarget("HH_16_EV_19.0", "146826697")
        traci.vehicle.setChargingStationStop("HH_16_EV_19.0", "hh16_ev19_public", flags=32)

        traci.vehicle.resume("HH_16_EV_20.0")
        traci.vehicle.changeTarget("HH_16_EV_20.0", "28825902#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_20.0", "hh16_ev20_public", flags=32)

        traci.vehicle.resume("HH_16_EV_21.0")
        traci.vehicle.changeTarget("HH_16_EV_21.0", "364957859")
        traci.vehicle.setChargingStationStop("HH_16_EV_21.0", "hh16_ev21_public", flags=32)

        traci.vehicle.resume("HH_16_EV_22.0")
        traci.vehicle.changeTarget("HH_16_EV_22.0", "33117532")
        traci.vehicle.setChargingStationStop("HH_16_EV_22.0", "hh16_ev22_public", flags=32)

        traci.vehicle.resume("HH_16_EV_23.0")
        traci.vehicle.changeTarget("HH_16_EV_23.0", "56185660#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_23.0", "hh16_ev23_public", flags=32)

        traci.vehicle.resume("HH_16_EV_24.0")
        traci.vehicle.changeTarget("HH_16_EV_24.0", "-17479197#12")
        traci.vehicle.setChargingStationStop("HH_16_EV_24.0", "hh16_ev24_public", flags=32)

        traci.vehicle.resume("HH_16_EV_25.0")
        traci.vehicle.changeTarget("HH_16_EV_25.0", "15389633")
        traci.vehicle.setChargingStationStop("HH_16_EV_25.0", "hh16_ev25_public", flags=32)

        traci.vehicle.resume("HH_16_EV_26.0")
        traci.vehicle.changeTarget("HH_16_EV_26.0", "27329943#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_26.0", "hh16_ev26_public", flags=32)

        traci.vehicle.resume("HH_16_EV_27.0")
        traci.vehicle.changeTarget("HH_16_EV_27.0", "-227668809#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_27.0", "hh16_ev27_public", flags=32)

        traci.vehicle.resume("HH_16_EV_28.0")
        traci.vehicle.changeTarget("HH_16_EV_28.0", "558331773")
        traci.vehicle.setChargingStationStop("HH_16_EV_28.0", "hh16_ev28_public", flags=32)

        traci.vehicle.resume("HH_16_EV_29.0")
        traci.vehicle.changeTarget("HH_16_EV_29.0", "-255460838#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_29.0", "hh16_ev29_public", flags=32)

        traci.vehicle.resume("HH_16_EV_30.0")
        traci.vehicle.changeTarget("HH_16_EV_30.0", "-226238008#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_30.0", "hh16_ev30_public", flags=32)

        traci.vehicle.resume("HH_16_EV_31.0")
        traci.vehicle.changeTarget("HH_16_EV_31.0", "150146634")
        traci.vehicle.setChargingStationStop("HH_16_EV_31.0", "hh16_ev31_public", flags=32)

        traci.vehicle.resume("HH_16_EV_32.0")
        traci.vehicle.changeTarget("HH_16_EV_32.0", "-338523208")
        traci.vehicle.setChargingStationStop("HH_16_EV_32.0", "hh16_ev32_public", flags=32)

        traci.vehicle.resume("HH_16_EV_33.0")
        traci.vehicle.changeTarget("HH_16_EV_33.0", "27529610")
        traci.vehicle.setChargingStationStop("HH_16_EV_33.0", "hh16_ev33_public", flags=32)

        traci.vehicle.resume("HH_16_EV_34.0")
        traci.vehicle.changeTarget("HH_16_EV_34.0", "-209767602#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_34.0", "hh16_ev34_public", flags=32)

        traci.vehicle.resume("HH_16_EV_35.0")
        traci.vehicle.changeTarget("HH_16_EV_35.0", "121144959#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_35.0", "hh16_ev35_public", flags=32)

        traci.vehicle.resume("HH_16_EV_36.0")
        traci.vehicle.changeTarget("HH_16_EV_36.0", "160616788#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_36.0", "hh16_ev36_public", flags=32)

        traci.vehicle.resume("HH_16_EV_37.0")
        traci.vehicle.changeTarget("HH_16_EV_37.0", "778957162")
        traci.vehicle.setChargingStationStop("HH_16_EV_37.0", "hh16_ev37_public", flags=32)

        traci.vehicle.resume("HH_16_EV_38.0")
        traci.vehicle.changeTarget("HH_16_EV_38.0", "225775909#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_38.0", "hh16_ev38_public", flags=32)

        traci.vehicle.resume("HH_16_EV_39.0")
        traci.vehicle.changeTarget("HH_16_EV_39.0", "-31152919")
        traci.vehicle.setChargingStationStop("HH_16_EV_39.0", "hh16_ev39_public", flags=32)

        traci.vehicle.resume("HH_16_EV_40.0")
        traci.vehicle.changeTarget("HH_16_EV_40.0", "182084305#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_40.0", "hh16_ev40_public", flags=32)

        traci.vehicle.resume("HH_16_EV_41.0")
        traci.vehicle.changeTarget("HH_16_EV_41.0", "84176718#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_41.0", "hh16_ev41_public", flags=32)

        traci.vehicle.resume("HH_16_EV_42.0")
        traci.vehicle.changeTarget("HH_16_EV_42.0", "27401821#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_42.0", "hh16_ev42_public", flags=32)

        traci.vehicle.resume("HH_16_EV_43.0")
        traci.vehicle.changeTarget("HH_16_EV_43.0", "-29494918#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_43.0", "hh16_ev43_public", flags=32)

        traci.vehicle.resume("HH_16_EV_44.0")
        traci.vehicle.changeTarget("HH_16_EV_44.0", "10373108#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_44.0", "hh16_ev44_public", flags=32)

        traci.vehicle.resume("HH_16_EV_45.0")
        traci.vehicle.changeTarget("HH_16_EV_45.0", "147301307#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_45.0", "hh16_ev45_public", flags=32)

        traci.vehicle.resume("HH_16_EV_46.0")
        traci.vehicle.changeTarget("HH_16_EV_46.0", "240348395#5")
        traci.vehicle.setChargingStationStop("HH_16_EV_46.0", "hh16_ev46_public", flags=32)

        traci.vehicle.resume("HH_16_EV_47.0")
        traci.vehicle.changeTarget("HH_16_EV_47.0", "-182044419")
        traci.vehicle.setChargingStationStop("HH_16_EV_47.0", "hh16_ev47_public", flags=32)

        traci.vehicle.resume("HH_16_EV_48.0")
        traci.vehicle.changeTarget("HH_16_EV_48.0", "144429614")
        traci.vehicle.setChargingStationStop("HH_16_EV_48.0", "hh16_ev48_public", flags=32)

        traci.vehicle.resume("HH_16_EV_49.0")
        traci.vehicle.changeTarget("HH_16_EV_49.0", "-500378536#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_49.0", "hh16_ev49_public", flags=32)

        traci.vehicle.resume("HH_16_EV_50.0")
        traci.vehicle.changeTarget("HH_16_EV_50.0", "288096398#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_50.0", "hh16_ev50_public", flags=32)

        traci.vehicle.resume("HH_16_EV_51.0")
        traci.vehicle.changeTarget("HH_16_EV_51.0", "229133280#5")
        traci.vehicle.setChargingStationStop("HH_16_EV_51.0", "hh16_ev51_public", flags=32)

        traci.vehicle.resume("HH_16_EV_52.0")
        traci.vehicle.changeTarget("HH_16_EV_52.0", "-150697174#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_52.0", "hh16_ev52_public", flags=32)

        traci.vehicle.resume("HH_16_EV_53.0")
        traci.vehicle.changeTarget("HH_16_EV_53.0", "251256299")
        traci.vehicle.setChargingStationStop("HH_16_EV_53.0", "hh16_ev53_public", flags=32)

        traci.vehicle.resume("HH_16_EV_54.0")
        traci.vehicle.changeTarget("HH_16_EV_54.0", "159242785#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_54.0", "hh16_ev54_public", flags=32)

        traci.vehicle.resume("HH_16_EV_55.0")
        traci.vehicle.changeTarget("HH_16_EV_55.0", "21905102#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_55.0", "hh16_ev55_public", flags=32)

        traci.vehicle.resume("HH_16_EV_56.0")
        traci.vehicle.changeTarget("HH_16_EV_56.0", "554223268")
        traci.vehicle.setChargingStationStop("HH_16_EV_56.0", "hh16_ev56_public", flags=32)

        traci.vehicle.resume("HH_16_EV_57.0")
        traci.vehicle.changeTarget("HH_16_EV_57.0", "25950296#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_57.0", "hh16_ev57_public", flags=32)

        traci.vehicle.resume("HH_16_EV_58.0")
        traci.vehicle.changeTarget("HH_16_EV_58.0", "-33117527#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_58.0", "hh16_ev58_public", flags=32)

        traci.vehicle.resume("HH_16_EV_59.0")
        traci.vehicle.changeTarget("HH_16_EV_59.0", "215971176#6")
        traci.vehicle.setChargingStationStop("HH_16_EV_59.0", "hh16_ev59_public", flags=32)

        traci.vehicle.resume("HH_16_EV_60.0")
        traci.vehicle.changeTarget("HH_16_EV_60.0", "40309035#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_60.0", "hh16_ev60_public", flags=32)

        traci.vehicle.resume("HH_16_EV_61.0")
        traci.vehicle.changeTarget("HH_16_EV_61.0", "-41269342#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_61.0", "hh16_ev61_public", flags=32)

        traci.vehicle.resume("HH_16_EV_62.0")
        traci.vehicle.changeTarget("HH_16_EV_62.0", "-26969495#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_62.0", "hh16_ev62_public", flags=32)

        traci.vehicle.resume("HH_16_EV_63.0")
        traci.vehicle.changeTarget("HH_16_EV_63.0", "-246432091#5")
        traci.vehicle.setChargingStationStop("HH_16_EV_63.0", "hh16_ev63_public", flags=32)

        traci.vehicle.resume("HH_16_EV_64.0")
        traci.vehicle.changeTarget("HH_16_EV_64.0", "-27435069#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_64.0", "hh16_ev64_public", flags=32)

        traci.vehicle.resume("HH_16_EV_65.0")
        traci.vehicle.changeTarget("HH_16_EV_65.0", "-374052771#8")
        traci.vehicle.setChargingStationStop("HH_16_EV_65.0", "hh16_ev65_public", flags=32)

        traci.vehicle.resume("HH_16_EV_66.0")
        traci.vehicle.changeTarget("HH_16_EV_66.0", "-37881517#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_66.0", "hh16_ev66_public", flags=32)

        traci.vehicle.resume("HH_16_EV_67.0")
        traci.vehicle.changeTarget("HH_16_EV_67.0", "577952363")
        traci.vehicle.setChargingStationStop("HH_16_EV_67.0", "hh16_ev67_public", flags=32)

        traci.vehicle.resume("HH_16_EV_68.0")
        traci.vehicle.changeTarget("HH_16_EV_68.0", "146403342")
        traci.vehicle.setChargingStationStop("HH_16_EV_68.0", "hh16_ev68_public", flags=32)

        traci.vehicle.resume("HH_16_EV_69.0")
        traci.vehicle.changeTarget("HH_16_EV_69.0", "27330922#4")
        traci.vehicle.setChargingStationStop("HH_16_EV_69.0", "hh16_ev69_public", flags=32)

        traci.vehicle.resume("HH_16_EV_70.0")
        traci.vehicle.changeTarget("HH_16_EV_70.0", "-32977407#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_70.0", "hh16_ev70_public", flags=32)

        traci.vehicle.resume("HH_16_EV_71.0")
        traci.vehicle.changeTarget("HH_16_EV_71.0", "-215971173#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_71.0", "hh16_ev71_public", flags=32)

        traci.vehicle.resume("HH_16_EV_72.0")
        traci.vehicle.changeTarget("HH_16_EV_72.0", "-163632029#7")
        traci.vehicle.setChargingStationStop("HH_16_EV_72.0", "hh16_ev72_public", flags=32)

        traci.vehicle.resume("HH_16_EV_73.0")
        traci.vehicle.changeTarget("HH_16_EV_73.0", "-549690624")
        traci.vehicle.setChargingStationStop("HH_16_EV_73.0", "hh16_ev73_public", flags=32)

        traci.vehicle.resume("HH_16_EV_74.0")
        traci.vehicle.changeTarget("HH_16_EV_74.0", "-260866561#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_74.0", "hh16_ev74_public", flags=32)

        traci.vehicle.resume("HH_16_EV_75.0")
        traci.vehicle.changeTarget("HH_16_EV_75.0", "-253848481#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_75.0", "hh16_ev75_public", flags=32)

        traci.vehicle.resume("HH_16_EV_76.0")
        traci.vehicle.changeTarget("HH_16_EV_76.0", "-15568893#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_76.0", "hh16_ev76_public", flags=32)

        traci.vehicle.resume("HH_16_EV_77.0")
        traci.vehicle.changeTarget("HH_16_EV_77.0", "225528129")
        traci.vehicle.setChargingStationStop("HH_16_EV_77.0", "hh16_ev77_public", flags=32)

        traci.vehicle.resume("HH_16_EV_78.0")
        traci.vehicle.changeTarget("HH_16_EV_78.0", "161125365#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_78.0", "hh16_ev78_public", flags=32)

        traci.vehicle.resume("HH_16_EV_79.0")
        traci.vehicle.changeTarget("HH_16_EV_79.0", "161114859#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_79.0", "hh16_ev79_public", flags=32)

        traci.vehicle.resume("HH_16_EV_80.0")
        traci.vehicle.changeTarget("HH_16_EV_80.0", "-25950295#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_80.0", "hh16_ev80_public", flags=32)

        traci.vehicle.resume("HH_16_EV_81.0")
        traci.vehicle.changeTarget("HH_16_EV_81.0", "204207290#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_81.0", "hh16_ev81_public", flags=32)

        traci.vehicle.resume("HH_16_EV_82.0")
        traci.vehicle.changeTarget("HH_16_EV_82.0", "-34655504#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_82.0", "hh16_ev82_public", flags=32)

        traci.vehicle.resume("HH_16_EV_83.0")
        traci.vehicle.changeTarget("HH_16_EV_83.0", "-8616276#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_83.0", "hh16_ev83_public", flags=32)

        traci.vehicle.resume("HH_16_EV_84.0")
        traci.vehicle.changeTarget("HH_16_EV_84.0", "-187977271")
        traci.vehicle.setChargingStationStop("HH_16_EV_84.0", "hh16_ev84_public", flags=32)

        traci.vehicle.resume("HH_16_EV_85.0")
        traci.vehicle.changeTarget("HH_16_EV_85.0", "-51366102#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_85.0", "hh16_ev85_public", flags=32)

        traci.vehicle.resume("HH_16_EV_86.0")
        traci.vehicle.changeTarget("HH_16_EV_86.0", "-413439173#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_86.0", "hh16_ev86_public", flags=32)

        traci.vehicle.resume("HH_16_EV_87.0")
        traci.vehicle.changeTarget("HH_16_EV_87.0", "-4914451#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_87.0", "hh16_ev87_public", flags=32)

        traci.vehicle.resume("HH_16_EV_88.0")
        traci.vehicle.changeTarget("HH_16_EV_88.0", "136819324#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_88.0", "hh16_ev88_public", flags=32)

        traci.vehicle.resume("HH_16_EV_89.0")
        traci.vehicle.changeTarget("HH_16_EV_89.0", "366630591#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_89.0", "hh16_ev89_public", flags=32)

        traci.vehicle.resume("HH_16_EV_90.0")
        traci.vehicle.changeTarget("HH_16_EV_90.0", "29494919#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_90.0", "hh16_ev90_public", flags=32)

        traci.vehicle.resume("HH_16_EV_91.0")
        traci.vehicle.changeTarget("HH_16_EV_91.0", "-33205896#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_91.0", "hh16_ev91_public", flags=32)

        traci.vehicle.resume("HH_16_EV_92.0")
        traci.vehicle.changeTarget("HH_16_EV_92.0", "-128878530")
        traci.vehicle.setChargingStationStop("HH_16_EV_92.0", "hh16_ev92_public", flags=32)

        traci.vehicle.resume("HH_16_EV_93.0")
        traci.vehicle.changeTarget("HH_16_EV_93.0", "683697133#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_93.0", "hh16_ev93_public", flags=32)

        traci.vehicle.resume("HH_16_EV_94.0")
        traci.vehicle.changeTarget("HH_16_EV_94.0", "222046778#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_94.0", "hh16_ev94_public", flags=32)

        traci.vehicle.resume("HH_16_EV_95.0")
        traci.vehicle.changeTarget("HH_16_EV_95.0", "35773267#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_95.0", "hh16_ev95_public", flags=32)

        traci.vehicle.resume("HH_16_EV_96.0")
        traci.vehicle.changeTarget("HH_16_EV_96.0", "26969566#4")
        traci.vehicle.setChargingStationStop("HH_16_EV_96.0", "hh16_ev96_public", flags=32)

        traci.vehicle.resume("HH_16_EV_97.0")
        traci.vehicle.changeTarget("HH_16_EV_97.0", "30633396#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_97.0", "hh16_ev97_public", flags=32)

        traci.vehicle.resume("HH_16_EV_98.0")
        traci.vehicle.changeTarget("HH_16_EV_98.0", "23863086#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_98.0", "hh16_ev98_public", flags=32)

        try:
            traci.vehicle.resume("HH_16_EV_99.0")
        except:
            print("Resume Error HH5")
        traci.vehicle.changeTarget("HH_16_EV_99.0", "-30057718#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_99.0", "hh16_ev99_public", flags=32)

        traci.vehicle.resume("HH_16_EV_100.0")
        traci.vehicle.changeTarget("HH_16_EV_100.0", "116214595")
        traci.vehicle.setChargingStationStop("HH_16_EV_100.0", "hh16_ev100_public", flags=32)

        traci.vehicle.resume("HH_16_EV_101.0")
        traci.vehicle.changeTarget("HH_16_EV_101.0", "173090898#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_101.0", "hh16_ev101_public", flags=32)

        traci.vehicle.resume("HH_16_EV_102.0")
        traci.vehicle.changeTarget("HH_16_EV_102.0", "279303998")
        traci.vehicle.setChargingStationStop("HH_16_EV_102.0", "hh16_ev102_public", flags=32)

        traci.vehicle.resume("HH_16_EV_103.0")
        traci.vehicle.changeTarget("HH_16_EV_103.0", "550668395")
        traci.vehicle.setChargingStationStop("HH_16_EV_103.0", "hh16_ev103_public", flags=32)

        traci.vehicle.resume("HH_16_EV_104.0")
        traci.vehicle.changeTarget("HH_16_EV_104.0", "32860134#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_104.0", "hh16_ev104_public", flags=32)

        traci.vehicle.resume("HH_16_EV_105.0")
        traci.vehicle.changeTarget("HH_16_EV_105.0", "-37804697#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_105.0", "hh16_ev105_public", flags=32)

        traci.vehicle.resume("HH_16_EV_106.0")
        traci.vehicle.changeTarget("HH_16_EV_106.0", "917497450#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_106.0", "hh16_ev106_public", flags=32)

        traci.vehicle.resume("HH_16_EV_107.0")
        traci.vehicle.changeTarget("HH_16_EV_107.0", "118080561#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_107.0", "hh16_ev107_public", flags=32)

        traci.vehicle.resume("HH_16_EV_108.0")
        traci.vehicle.changeTarget("HH_16_EV_108.0", "253508450#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_108.0", "hh16_ev108_public", flags=32)

        traci.vehicle.resume("HH_16_EV_109.0")
        traci.vehicle.changeTarget("HH_16_EV_109.0", "93178198#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_109.0", "hh16_ev109_public", flags=32)

        traci.vehicle.resume("HH_16_EV_110.0")
        traci.vehicle.changeTarget("HH_16_EV_110.0", "-164297567#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_110.0", "hh16_ev110_public", flags=32)

        traci.vehicle.resume("HH_16_EV_111.0")
        traci.vehicle.changeTarget("HH_16_EV_111.0", "152398678#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_111.0", "hh16_ev111_public", flags=32)

        traci.vehicle.resume("HH_16_EV_112.0")
        traci.vehicle.changeTarget("HH_16_EV_112.0", "-390565779")
        traci.vehicle.setChargingStationStop("HH_16_EV_112.0", "hh16_ev112_public", flags=32)

        traci.vehicle.resume("HH_16_EV_113.0")
        traci.vehicle.changeTarget("HH_16_EV_113.0", "163199440")
        traci.vehicle.setChargingStationStop("HH_16_EV_113.0", "hh16_ev113_public", flags=32)

        traci.vehicle.resume("HH_16_EV_114.0")
        traci.vehicle.changeTarget("HH_16_EV_114.0", "852475938#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_114.0", "hh16_ev114_public", flags=32)

        try:
            traci.vehicle.resume("HH_16_EV_115.0")
        except:
            print("Resume Error HH16")
        traci.vehicle.changeTarget("HH_16_EV_115.0", "29504039#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_115.0", "hh16_ev115_public", flags=32)

        traci.vehicle.resume("HH_16_EV_116.0")
        traci.vehicle.changeTarget("HH_16_EV_116.0", "-48494257#5")
        traci.vehicle.setChargingStationStop("HH_16_EV_116.0", "hh16_ev116_public", flags=32)

        traci.vehicle.resume("HH_16_EV_117.0")
        traci.vehicle.changeTarget("HH_16_EV_117.0", "246432125#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_117.0", "hh16_ev117_public", flags=32)

        traci.vehicle.resume("HH_16_EV_118.0")
        traci.vehicle.changeTarget("HH_16_EV_118.0", "227062819#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_118.0", "hh16_ev118_public", flags=32)

        traci.vehicle.resume("HH_16_EV_119.0")
        traci.vehicle.changeTarget("HH_16_EV_119.0", "-39273945#5")
        traci.vehicle.setChargingStationStop("HH_16_EV_119.0", "hh16_ev119_public", flags=32)

        traci.vehicle.resume("HH_16_EV_120.0")
        traci.vehicle.changeTarget("HH_16_EV_120.0", "-163870005#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_120.0", "hh16_ev120_public", flags=32)

        traci.vehicle.resume("HH_16_EV_121.0")
        traci.vehicle.changeTarget("HH_16_EV_121.0", "-121797362#5")
        traci.vehicle.setChargingStationStop("HH_16_EV_121.0", "hh16_ev121_public", flags=32)

        traci.vehicle.resume("HH_16_EV_122.0")
        traci.vehicle.changeTarget("HH_16_EV_122.0", "405312618")
        traci.vehicle.setChargingStationStop("HH_16_EV_122.0", "hh16_ev122_public", flags=32)

        traci.vehicle.resume("HH_16_EV_123.0")
        traci.vehicle.changeTarget("HH_16_EV_123.0", "27593144#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_123.0", "hh16_ev123_public", flags=32)

        traci.vehicle.resume("HH_16_EV_124.0")
        traci.vehicle.changeTarget("HH_16_EV_124.0", "-196841089#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_124.0", "hh16_ev124_public", flags=32)

        traci.vehicle.resume("HH_16_EV_125.0")
        traci.vehicle.changeTarget("HH_16_EV_125.0", "-32881615#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_125.0", "hh16_ev125_public", flags=32)

        traci.vehicle.resume("HH_16_EV_126.0")
        traci.vehicle.changeTarget("HH_16_EV_126.0", "-21904941#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_126.0", "hh16_ev126_public", flags=32)

        traci.vehicle.resume("HH_16_EV_127.0")
        traci.vehicle.changeTarget("HH_16_EV_127.0", "129702720#4")
        traci.vehicle.setChargingStationStop("HH_16_EV_127.0", "hh16_ev127_public", flags=32)

        traci.vehicle.resume("HH_16_EV_128.0")
        traci.vehicle.changeTarget("HH_16_EV_128.0", "-37847013#6")
        traci.vehicle.setChargingStationStop("HH_16_EV_128.0", "hh16_ev128_public", flags=32)

        traci.vehicle.resume("HH_16_EV_129.0")
        traci.vehicle.changeTarget("HH_16_EV_129.0", "-33440562#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_129.0", "hh16_ev129_public", flags=32)

        traci.vehicle.resume("HH_16_EV_130.0")
        traci.vehicle.changeTarget("HH_16_EV_130.0", "-159226246#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_130.0", "hh16_ev130_public", flags=32)

        traci.vehicle.resume("HH_16_EV_131.0")
        traci.vehicle.changeTarget("HH_16_EV_131.0", "161482157#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_131.0", "hh16_ev131_public", flags=32)

        traci.vehicle.resume("HH_16_EV_132.0")
        traci.vehicle.changeTarget("HH_16_EV_132.0", "223171223")
        traci.vehicle.setChargingStationStop("HH_16_EV_132.0", "hh16_ev132_public", flags=32)

        traci.vehicle.resume("HH_16_EV_133.0")
        traci.vehicle.changeTarget("HH_16_EV_133.0", "-161544526")
        traci.vehicle.setChargingStationStop("HH_16_EV_133.0", "hh16_ev133_public", flags=32)

        traci.vehicle.resume("HH_16_EV_134.0")
        traci.vehicle.changeTarget("HH_16_EV_134.0", "-40711858#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_134.0", "hh16_ev134_public", flags=32)

        traci.vehicle.resume("HH_16_EV_135.0")
        traci.vehicle.changeTarget("HH_16_EV_135.0", "33457172")
        traci.vehicle.setChargingStationStop("HH_16_EV_135.0", "hh16_ev135_public", flags=32)

        traci.vehicle.resume("HH_16_EV_136.0")
        traci.vehicle.changeTarget("HH_16_EV_136.0", "439850262#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_136.0", "hh16_ev136_public", flags=32)

    # HH16 second round trip route assignment to home
    if step == 42000:
        traci.vehicle.resume("HH_16_EV_1.0")
        traci.vehicle.changeTarget("HH_16_EV_1.0", "41206587#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_1.0", "hh16_ev1_home", flags=32)

        traci.vehicle.resume("HH_16_EV_2.0")
        traci.vehicle.changeTarget("HH_16_EV_2.0", "556954636#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_2.0", "hh16_ev2_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_3.0")
        traci.vehicle.changeTarget("HH_16_EV_3.0", "-18823658#2")
        traci.vehicle.setParkingAreaStop("HH_16_EV_3.0", "hh16_ev3_home", flags=32)

        traci.vehicle.resume("HH_16_EV_4.0")
        traci.vehicle.changeTarget("HH_16_EV_4.0", "-204207296#11")
        traci.vehicle.setParkingAreaStop("HH_16_EV_4.0", "hh16_ev4_home", flags=32)

        traci.vehicle.resume("HH_16_EV_5.0")
        traci.vehicle.changeTarget("HH_16_EV_5.0", "-302156370#2")
        traci.vehicle.setParkingAreaStop("HH_16_EV_5.0", "hh16_ev5_home", flags=32)

        traci.vehicle.resume("HH_16_EV_6.0")
        traci.vehicle.changeTarget("HH_16_EV_6.0", "24600596")
        traci.vehicle.setParkingAreaStop("HH_16_EV_6.0", "hh16_ev6_home", flags=32)

        traci.vehicle.resume("HH_16_EV_7.0")
        traci.vehicle.changeTarget("HH_16_EV_7.0", "155951646#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_7.0", "hh16_ev7_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_8.0")
        traci.vehicle.changeTarget("HH_16_EV_8.0", "194765169#2")
        traci.vehicle.setParkingAreaStop("HH_16_EV_8.0", "hh16_ev8_home", flags=32)

        traci.vehicle.resume("HH_16_EV_9.0")
        traci.vehicle.changeTarget("HH_16_EV_9.0", "277905155")
        traci.vehicle.setChargingStationStop("HH_16_EV_9.0", "hh16_ev9_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_10.0")
        traci.vehicle.changeTarget("HH_16_EV_10.0", "-354362667#6")
        traci.vehicle.setChargingStationStop("HH_16_EV_10.0", "hh16_ev10_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_11.0")
        traci.vehicle.changeTarget("HH_16_EV_11.0", "-15216164#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_11.0", "hh16_ev11_home", flags=32)

        traci.vehicle.resume("HH_16_EV_12.0")
        traci.vehicle.changeTarget("HH_16_EV_12.0", "-39403875#2")
        traci.vehicle.setParkingAreaStop("HH_16_EV_12.0", "hh16_ev12_home", flags=32)

        traci.vehicle.resume("HH_16_EV_13.0")
        traci.vehicle.changeTarget("HH_16_EV_13.0", "-364071765#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_13.0", "hh16_ev13_home", flags=32)

        traci.vehicle.resume("HH_16_EV_14.0")
        traci.vehicle.changeTarget("HH_16_EV_14.0", "-313869321")
        traci.vehicle.setParkingAreaStop("HH_16_EV_14.0", "hh16_ev14_home", flags=32)

        traci.vehicle.resume("HH_16_EV_15.0")
        traci.vehicle.changeTarget("HH_16_EV_15.0", "-33080713#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_15.0", "hh16_ev15_home", flags=32)

        traci.vehicle.resume("HH_16_EV_16.0")
        traci.vehicle.changeTarget("HH_16_EV_16.0", "-142322426#6")
        traci.vehicle.setParkingAreaStop("HH_16_EV_16.0", "hh16_ev16_home", flags=32)

        traci.vehicle.resume("HH_16_EV_17.0")
        traci.vehicle.changeTarget("HH_16_EV_17.0", "338663462#2")
        traci.vehicle.setParkingAreaStop("HH_16_EV_17.0", "hh16_ev17_home", flags=32)

        traci.vehicle.resume("HH_16_EV_18.0")
        traci.vehicle.changeTarget("HH_16_EV_18.0", "29280244")
        traci.vehicle.setParkingAreaStop("HH_16_EV_18.0", "hh16_ev18_home", flags=32)

        traci.vehicle.resume("HH_16_EV_19.0")
        traci.vehicle.changeTarget("HH_16_EV_19.0", "-155822489#3")
        traci.vehicle.setParkingAreaStop("HH_16_EV_19.0", "hh16_ev19_home", flags=32)

        traci.vehicle.resume("HH_16_EV_20.0")
        traci.vehicle.changeTarget("HH_16_EV_20.0", "118094455#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_20.0", "hh16_ev20_home", flags=32)

        traci.vehicle.resume("HH_16_EV_21.0")
        traci.vehicle.changeTarget("HH_16_EV_21.0", "31976896#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_21.0", "hh16_ev21_home", flags=32)

        traci.vehicle.resume("HH_16_EV_22.0")
        traci.vehicle.changeTarget("HH_16_EV_22.0", "-740526381#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_22.0", "hh16_ev22_home", flags=32)

        traci.vehicle.resume("HH_16_EV_23.0")
        traci.vehicle.changeTarget("HH_16_EV_23.0", "128079844#3")
        traci.vehicle.setParkingAreaStop("HH_16_EV_23.0", "hh16_ev23_home", flags=32)

        traci.vehicle.resume("HH_16_EV_24.0")
        traci.vehicle.changeTarget("HH_16_EV_24.0", "320166773#4")
        traci.vehicle.setChargingStationStop("HH_16_EV_24.0", "hh16_ev24_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_25.0")
        traci.vehicle.changeTarget("HH_16_EV_25.0", "-46963653#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_25.0", "hh16_ev25_home", flags=32)

        traci.vehicle.resume("HH_16_EV_26.0")
        traci.vehicle.changeTarget("HH_16_EV_26.0", "-5488391#13")
        traci.vehicle.setParkingAreaStop("HH_16_EV_26.0", "hh16_ev26_home", flags=32)

        traci.vehicle.resume("HH_16_EV_27.0")
        traci.vehicle.changeTarget("HH_16_EV_27.0", "249224806#4")
        traci.vehicle.setParkingAreaStop("HH_16_EV_27.0", "hh16_ev27_home", flags=32)

        traci.vehicle.resume("HH_16_EV_28.0")
        traci.vehicle.changeTarget("HH_16_EV_28.0", "-30617953#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_28.0", "hh16_ev28_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_29.0")
        traci.vehicle.changeTarget("HH_16_EV_29.0", "-29021275#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_29.0", "hh16_ev29_home", flags=32)

        traci.vehicle.resume("HH_16_EV_30.0")
        traci.vehicle.changeTarget("HH_16_EV_30.0", "-175632257#7")
        traci.vehicle.setParkingAreaStop("HH_16_EV_30.0", "hh16_ev30_home", flags=32)

        traci.vehicle.resume("HH_16_EV_31.0")
        traci.vehicle.changeTarget("HH_16_EV_31.0", "-170720179#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_31.0", "hh16_ev31_home", flags=32)

        traci.vehicle.resume("HH_16_EV_32.0")
        traci.vehicle.changeTarget("HH_16_EV_32.0", "-14890665#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_32.0", "hh16_ev32_home", flags=32)

        traci.vehicle.resume("HH_16_EV_33.0")
        traci.vehicle.changeTarget("HH_16_EV_33.0", "-34773050#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_33.0", "hh16_ev33_home", flags=32)

        traci.vehicle.resume("HH_16_EV_34.0")
        traci.vehicle.changeTarget("HH_16_EV_34.0", "-5942831")
        traci.vehicle.setParkingAreaStop("HH_16_EV_34.0", "hh16_ev34_home", flags=32)

        traci.vehicle.resume("HH_16_EV_35.0")
        traci.vehicle.changeTarget("HH_16_EV_35.0", "-169070536#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_35.0", "hh16_ev35_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_36.0")
        traci.vehicle.changeTarget("HH_16_EV_36.0", "-266188220#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_36.0", "hh16_ev36_home", flags=32)

        traci.vehicle.resume("HH_16_EV_37.0")
        traci.vehicle.changeTarget("HH_16_EV_37.0", "-8024199#3")
        traci.vehicle.setParkingAreaStop("HH_16_EV_37.0", "hh16_ev37_home", flags=32)

        traci.vehicle.resume("HH_16_EV_38.0")
        traci.vehicle.changeTarget("HH_16_EV_38.0", "-18844186#4")
        traci.vehicle.setParkingAreaStop("HH_16_EV_38.0", "hh16_ev38_home", flags=32)

        traci.vehicle.resume("HH_16_EV_39.0")
        traci.vehicle.changeTarget("HH_16_EV_39.0", "161292464#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_39.0", "hh16_ev39_home", flags=32)

        traci.vehicle.resume("HH_16_EV_40.0")
        traci.vehicle.changeTarget("HH_16_EV_40.0", "116495992#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_40.0", "hh16_ev40_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_41.0")
        traci.vehicle.changeTarget("HH_16_EV_41.0", "383060134")
        traci.vehicle.setParkingAreaStop("HH_16_EV_41.0", "hh16_ev41_home", flags=32)

        traci.vehicle.resume("HH_16_EV_42.0")
        traci.vehicle.changeTarget("HH_16_EV_42.0", "-270181835#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_42.0", "hh16_ev42_home", flags=32)

        traci.vehicle.resume("HH_16_EV_43.0")
        traci.vehicle.changeTarget("HH_16_EV_43.0", "123273274#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_43.0", "hh16_ev43_home", flags=32)

        traci.vehicle.resume("HH_16_EV_44.0")
        traci.vehicle.changeTarget("HH_16_EV_44.0", "-170246347#3")
        traci.vehicle.setParkingAreaStop("HH_16_EV_44.0", "hh16_ev44_home", flags=32)

        traci.vehicle.resume("HH_16_EV_45.0")
        traci.vehicle.changeTarget("HH_16_EV_45.0", "223171208#5")
        traci.vehicle.setChargingStationStop("HH_16_EV_45.0", "hh16_ev45_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_46.0")
        traci.vehicle.changeTarget("HH_16_EV_46.0", "425498310")
        traci.vehicle.setParkingAreaStop("HH_16_EV_46.0", "hh16_ev46_home", flags=32)

        traci.vehicle.resume("HH_16_EV_47.0")
        traci.vehicle.changeTarget("HH_16_EV_47.0", "170247586#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_47.0", "hh16_ev47_home", flags=32)

        traci.vehicle.resume("HH_16_EV_48.0")
        traci.vehicle.changeTarget("HH_16_EV_48.0", "461201009#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_48.0", "hh16_ev48_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_49.0")
        traci.vehicle.changeTarget("HH_16_EV_49.0", "-28725393#6")
        traci.vehicle.setChargingStationStop("HH_16_EV_49.0", "hh16_ev49_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_50.0")
        traci.vehicle.changeTarget("HH_16_EV_50.0", "10675848")
        traci.vehicle.setChargingStationStop("HH_16_EV_50.0", "hh16_ev50_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_51.0")
        traci.vehicle.changeTarget("HH_16_EV_51.0", "-27770612#2")
        traci.vehicle.setParkingAreaStop("HH_16_EV_51.0", "hh16_ev51_home", flags=32)

        traci.vehicle.resume("HH_16_EV_52.0")
        traci.vehicle.changeTarget("HH_16_EV_52.0", "32762556#4")
        traci.vehicle.setParkingAreaStop("HH_16_EV_52.0", "hh16_ev52_home", flags=32)

        traci.vehicle.resume("HH_16_EV_53.0")
        traci.vehicle.changeTarget("HH_16_EV_53.0", "-39094287#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_53.0", "hh16_ev53_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_54.0")
        traci.vehicle.changeTarget("HH_16_EV_54.0", "-295555117#2")
        traci.vehicle.setParkingAreaStop("HH_16_EV_54.0", "hh16_ev54_home", flags=32)

        traci.vehicle.resume("HH_16_EV_55.0")
        traci.vehicle.changeTarget("HH_16_EV_55.0", "-255326856#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_55.0", "hh16_ev55_home", flags=32)

        traci.vehicle.resume("HH_16_EV_56.0")
        traci.vehicle.changeTarget("HH_16_EV_56.0", "-22650143#2")
        traci.vehicle.setParkingAreaStop("HH_16_EV_56.0", "hh16_ev56_home", flags=32)

        traci.vehicle.resume("HH_16_EV_57.0")
        traci.vehicle.changeTarget("HH_16_EV_57.0", "217570995#2")
        traci.vehicle.setParkingAreaStop("HH_16_EV_57.0", "hh16_ev57_home", flags=32)

        traci.vehicle.resume("HH_16_EV_58.0")
        traci.vehicle.changeTarget("HH_16_EV_58.0", "-33437190#2")
        traci.vehicle.setParkingAreaStop("HH_16_EV_58.0", "hh16_ev58_home", flags=32)

        traci.vehicle.resume("HH_16_EV_59.0")
        traci.vehicle.changeTarget("HH_16_EV_59.0", "-163313397#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_59.0", "hh16_ev59_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_60.0")
        traci.vehicle.changeTarget("HH_16_EV_60.0", "377905809#2")
        traci.vehicle.setParkingAreaStop("HH_16_EV_60.0", "hh16_ev60_home", flags=32)

        traci.vehicle.resume("HH_16_EV_61.0")
        traci.vehicle.changeTarget("HH_16_EV_61.0", "-246432091#10")
        traci.vehicle.setParkingAreaStop("HH_16_EV_61.0", "hh16_ev61_home", flags=32)

        traci.vehicle.resume("HH_16_EV_62.0")
        traci.vehicle.changeTarget("HH_16_EV_62.0", "-34630547#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_62.0", "hh16_ev62_home", flags=32)

        traci.vehicle.resume("HH_16_EV_63.0")
        traci.vehicle.changeTarget("HH_16_EV_63.0", "92738099")
        traci.vehicle.setParkingAreaStop("HH_16_EV_63.0", "hh16_ev63_home", flags=32)

        traci.vehicle.resume("HH_16_EV_64.0")
        traci.vehicle.changeTarget("HH_16_EV_64.0", "-190053109#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_64.0", "hh16_ev64_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_65.0")
        traci.vehicle.changeTarget("HH_16_EV_65.0", "-309195981#3")
        traci.vehicle.setParkingAreaStop("HH_16_EV_65.0", "hh16_ev65_home", flags=32)

        traci.vehicle.resume("HH_16_EV_66.0")
        traci.vehicle.changeTarget("HH_16_EV_66.0", "418572811#6")
        traci.vehicle.setParkingAreaStop("HH_16_EV_66.0", "hh16_ev66_home", flags=32)

        traci.vehicle.resume("HH_16_EV_67.0")
        traci.vehicle.changeTarget("HH_16_EV_67.0", "-270181835#11")
        traci.vehicle.setChargingStationStop("HH_16_EV_67.0", "hh16_ev67_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_68.0")
        traci.vehicle.changeTarget("HH_16_EV_68.0", "161144029#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_68.0", "hh16_ev68_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_69.0")
        traci.vehicle.changeTarget("HH_16_EV_69.0", "18672433#11")
        traci.vehicle.setChargingStationStop("HH_16_EV_69.0", "hh16_ev69_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_70.0")
        traci.vehicle.changeTarget("HH_16_EV_70.0", "-283737816#4")
        traci.vehicle.setChargingStationStop("HH_16_EV_70.0", "hh16_ev70_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_71.0")
        traci.vehicle.changeTarget("HH_16_EV_71.0", "497514538#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_71.0", "hh16_ev71_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_72.0")
        traci.vehicle.changeTarget("HH_16_EV_72.0", "-390565781")
        traci.vehicle.setParkingAreaStop("HH_16_EV_72.0", "hh16_ev72_home", flags=32)

        traci.vehicle.resume("HH_16_EV_73.0")
        traci.vehicle.changeTarget("HH_16_EV_73.0", "-53175159#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_73.0", "hh16_ev73_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_74.0")
        traci.vehicle.changeTarget("HH_16_EV_74.0", "21250109#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_74.0", "hh16_ev74_home", flags=32)

        traci.vehicle.resume("HH_16_EV_75.0")
        traci.vehicle.changeTarget("HH_16_EV_75.0", "252533210")
        traci.vehicle.setParkingAreaStop("HH_16_EV_75.0", "hh16_ev75_home", flags=32)

        traci.vehicle.resume("HH_16_EV_76.0")
        traci.vehicle.changeTarget("HH_16_EV_76.0", "23863087#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_76.0", "hh16_ev76_home", flags=32)

        traci.vehicle.resume("HH_16_EV_77.0")
        traci.vehicle.changeTarget("HH_16_EV_77.0", "33173445")
        traci.vehicle.setParkingAreaStop("HH_16_EV_77.0", "hh16_ev77_home", flags=32)

        traci.vehicle.resume("HH_16_EV_78.0")
        traci.vehicle.changeTarget("HH_16_EV_78.0", "27245673#10")
        traci.vehicle.setChargingStationStop("HH_16_EV_78.0", "hh16_ev78_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_79.0")
        traci.vehicle.changeTarget("HH_16_EV_79.0", "-203059058#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_79.0", "hh16_ev79_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_80.0")
        traci.vehicle.changeTarget("HH_16_EV_80.0", "14890834#12")
        traci.vehicle.setParkingAreaStop("HH_16_EV_80.0", "hh16_ev80_home", flags=32)

        traci.vehicle.resume("HH_16_EV_81.0")
        traci.vehicle.changeTarget("HH_16_EV_81.0", "-615449790#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_81.0", "hh16_ev81_home", flags=32)

        traci.vehicle.resume("HH_16_EV_82.0")
        traci.vehicle.changeTarget("HH_16_EV_82.0", "165823636")
        traci.vehicle.setChargingStationStop("HH_16_EV_82.0", "hh16_ev82_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_83.0")
        traci.vehicle.changeTarget("HH_16_EV_83.0", "104211826#5")
        traci.vehicle.setChargingStationStop("HH_16_EV_83.0", "hh16_ev83_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_84.0")
        traci.vehicle.changeTarget("HH_16_EV_84.0", "32445770#4")
        traci.vehicle.setParkingAreaStop("HH_16_EV_84.0", "hh16_ev84_home", flags=32)

        traci.vehicle.resume("HH_16_EV_85.0")
        traci.vehicle.changeTarget("HH_16_EV_85.0", "40711859#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_85.0", "hh16_ev85_home", flags=32)

        traci.vehicle.resume("HH_16_EV_86.0")
        traci.vehicle.changeTarget("HH_16_EV_86.0", "225416642#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_86.0", "hh16_ev86_home", flags=32)

        traci.vehicle.resume("HH_16_EV_87.0")
        traci.vehicle.changeTarget("HH_16_EV_87.0", "173084913")
        traci.vehicle.setParkingAreaStop("HH_16_EV_87.0", "hh16_ev87_home", flags=32)

        traci.vehicle.resume("HH_16_EV_88.0")
        traci.vehicle.changeTarget("HH_16_EV_88.0", "-28825900#4")
        traci.vehicle.setChargingStationStop("HH_16_EV_88.0", "hh16_ev88_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_89.0")
        traci.vehicle.changeTarget("HH_16_EV_89.0", "187645376#5")
        traci.vehicle.setParkingAreaStop("HH_16_EV_89.0", "hh16_ev89_home", flags=32)

        traci.vehicle.resume("HH_16_EV_90.0")
        traci.vehicle.changeTarget("HH_16_EV_90.0", "16543102")
        traci.vehicle.setParkingAreaStop("HH_16_EV_90.0", "hh16_ev90_home", flags=32)

        traci.vehicle.resume("HH_16_EV_91.0")
        traci.vehicle.changeTarget("HH_16_EV_91.0", "-432324101#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_91.0", "hh16_ev91_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_92.0")
        traci.vehicle.changeTarget("HH_16_EV_92.0", "33359866#6")
        traci.vehicle.setParkingAreaStop("HH_16_EV_92.0", "hh16_ev92_home", flags=32)

        traci.vehicle.resume("HH_16_EV_93.0")
        traci.vehicle.changeTarget("HH_16_EV_93.0", "-218279120")
        traci.vehicle.setParkingAreaStop("HH_16_EV_93.0", "hh16_ev93_home", flags=32)

        traci.vehicle.resume("HH_16_EV_94.0")
        traci.vehicle.changeTarget("HH_16_EV_94.0", "32340195#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_94.0", "hh16_ev94_home", flags=32)

        traci.vehicle.resume("HH_16_EV_95.0")
        traci.vehicle.changeTarget("HH_16_EV_95.0", "4777169#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_95.0", "hh16_ev95_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_96.0")
        traci.vehicle.changeTarget("HH_16_EV_96.0", "4777171#10")
        traci.vehicle.setParkingAreaStop("HH_16_EV_96.0", "hh16_ev96_home", flags=32)

        traci.vehicle.resume("HH_16_EV_97.0")
        traci.vehicle.changeTarget("HH_16_EV_97.0", "30617772#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_97.0", "hh16_ev97_home", flags=32)

        traci.vehicle.resume("HH_16_EV_98.0")
        traci.vehicle.changeTarget("HH_16_EV_98.0", "254343670#4")
        traci.vehicle.setChargingStationStop("HH_16_EV_98.0", "hh16_ev98_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_99.0")
        traci.vehicle.changeTarget("HH_16_EV_99.0", "-18843862#4")
        traci.vehicle.setParkingAreaStop("HH_16_EV_99.0", "hh16_ev99_home", flags=32)

        traci.vehicle.resume("HH_16_EV_100.0")
        traci.vehicle.changeTarget("HH_16_EV_100.0", "41877362")
        traci.vehicle.setParkingAreaStop("HH_16_EV_100.0", "hh16_ev100_home", flags=32)

        traci.vehicle.resume("HH_16_EV_101.0")
        traci.vehicle.changeTarget("HH_16_EV_101.0", "161111210#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_101.0", "hh16_ev101_home", flags=32)

        traci.vehicle.resume("HH_16_EV_102.0")
        traci.vehicle.changeTarget("HH_16_EV_102.0", "197064630#18")
        traci.vehicle.setParkingAreaStop("HH_16_EV_102.0", "hh16_ev102_home", flags=32)

        traci.vehicle.resume("HH_16_EV_103.0")
        traci.vehicle.changeTarget("HH_16_EV_103.0", "-30617720#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_103.0", "hh16_ev103_home", flags=32)

        traci.vehicle.resume("HH_16_EV_104.0")
        traci.vehicle.changeTarget("HH_16_EV_104.0", "122049943#8")
        traci.vehicle.setChargingStationStop("HH_16_EV_104.0", "hh16_ev104_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_105.0")
        traci.vehicle.changeTarget("HH_16_EV_105.0", "27330922#12")
        traci.vehicle.setParkingAreaStop("HH_16_EV_105.0", "hh16_ev105_home", flags=32)

        traci.vehicle.resume("HH_16_EV_106.0")
        traci.vehicle.changeTarget("HH_16_EV_106.0", "-688370154")
        traci.vehicle.setParkingAreaStop("HH_16_EV_106.0", "hh16_ev106_home", flags=32)

        traci.vehicle.resume("HH_16_EV_107.0")
        traci.vehicle.changeTarget("HH_16_EV_107.0", "156539907#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_107.0", "hh16_ev107_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_108.0")
        traci.vehicle.changeTarget("HH_16_EV_108.0", "24435827")
        traci.vehicle.setChargingStationStop("HH_16_EV_108.0", "hh16_ev108_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_109.0")
        traci.vehicle.changeTarget("HH_16_EV_109.0", "-34774347#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_109.0", "hh16_ev109_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_110.0")
        traci.vehicle.changeTarget("HH_16_EV_110.0", "-522012172#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_110.0", "hh16_ev110_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_111.0")
        traci.vehicle.changeTarget("HH_16_EV_111.0", "685123143#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_111.0", "hh16_ev111_home", flags=32)

        traci.vehicle.resume("HH_16_EV_112.0")
        traci.vehicle.changeTarget("HH_16_EV_112.0", "-13547731#13")
        traci.vehicle.setChargingStationStop("HH_16_EV_112.0", "hh16_ev112_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_113.0")
        traci.vehicle.changeTarget("HH_16_EV_113.0", "163114606#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_113.0", "hh16_ev113_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_114.0")
        traci.vehicle.changeTarget("HH_16_EV_114.0", "-328005193#5")
        traci.vehicle.setParkingAreaStop("HH_16_EV_114.0", "hh16_ev114_home", flags=32)

        traci.vehicle.resume("HH_16_EV_115.0")
        traci.vehicle.changeTarget("HH_16_EV_115.0", "-395369204")
        traci.vehicle.setChargingStationStop("HH_16_EV_115.0", "hh16_ev115_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_116.0")
        traci.vehicle.changeTarget("HH_16_EV_116.0", "-60725640")
        traci.vehicle.setChargingStationStop("HH_16_EV_116.0", "hh16_ev116_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_117.0")
        traci.vehicle.changeTarget("HH_16_EV_117.0", "343781165#1")
        traci.vehicle.setParkingAreaStop("HH_16_EV_117.0", "hh16_ev117_home", flags=32)

        traci.vehicle.resume("HH_16_EV_118.0")
        traci.vehicle.changeTarget("HH_16_EV_118.0", "25835872#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_118.0", "hh16_ev118_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_119.0")
        traci.vehicle.changeTarget("HH_16_EV_119.0", "-34257482#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_119.0", "hh16_ev119_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_120.0")
        traci.vehicle.changeTarget("HH_16_EV_120.0", "-368579482#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_120.0", "hh16_ev120_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_121.0")
        traci.vehicle.changeTarget("HH_16_EV_121.0", "-28217659#6")
        traci.vehicle.setChargingStationStop("HH_16_EV_121.0", "hh16_ev121_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_122.0")
        traci.vehicle.changeTarget("HH_16_EV_122.0", "-23197394#2")
        traci.vehicle.setChargingStationStop("HH_16_EV_122.0", "hh16_ev122_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_123.0")
        traci.vehicle.changeTarget("HH_16_EV_123.0", "107005667#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_123.0", "hh16_ev123_home", flags=32)

        traci.vehicle.resume("HH_16_EV_124.0")
        traci.vehicle.changeTarget("HH_16_EV_124.0", "146749525#6")
        traci.vehicle.setChargingStationStop("HH_16_EV_124.0", "hh16_ev124_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_125.0")
        traci.vehicle.changeTarget("HH_16_EV_125.0", "15216164#1")
        traci.vehicle.setChargingStationStop("HH_16_EV_125.0", "hh16_ev125_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_126.0")
        traci.vehicle.changeTarget("HH_16_EV_126.0", "24436163#3")
        traci.vehicle.setParkingAreaStop("HH_16_EV_126.0", "hh16_ev126_home", flags=32)

        traci.vehicle.resume("HH_16_EV_127.0")
        traci.vehicle.changeTarget("HH_16_EV_127.0", "-33456547#5")
        traci.vehicle.setParkingAreaStop("HH_16_EV_127.0", "hh16_ev127_home", flags=32)

        traci.vehicle.resume("HH_16_EV_128.0")
        traci.vehicle.changeTarget("HH_16_EV_128.0", "332856363#0")
        traci.vehicle.setChargingStationStop("HH_16_EV_128.0", "hh16_ev128_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_129.0")
        traci.vehicle.changeTarget("HH_16_EV_129.0", "-18844833#13")
        traci.vehicle.setChargingStationStop("HH_16_EV_129.0", "hh16_ev129_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_130.0")
        traci.vehicle.changeTarget("HH_16_EV_130.0", "144342279")
        traci.vehicle.setParkingAreaStop("HH_16_EV_130.0", "hh16_ev130_home", flags=32)

        traci.vehicle.resume("HH_16_EV_131.0")
        traci.vehicle.changeTarget("HH_16_EV_131.0", "41877362")
        traci.vehicle.setParkingAreaStop("HH_16_EV_131.0", "hh16_ev131_home", flags=32)

        traci.vehicle.resume("HH_16_EV_132.0")
        traci.vehicle.changeTarget("HH_16_EV_132.0", "247071634")
        traci.vehicle.setChargingStationStop("HH_16_EV_132.0", "hh16_ev132_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_133.0")
        traci.vehicle.changeTarget("HH_16_EV_133.0", "366630605#6")
        traci.vehicle.setChargingStationStop("HH_16_EV_133.0", "hh16_ev133_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_134.0")
        traci.vehicle.changeTarget("HH_16_EV_134.0", "-156465719#5")
        traci.vehicle.setParkingAreaStop("HH_16_EV_134.0", "hh16_ev134_home", flags=32)

        traci.vehicle.resume("HH_16_EV_135.0")
        traci.vehicle.changeTarget("HH_16_EV_135.0", "-170246201#3")
        traci.vehicle.setChargingStationStop("HH_16_EV_135.0", "hh16_ev135_homecs", flags=32)

        traci.vehicle.resume("HH_16_EV_136.0")
        traci.vehicle.changeTarget("HH_16_EV_136.0", "-33118715#0")
        traci.vehicle.setParkingAreaStop("HH_16_EV_136.0", "hh16_ev136_home", flags=32)

    # stop simulation at 86,400 seconds/06:00 a.m.
    if step == 86400:
        print("Simulation closed")
        traci.close();

    # increase simulation step
    step += 1
