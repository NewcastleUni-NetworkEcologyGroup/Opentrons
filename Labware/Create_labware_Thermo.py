from opentrons import labware

metadata = {
    'protocolName': 'Create_labware_Starlab',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A list of the labware create commands for standard ThermoFisher consumables'
    }

#######################################
############## Microplates ############
#######################################

# Black Thermo micro plates compatible with the Scorpion plate stacker and plate reader
plate_name = 'Thermo-237108'
if plate_name not in labware.list():
    custom_plate = labware.create(
        plate_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=7.1,                     # diameter (mm) of each well on the plate
        depth=11.2,                       # depth (mm) of each well on the plate
        volume=250)

