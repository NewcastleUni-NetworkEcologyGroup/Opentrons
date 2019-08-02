from opentrons import labware, instruments, modules

metadata = {
    'protocolName': 'SPRI bead cleanups',
    'author': 'James Kitson',
    }

magdeck = modules.load('magdeck', '7') 
tips50 = labware.load('tiprack-starlab-S1120-2810', '1')
pipette = instruments.P50_Single(mount='left',tip_racks=[tips50])
plate = labware.load('starlab-E1403-5200', '7', share = True) 

magdeck.engage(height=10)
pipette.pick_up_tip()
pipette.move_to(plate.wells('A1'))
pipette.drop_tip(tips50['A1'])
pipette.delay(10)

magdeck.disengage()
