from opentrons import labware, instruments

tips1000 = labware.load('opentrons-tiprack-1000ul', '1')
plate1 = labware.load('96-deep-well', '2')

pipette1000 = instruments.P1000_Single(mount='left', tip_racks=[tips1000])

pipette1000.transfer(100, plate1.well('A1'),
                     plate1.well('B1'),
                     touch_tip=True)