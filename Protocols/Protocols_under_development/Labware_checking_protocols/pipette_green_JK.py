from opentrons import labware, instruments

metadata = {
    'protocolName': 'Pipette Green',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A simple test protocol that mixes yellow and blue solutions to make a plate'
    }

# Set labware to use
tiprack = labware.load('opentrons-tiprack-300ul', '1')
trough = labware.load('starlab-E2896-0220', '2')
plate = labware.load('starlab-E1403-0100', '3')
tips10 = labware.load('tiprack-starlab-S1181-3810', '4')

# reagent setup
mineral_oil = trough.wells('A1')
yellow = trough.wells('A3')
blue = trough.wells('A4')
liquid_trash = trough.wells('A12')
distance_from_oil_surface_to_opening_of_trough_in_mm: float = 20
volume_of_mineral_oil_in_ul: float = 30


# pipette300 setup
pipette300=instruments.P300_Multi(mount='left', tip_racks=[tiprack])
pipette10=instruments.P10_Multi(mount='right', tip_racks=[tips10])

# variables for mineral oil height track
h_oil = -(distance_from_oil_surface_to_opening_of_trough_in_mm + 5)
length = 8
width = 8

def oil_height_track():
    global h_oil
    dh = volume_of_mineral_oil_in_ul/(length*width)
    h_oil -= dh
    #print(h_oil)

# transfer mineral oil
pipette300.set_flow_rate(aspirate=5, dispense=10)
t_count = 0
pipette300.pick_up_tip(tiprack['A1'])
for d in plate.rows('A'):
   # prevent oil buildup in the same tip (replace after each plate fill)
   if t_count == 12:
       pipette300.drop_tip()
       pipette300.pick_up_tip()
       t_count = 1

oil_height_track()
pipette300.aspirate(volume_of_mineral_oil_in_ul, mineral_oil.top(h_oil))
pipette300.delay(seconds=5)
pipette300.dispense(plate.rows('A').bottom(5))
t_count += 1
pipette300.blow_out()
pipette300.drop_tip()

# Distribute the coloured liquids
pipette300.set_flow_rate(aspirate=25, dispense=50)
pipette300.pick_up_tip(tiprack['A2'])

pipette300.distribute(50, trough.rows('A'),
	plate.rows('A'),
	#disposal_vol=30,
	new_tip='never',
	touch_tip=False)
pipette300.drop_tip(home_after=False)

pipette300.pick_up_tip(tiprack['A3'])

pipette300.distribute(50, trough.rows('A'),
	plate.rows('A'),
	#disposal_vol=30,
	new_tip='never',
	touch_tip=False)
pipette300.drop_tip(home_after=False)

#pipette300.pick_up_tip(tiprack['A4'])
#pipette300.mix(3, 50, plate['A1']-['A12'], 
#            new_tip='never')
#pipette300.drop_tip(home_after=False)
