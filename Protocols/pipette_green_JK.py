from opentrons import labware, instruments

metadata = {
    'protocolName': 'Pipette Green from',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A simple test protocol that mixes yellow and blue solutions to make a plate'
    }

# Set labware to use
trough = labware.load('starlab-E2896-0220', '2')
plate = labware.load('starlab-E2896-0600', '3')
tiprack = labware.load('opentrons-tiprack-300ul', '1')

# reagent setup
mineral_oil = trough.wells('A1')
yellow = trough.wells('A3')
blue = trough.wells('A4')
liquid_trash = trough.wells('A12')
distance_from_oil_surface_to_opening_of_trough_in_mm: float = 10
volume_of_mineral_oil_in_ul: float = 30


# pipette setup
pipette=instruments.P300_Multi(mount='left')

# variables for mineral oil height track
h_oil = -(distance_from_oil_surface_to_opening_of_trough_in_mm + 5)
length = 10
width = 10

def oil_height_track():
    nonlocal h_oil
    dh = volume_of_mineral_oil_in_ul/(length*width)
    h_oil -= dh

# transfer mineral oil
pipette.set_flow_rate(aspirate=5, dispense=10)
t_count = 0
pipette.pick_up_tip()
for d in plate.rows('A'):
   # prevent oil buildup in the same tip (replace after each plate fill)
   if t_count == 12:
       pipette.drop_tip()
       pipette.pick_up_tip()
       t_count = 1

oil_height_track()
pipette.aspirate(volume_of_mineral_oil_in_ul, mineral_oil.top(h_oil))
pipette.delay(seconds=5)
pipette.dispense(plate.rows('A').bottom(5))
t_count += 1
pipette.blow_out()
pipette.drop_tip()

pipette.pick_up_tip(tiprack['A2'])

pipette.distribute(50, trough.wells('A1'),
	plate.rows('A'),
	#disposal_vol=30,
	new_tip='never',
	touch_tip=False)
pipette.drop_tip(home_after=False)

pipette.pick_up_tip(tiprack['A2'])

pipette.distribute(50, trough.wells('A3'),
	plate.rows('A'),
	#disposal_vol=30,
	new_tip='never',
	touch_tip=False)
pipette.drop_tip(home_after=False)

#pipette.pick_up_tip(tiprack['A4'])
#pipette.mix(3, 50, plate['A1']-['A12'], 
#            new_tip='never')
#pipette.drop_tip(home_after=False)
