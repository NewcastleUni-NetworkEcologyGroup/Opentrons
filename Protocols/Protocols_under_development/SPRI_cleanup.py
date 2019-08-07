from opentrons import labware, instruments, modules

metadata = {
    'protocolName': 'SPRI bead cleanups',
    'author': 'James Kitson',
    }

magdeck = modules.load('magdeck', '7') 
tips50 = labware.load('tiprack-starlab-S1120-2810', '1')
pipette = instruments.P50_Single(mount='left',tip_racks=[tips50])
plate = labware.load('starlab-E1403-5200', '7', share = True) 

pipette.pick_up_tip()
pipette.drop_tip(tips50['A1'])


magdeck.engage(height=15)
pipette.delay(5)
magdeck.disengage()

magdeck.engage(height=16)
pipette.delay(5)
magdeck.disengage()

magdeck.engage(height=17)
pipette.delay(10)
magdeck.disengage()

magdeck.engage(height=18)
pipette.delay(10)
magdeck.disengage()