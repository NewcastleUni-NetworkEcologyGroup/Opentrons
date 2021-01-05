from opentrons import labware, instruments

metadata = {
    'protocolName': 'SybrGreen 1 setup',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A protocol to dilute DNA controls and distribute Sybr Green 1'
    }

# Set labware to use
tips300 = labware.load('opentrons-tiprack-1000ul', '9', 'for SybrGreen and DNA dilutions')
tips10_1 = labware.load('opentrons-tiprack-10ul', '2', 'for primers')
tips10_2 = labware.load('opentrons-tiprack-10ul', '3', 'for template DNA')
Control_plate = labware.load('Thermo-237108','4', 'lambda DNA controls')
test_DNA = labware.load('Thermo-237108','5', 'template DNA plate')

tubes = labware.load('opentrons-tuberack-50ml', '6', 'Sybr Green 1 in A1')
trough = labware.load('starlab-E2896-0220', '7', 'Control dilutions')

pipette300 = instruments.P300_Multi(mount='left')
pipette10 = instruments.P10_Multi(mount='right', tip_racks=[tips10_1, tips10_2]) 

pipette300.pick_up_tip(tips300.wells('H1'))
pipette300.transfer(100, trough.wells('A1'), test_DNA.wells('A1'))

pipette300.pick_up_tip(tips300.wells('F2'))
pipette300.transfer(100, trough.wells('A1'), test_DNA.wells('B1'))