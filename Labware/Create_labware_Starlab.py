from opentrons import labware

metadata = {
    'protocolName': 'Create_labware_Starlab',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A list of the labware create commands for standard Starlab consumables'
    }
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
######## PCR plates and strips ########
#######################################


#######################################
################ Tips #################
#######################################
