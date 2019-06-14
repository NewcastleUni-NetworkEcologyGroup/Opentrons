from opentrons import labware

metadata = {
    'protocolName': 'Create_labware_Starlab',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A list of the labware create commands for standard Starlab consumables'
    }

#######################################
######## PCR plates and strips ########
#######################################

# Starlab plate holders (E2396-1641) with cuttable nonskirted cuttable PCR plates (E1403-0100) on top
plate_name = 'starlab-E1403-0100'
if plate_name not in labware.list():
    custom_plate = labware.create(
        plate_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=5.5,                     # diameter (mm) of each well on the plate
        depth=21,                       # depth (mm) of each well on the plate
        volume=350)

#######################################
########### Deepwell plates ###########
#######################################

# Starlab 2.2ml deepwell plates - cat no. E2896-0220
plate_name = 'starlab-E2896-0220'
if plate_name not in labware.list():
    custom_plate = labware.create(
        plate_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=8,                     # diameter (mm) of each well on the plate
        depth=37,                       # depth (mm) of each well on the plate
        volume=2200)

# Starlab 0.6ml deepwell plates - cat no. E2896-0600
plate_name = 'starlab-E2896-0600'
if plate_name not in labware.list():
    custom_plate = labware.create(
        plate_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=6,                     # diameter (mm) of each well on the plate
        depth=28,                       # depth (mm) of each well on the plate
        volume=600)

#######################################
################ Tips #################
#######################################
# RPT filter tips
# Starlab 10ul RPT filter tips - cat no. S1181-3810
tip_name = 'tiprack-starlab-S1181-3810'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=6.4,                     # diameter (mm) of each well on the plate
        depth=63,                       # depth (mm) of tiprack and holder
        volume=10)

#Regular filter tips
# Starlab 1000ul filter tips - cat no. S1122-1830
tip_name = 'tiprack-starlab-S1181-3810'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=8.7,                     # diameter (mm) of each well on the plate
        depth=93.5,                       # depth (mm) of tiprack and holder
        volume=1000)
