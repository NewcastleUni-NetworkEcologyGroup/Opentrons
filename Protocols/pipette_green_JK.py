from opentrons import labware, instruments

metadata = {
    'protocolName': 'Pipette Green from',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A simple test protocol that mixes yellow and blue solutions to make a plate'
    }

trough = labware.load('starlab-E2896-0220', '2')

liquid_trash = trough.wells('A12')

plate = labware.load('starlab-E2896-0600', '3')

tiprack = [labware.load('opentrons-tiprack-300ul', slot)
           for slot in ['1', '4']]

pipette=instruments.P300_Multi(mount='left')

pipette.pick_up_tip(tiprack.wells('A1'))

pipette.distribute(50, trough.wells('A1'),
	plate.rows('A'),
	disposal_vol=30,
	new_tip='never',
	touch_tip=False)
pipette.drop_tip()

pipette.pick_up_tip(tiprack.wells('A2'))

pipette.distribute(50, trough.wells('A2'),
	plate.rows('A'),
	disposal_vol=30,
	new_tip='never',
	touch_tip=False)
pipette.drop_tip()

pipette.pick_up_tip(tiprack.wells('A3'))
pipette.mix(3, 50, plate.rows('A'), 
            new_tip='never')
pipette.drop_tip()
