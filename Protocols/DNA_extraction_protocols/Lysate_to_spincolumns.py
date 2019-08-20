from opentrons import labware, instruments

metadata = {
    'protocolName': 'Tissue lysate into PDB+EtOH then into spin column',
    'author': 'James Kitson',
    'description': 'a series of commands that will transfer tissue lysate from a deepwell plate into mixing plates and then on to spin columns' 
    }

# get the plates loaded and spin columns loaded
lysate_plate1 = labware.load('starlab-E2896-0220', '4', 'input lysate plate')
lysate_plate2 = labware.load('starlab-E2896-0220', '5', 'input lysate plate')

mix_plate1 = labware.load('starlab-E2896-0220', '7', 'mixing plate')
mix_plate2 = labware.load('starlab-E2896-0220', '8', 'mixing plate')

spin_cols1 = labware.load('spin_cols_96', '10', 'mixing plate')
spin_cols2 = labware.load('spin_cols_96', '11', 'mixing plate')

# load the tips
tips_300 = [labware.load('tiprack-starlab-S1120-9810', str(slot))
             for slot in [1,2]]

# set pipettes
pipette300 = instruments.P300_Multi(mount='left', tip_racks=tips_300)

lysate_volume: float=200
denature_volume: float=400

# set up lists of labware to iterate across
lysates=[lysate_plate1,lysate_plate2]
mixes=[mix_plate1,mix_plate2]
spins=[spin_cols1,spin_cols2]

for idx, plate in enumerate(lysates):
    for well in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
        pipette300.pick_up_tip()
        pipette300.aspirate(lysate_volume, plate[well].top(-28))
        pipette300.move_to(plate[well].top(25)),
        pipette300.dispense(lysate_volume, mixes[idx][well].bottom(3))
        pipette300.mix(5,lysate_volume, mixes[idx][well].bottom(1.5))
        pipette300.mix(5,lysate_volume, mixes[idx][well].bottom(4))
        pipette300.transfer(lysate_volume+denature_volume,
                            mixes[idx][well].bottom(0.5),
                            spins[idx][well].top(-8),
                            touch_tip=False,
                            new_tip='never').blow_out(spins[idx][well].top(-4))
        pipette300.drop_tip()
        

