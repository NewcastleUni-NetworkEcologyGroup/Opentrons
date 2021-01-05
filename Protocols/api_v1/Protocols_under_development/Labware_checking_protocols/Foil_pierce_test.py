from opentrons import labware, instruments

metadata = {
    'protocolName': 'Dilute extracted DNA',
    'author': 'James Kitson',
    'description': 'A series of commands to test piercing film with 10ul and 300ul multichannel pipettes' 
    }

# get the plates loaded
DNA_plate = labware.load('starlab-E2896-0600', '5', 'input DNA plate')

Tris_plate = labware.load('starlab-E2896-0220', '6', 'Tris plate')

# load the tips
tips_10 = labware.load('tiprack-starlab-S1120-3810', '1')
tips_300 = labware.load('tiprack-starlab-S1120-9810', '2')

# set pipettes
pipette300 = instruments.P300_Multi(mount='left', tip_racks=[tips_300])
pipette10 = instruments.P10_Multi(mount='right', tip_racks=[tips_10])

wells=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']

pipette10.pick_up_tip()
ticker=0
for well in wells:
    pipette10.aspirate(10, DNA_plate[well].bottom(3)).touch_tip(radius=0.1),
    pipette10.move_to(DNA_plate[well].top(25)),
    pipette10.dispense(10, DNA_plate[well].bottom(3))
pipette10.drop_tip()

pipette300.pick_up_tip()
ticker=0
for well in wells:
    pipette300.aspirate(30, Tris_plate[well].bottom(3)).touch_tip(radius=0.1),
    pipette300.move_to(Tris_plate[well].top(25)),
    pipette300.dispense(30, Tris_plate[well].bottom(3))
pipette300.drop_tip()