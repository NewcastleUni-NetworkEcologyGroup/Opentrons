from opentrons import labware, instruments

metadata = {
    'protocolName': 'Test tips',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A simple test protocol that checks I have set up a give tiprack correctly'
    }

# Set labware to use
trough = labware.load('starlab-E2896-0220', '2')
plate = labware.load('starlab-E1403-0100', '3')
tiprack = labware.load('opentrons-tiprack-300ul', '1')

pipette=instruments.P300_Multi(mount='left')

# for multichannels
column = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']
#for x in column:
#    pipette.pick_up_tip(tiprack[x])
#    pipette.return_tip()

# for single channels
#well = ['A1','B2','C3','D4','E5','F6','G7','H8']
#for x in well:
#    pipette.pick_up_tip(tiprack[x])
#    pipette.return_tip()

# dispense some mineral oil
pipette.set_flow_rate(aspirate=5, dispense=10)
pipette.pick_up_tip(tiprack['A1'])
for x in column:
	pipette.aspirate(30, trough['A1'])
	pipette.move_to(trough['A1'].top(-2))
	pipette.delay(seconds=5)
	pipette.touch_tip(radius = 0.8)
	pipette.dispense(plate[x].bottom(5))
pipette.drop_tip()

# dispense some blue
pipette.set_flow_rate(aspirate=25, dispense=50)
pipette.pick_up_tip(tiprack['A2'])
for x in column:
	pipette.aspirate(30, trough['A2'])
	pipette.move_to(trough['A2'].top(-2))
	pipette.delay(seconds=5)
	pipette.touch_tip(radius = 0.8)
	pipette.dispense(plate[x].bottom(10))
pipette.drop_tip()

# dispense some yellow
pipette.pick_up_tip(tiprack['A3'])
for x in column:
	pipette.aspirate(30, trough['A3'])
	pipette.move_to(trough['A1'].top(-2))
	pipette.delay(seconds=5)
	pipette.touch_tip(radius = 0.8)
	pipette.dispense(plate[x].bottom(10))
pipette.drop_tip()