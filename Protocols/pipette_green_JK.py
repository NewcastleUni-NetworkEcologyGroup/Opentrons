from opentrons import labware, instruments

metadata = {
    'protocolName': 'Pipette Green from',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A simple test protocol that mixes yellow and blue solutions to make a plate'
    }

trough = labware.load('starlab-E2896-0220', '2')

liquid_trash = trough.cols('12')

plate = labware.load('starlab-E2896-0600', '3')

tiprack = [labware.load('opentrons-tiprack-300ul', slot)
           for slot in ['1', '4']]

pipette=instruments.P300_Multi(mount='left')

pipette.pick_up_tip(tiprack.cols('1'))

pipette.distribute(50, trough.cols('1'),
	plate.cols('1','2','3','4','5','6','7','8','9','10','11','12'),
	disposal_vol=50,
	new_tip='never',
	touch_tip=True)
pipette.drop_tip()

pipette.pick_up_tip(tiprack.cols('2'))

pipette.distribute(50, trough.cols('2'),
	plate.cols('1','2','3','4','5','6','7','8','9','10','11','12'),
	disposal_vol=50,
	new_tip='never',
	touch_tip=True)
pipette.drop_tip()

pipette.pick_up_tip(tiprack.cols('3'))
pipette.mix(3, 50, plate.cols('1','2','3','4','5','6','7','8','9','10','11','12'))
pipette.drop_tip()
