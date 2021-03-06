from opentrons import labware, instruments

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
        
# Starlab fully skirted PCR plates (E1403-5200) (no holder needed)  
plate_name = 'starlab-E1403-5200'
if plate_name not in labware.list():
    labware.create(
        plate_name,
        grid=(12, 8),
        spacing=(8.9, 8.9),
        diameter=5.6,
        depth=15,
        volume=200
    )

#######################################
#### Deepwell plates  and troughs #####
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
        
trough_name = 'starlab-E2310-1200'
if trough_name not in labware.list():
    labware.create(
        trough_name,
        grid=(12, 1),
        spacing=(9, 0),
        diameter=8.2,
        depth=41.7,
        volume=22000)

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
        depth=62,                       # depth (mm) of tiprack and holder
        volume=10)

# Starlab 10/20ul XL RPT filter tips - cat no. S1180-3810
tip_name = 'tiprack-starlab-S1180-3810'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=6.4,                     # diameter (mm) of each well on the plate
        depth=62,                       # depth (mm) of tiprack and holder
        volume=10)

# Starlab 100ul RPT filter tips - cat no. S1180-1840
tip_name = 'tiprack-starlab-S1180-1840'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=6.8,                     # diameter (mm) of each well on the plate
        depth=62,                       # depth (mm) of tiprack and holder
        volume=100)

# Starlab 200ul RPT filter tips - cat no. S1180-8810
tip_name = 'tiprack-starlab-S1180-8810'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=6.8,                     # diameter (mm) of each well on the plate
        depth=62,                       # depth (mm) of tiprack and holder
        volume=200)

# Starlab 300ul RPT filter tips - cat no. S1180-9810
tip_name = 'tiprack-starlab-S1180-9810'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=6.8,                     # diameter (mm) of each well on the plate
        depth=62,                       # depth (mm) of tiprack and holder
        volume=300)

# Starlab 1000ul RPT filter tips - cat no. S1182-1830
tip_name = 'tiprack-starlab-S1182-1830'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=8.7,                     # diameter (mm) of each well on the plate
        depth=98.3,                       # depth (mm) of tiprack and holder
        volume=1000)

#Regular filter tips
# Starlab 10ul filter tips - cat no. S1121-3810
tip_name = 'tiprack-starlab-S1121-3810'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=6.4,                     # diameter (mm) of each well on the plate
        depth=62,                       # depth (mm) of tiprack and holder
        volume=10)

# Starlab 10/20ul XL filter tips - cat no. S1120-3810
tip_name = 'tiprack-starlab-S1120-3810'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=6.4,                     # diameter (mm) of each well on the plate
        depth=62,                       # depth (mm) of tiprack and holder
        volume=10)

# Starlab 50ul filter tips - cat no. S1120-2810
tip_name = 'tiprack-starlab-S1120-2810'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=6.8,                     # diameter (mm) of each well on the plate
        depth=62,                       # depth (mm) of tiprack and holder
        volume=50)

# Starlab 100ul ultrapoint filter tips - cat no. S1123-1840
tip_name = 'tiprack-starlab-S1123-1840'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=6.8,                     # diameter (mm) of each well on the plate
        depth=62,                       # depth (mm) of tiprack and holder
        volume=100)

# Starlab 200ul filter tips - cat no. S1120-8810
tip_name = 'tiprack-starlab-S1120-8810'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=6.8,                     # diameter (mm) of each well on the plate
        depth=62,                       # depth (mm) of tiprack and holder
        volume=200)

# Starlab 300ul filter tips - cat no. S1120-9810
tip_name = 'tiprack-starlab-S1120-9810'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=6.8,                     # diameter (mm) of each well on the plate
        depth=62,                       # depth (mm) of tiprack and holder
        volume=300)

# Starlab 1000ul filter tips - cat no. S1122-1830
tip_name = 'tiprack-starlab-S1122-1830'
if tip_name not in labware.list():
    custom_tiprack = labware.create(
        tip_name,                    # name of you labware
        grid=(12, 8),                    # specify amount of (columns, rows)
        spacing=(9, 9),               # distances (mm) between each (column, row)
        diameter=8.7,                     # diameter (mm) of each well on the plate
        depth=98.3,                       # depth (mm) of tiprack and holder
        volume=1000)
    
#######################################
### Calibration section, unhash the appropriate commands to calibrate new labware.
### Do this away from edges on the deck so the robot does not crash
#######################################

# Tips
#tips = labware.load('tiprack-starlab-S1120-2810','5’)
#tips = labware.load('tiprack-starlab-S1120-3810','5’)
#tips = labware.load('tiprack-starlab-S1120-8810','5’)
#tips = labware.load('tiprack-starlab-S1120-9810','5’)
#tips = labware.load('tiprack-starlab-S1121-3810','5’)
#tips = labware.load('tiprack-starlab-S1122-1830','5’)
#tips = labware.load('tiprack-starlab-S1123-1840','5’)
#tips = labware.load('tiprack-starlab-S1180-1840','5’)
#tips = labware.load('tiprack-starlab-S1180-3810','5’)
#tips = labware.load('tiprack-starlab-S1180-8810','5’)
#tips = labware.load('tiprack-starlab-S1180-9810','5’)
#tips = labware.load('tiprack-starlab-S1181-3810','5’)
#tips = labware.load('tiprack-starlab-S1182-1830','5’)

# Trough
#pipette=instruments.P300_Multi(mount='left')
#tips300 = labware.load('opentrons-tiprack-300ul', '2')
#trough = labware.load('starlab-E2310-1200', '5')

# PCR Plates
#tips300 = labware.load('opentrons-tiprack-300ul', '2')
#plate = labware.load('starlab-E1403-0100','5')
#plate = labware.load('starlab-E1403-5200','5')

# Deepwell plates
#tips300 = labware.load('opentrons-tiprack-300ul', '2')
#plate = labware.load('starlab-E2896-0220','5')
#plate = labware.load('starlab-E2896-0600','5')