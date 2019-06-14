from opentrons import labware, instruments

metadata = {
    'protocolName': 'Test tips',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A simple test protocol that checks I have set up a give tiprack correctly'
    }

tiprack = labware.load('tiprack-starlab-S1181-3810', 1)

pipette=instruments.P10_Multi(mount='right')

column = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']
for x in column:
    pipette.pick_up_tip(tiprack[x])
    pipette.return_tip()
