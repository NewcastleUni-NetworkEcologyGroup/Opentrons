from opentrons import labware, instruments

metadata = {
    'protocolName': 'Dilute extracted DNA',
    'author': 'James Kitson',
    'description': 'A series of commands to dilute the extracted DNA obtained through the spin column extraction proceedure' 
    }

# get the plates loaded
DNA_plate1 = labware.load('starlab-E2896-0600', '4', 'input DNA plate')
#DNA_plate2 = labware.load('starlab-E2896-0600', '5', 'input DNA plate')

diluted_DNA_plate1 = labware.load('starlab-E1403-0100', '7', 'diluted_DNA plate')
#diluted_DNA_plate2 = labware.load('starlab-E1403-0100', '8', 'diluted_DNA plate')

Tris_plate = labware.load('starlab-E2896-0220', '9', 'Tris plate')

# load the tips
tips_10 = labware.load('tiprack-starlab-S1120-3810', '1')
tips_300 = labware.load('tiprack-starlab-S1120-9810', '3')

# set pipettes
pipette300 = instruments.P300_Multi(mount='left', tip_racks=[tips_300])
pipette10 = instruments.P10_Multi(mount='right', tip_racks=[tips_10])

# set the dilution parameters
final_volume: float=200
dilution_factor: float=1/20
Tris_volume: float= final_volume-(final_volume*dilution_factor)

# define lists of locations
#DNAs=[DNA_plate1,DNA_plate2]
DNAs=[DNA_plate1]
#dilutions=[diluted_DNA_plate1,diluted_DNA_plate2]
dilutions=[diluted_DNA_plate1]
wells=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']

Tris = Tris_plate.wells('A1', 'A2','A3', 'A4') 
#Tris = Tris_plate.wells('A5', 'A6','A7', 'A8') 

# Distribute the Tris-HCl
pipette300.pick_up_tip()
columns_in_a_plate: float=12
ticker=0
for plate in dilutions:
    for well in wells:
        Tris_source = ticker//6
        pipette300.aspirate(Tris_volume, Tris_plate[Tris_source].bottom(3)).touch_tip(radius=0.1),
        pipette300.move_to(Tris_plate[Tris_source].top(25)),
        pipette300.dispense(Tris_volume, plate[well].bottom(3))
        ticker+=1
pipette300.drop_tip()

# dilute the DNA extractions
for idx, plate in enumerate(dilutions):
    for well in wells:
        pipette10.pick_up_tip()
        pipette10.transfer(final_volume*dilution_factor,
                            DNAs[idx][well].bottom(0.5),
                            plate[well].top(-8),
                            new_tip='never').mix(4,5).blow_out(plate[well].top(-4))
        pipette10.drop_tip()