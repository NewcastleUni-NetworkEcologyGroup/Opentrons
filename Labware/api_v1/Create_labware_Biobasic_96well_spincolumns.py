from opentrons import labware, instruments

metadata = {
    'protocolName': 'Create_labware_Starlab',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A list of the labware create commands for standard Starlab consumables'
    }

#######################################
######## PCR plates and strips ########
#######################################

    
    # Starlab 1000ul RPT filter tips - cat no. S1182-1830 without tips - USED AS TRASH TROUGH
plate_name = 'spin_cols_96'
if plate_name not in labware.list():
    custom_plate = labware.create(
        plate_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=7,                     # diameter (mm) of each well on the plate
        depth=25,                       # depth (mm) of tiprack and holder
        volume=960)


### makes sure to remove trash-tiprack-starlab-S1182-1830'